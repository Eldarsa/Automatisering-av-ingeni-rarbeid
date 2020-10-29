# nx: threaded

import math
import random
import numpy as np
from sympy import Line, Point3D, Plane
import copy

import NXOpen
import NXOpen.Annotations
import NXOpen.Features
import NXOpen.GeometricUtilities
import NXOpen.Preferences

from utilitiesA2 import *

class GeneticAlgorithm:

    def __init__(self,
        allow_joint_turn = False,
        allow_head_turn = False,
        allow_move_base = False,
        allow_base_change = False,
        allow_mutations = True,
        generations = False, 
        mutation_range = 1
        ):

        self.allow_joint_turn = allow_joint_turn
        self.allow_head_turn = allow_joint_turn
        self.allow_move_base = allow_move_base
        self.allow_base_change = allow_base_change
        self.allow_mutations = allow_mutations 
        self.mutation_range = mutation_range

        #Set wether there are generation limits or not
        if generations == False:
            self.limit_generations = False
        else:
            self.number_of_generations = generations 

    #Returns x similar copies of lamp
    def createNewInstances(self, lamp, number_of_copies):
        instance_list = []
        for i in range(0,number_of_copies):
            lamp_i = copy.deepcopy(lamp)
            instance_list.append(lamp_i)
        return instance_list

    def crossover(self, lamp1, lamp2, crossover_odds = 0.5):
        #IS IT POSSIBLE TO SWAP DIRECTLY IN DICTIONARIES? WRITE A FUNCTION FOR IT!!
        #I only crossover leg heights and vectors, because those are the most relevant parameters
        #Add all properties you want into lists
        # proplist_1 = []
        # proplist_2 = []

        if random.uniform(0,1) < crossover_odds:
            lamp1.base_params["origin"] = lamp2.base_params["origin"]
        if random.uniform(0,1) < crossover_odds:    
            lamp1.base_params["height"] = lamp2.base_params["height"]
        if random.uniform(0,1) < crossover_odds:
            lamp1.base_params["diameter"] = lamp2.base_params["diameter"]

        for i in range(0, len(lamp1.leg_params)):
            if random.uniform(0,1) < crossover_odds:
                lamp1.leg_params["leg"+str(i)]["vector"] = lamp2.leg_params["leg"+str(i)]["vector"]
            if random.uniform(0,1) < crossover_odds:
                lamp1.leg_params["leg"+str(i)]["height"] = lamp1.leg_params["leg"+str(i)]["height"]

        if random.uniform(0,1) < crossover_odds:
            lamp1.hood_params["hood_direction"] = lamp2.hood_params["hood_direction"]

        lamp1.update_properties()

        return lamp1


    def mutate(self, lamp, mutation_range_high = 0.8, mutation_range_low = 0.3, mutation_odds = 0.1):
        if self.allow_move_base and random.uniform(0,1) < mutation_odds:
            lamp.base_params["origin"] = self.mutate_base_point(lamp.base_params["origin"], mutation_range_low)

        if self.allow_base_change and random.uniform(0,1) < mutation_odds:
            lamp.base_params["height"] = randomize_int_from_reference(lamp.base_params["height"], mutation_range_high)
            lamp.base_params["diameter"] = randomize_int_from_reference(lamp.base_params["diameter"], mutation_range_high)
        
        for key in lamp.leg_params:
            leg = lamp.leg_params[key]

            if key == "leg0": #We do not want negative vertical angles here, so we do it seperately
                if random.uniform(0,1) < mutation_odds:
                    leg["height"] = randomize_int_from_reference(leg["height"], mutation_range_high)
                #Twist vector
                if self.allow_joint_turn and random.uniform(0,1) < mutation_odds:
                    leg["vector"] = self.mutate_vector_angles(leg["vector"], mutation_range_low, firstVector=True) #Mutate with respect to 90 deg. angle

            else:
                if random.uniform(0,1) < mutation_odds:
                    leg["height"] = randomize_int_from_reference(leg["height"], mutation_range_high)
                #Twist vector
                if self.allow_joint_turn and random.uniform(0,1) < mutation_odds:
                    leg["vector"] = self.mutate_vector_angles(leg["vector"], mutation_range_low) #Mutate with respect to 90 deg. angle. 

        if self.allow_head_turn and random.uniform(0,1) < mutation_odds:
            lamp.hood_params["hood_direction"] = self.mutate_hood_direction(lamp.hood_params["hood_direction"], mutation_range_high)

        lamp.update_properties() #Automatically updates joint origins and essential parameters

    def fitness_function(self, list_of_lamps, target):
        
        results = dict()
        for lamp in list_of_lamps:
            accuracy = calculate_accuracy(lamp.hood_params["origin"], lamp.hood_params["hood_direction"], target)
            results[lamp] = accuracy
        
        #return sorted(results.items(), key = lambda item: item[1], reverse=True) #Vet ikke hvilken retning den sorterer
        return sorted(results.items(), key = lambda item: item[1])

    def mutate_vector_angles(self, vector, mutation_range, firstVector = False):

        twist_mutation_deg = random.uniform(-mutation_range*90, mutation_range*90)
        vertical_mutation_deg = random.uniform(-mutation_range*90, mutation_range*90)

        vertical = math.radians(vertical_mutation_deg)
        twist = math.radians(twist_mutation_deg)

        #1) proj onto x-plane:
        xy_normal = np.array([0,0,1])
        xy_proj = project_onto_plane(vector, xy_normal)
        #2) find cross product of xy_normal and proj:
        cross_product = np.cross(xy_normal, xy_proj)
        #3) rotate around y and z:
        v1 = np.dot(rotation_matrix(cross_product, vertical), vector)
        v2 = np.dot(rotation_matrix(xy_normal, twist), v1)

        if firstVector:
            v2[2] = abs(v2[2]) #Just make z-direction positive if vector for first leg

        return v2

    def mutate_hood_direction(self, vector, mutation_range):
        '''Mutates the hood and ensures it always stays
        '''

        twist_mutation_deg = random.uniform(-mutation_range*90, mutation_range*90)
        vertical_mutation_deg = random.uniform(-mutation_range*90, mutation_range*90)

        vertical = math.radians(vertical_mutation_deg)
        twist = math.radians(twist_mutation_deg)

        #1) proj onto x-plane:
        xy_normal = np.array([0,0,1])
        xy_proj = project_onto_plane(vector, xy_normal)
        #2) find cross product of xy_normal and proj:
        cross_product = np.cross(xy_normal, xy_proj)
        #3) rotate around y and z:
        v1 = np.dot(rotation_matrix(cross_product, vertical), vector)
        v2 = np.dot(rotation_matrix(xy_normal, twist), v1)

        return v2

    def mutate_base_point(self, point, mut_range):
        new_point = [randomize_int_from_reference(point[0], mut_range), randomize_int_from_reference(point[1], mut_range), 0]
        return np.array(new_point)
        
    def perform_selection(self, lamplist, 
            target, 
            max_generations = 20, 
            success_criteria = 5):

        generation_counter = 0
        best_accuracy = float("inf")
        for i in range(0, max_generations):
            
            results = self.fitness_function(lamplist, target) #Returns a dictionary of sorted accuracy values
            keys_list = list(results)

            bestlamp = keys_list[0][0]
            print("Best lamp: ", bestlamp, type(bestlamp))
            if keys_list[0][1] < success_criteria:
                return bestlamp #SJEKK AT DET FAKTISK ER LAMPEN SOM RETURNERES

            new_lamps = []
            for j in range(0, math.floor(len(results)/2)):
                lamp_keep = copy.deepcopy(keys_list[j][0])
                new_lamps.append(lamp_keep)
                print("lampen vi kopierer over: ", lamp_keep)
                lamp1 = copy.deepcopy(keys_list[j][0])
                new_lamps.append(lamp1)
                lamp2 = keys_list[j+1][0]
                self.crossover(lamp1, lamp2, crossover_odds=0.5)
                self.mutate(lamp1, mutation_range_low=0.6)
                print("Den nye muterte lampen: ", lamp1)
            
            if len(results) % 2 != 0:
                #last lamp to be copied
                index = math.floor(len(results)/2)
                last_lamp = copy.deepcopy(keys_list[index][0])
                new_lamps.append(last_lamp)

            lamplist = new_lamps

            generation_counter+=1
            best_accuracy = keys_list[0][1]
            print("Best accuracy gen", generation_counter, best_accuracy)

        return bestlamp