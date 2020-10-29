# nx: threaded

from utilitiesA2 import *
from shapes.cylinder import Cylinder
from shapes.sphere import Sphere

import random
import numpy as np
import math
import NXOpen
import NXOpen.Annotations
import NXOpen.Features
import NXOpen.GeometricUtilities
import NXOpen.Preferences

class Lamp:

    '''
    This class should only take the 'skeleton' of the lamp and be able to regenerate its
    parameters and updating values systematically. This is to store the data for individual lamps.
    '''

    def __init__(self, 
        origin = np.array([0,0,0]),
        base_vector = np.array([0,0,1]),
        base_params = dict(), #dictionary
        leg_params = dict(), #nested dictionary
        hood_params = dict(), #dictionary
        joint_params = dict() #nested dictionary (because several origins)
        ):

        #Store all the variables needed to create a lamp
        self.origin = np.array(origin)
        self.base_vector = np.array(base_vector)
        self.base_params = base_params
        self.leg_params = leg_params
        self.hood_params = hood_params
        self.joint_params = joint_params


    def generate_initial_base(self, height, diameter):
        self.base_params = {
            "origin": self.origin,
            "vector": self.base_vector,
            "height": height,
            "diameter": diameter
        }
        return 0

    #This function generates a basic leg skeleton
    def generate_initial_legs(self, 
        number_of_legs,
        leg_diameter,
        joint_diameter,
        leg_height,
        first_leg_angle,
        general_leg_angle = 45,
        twist_angle = 0 #How much each joint twists sideways between legs
        ):

        #Reset leg_param dict
        self.leg_params = dict()
        self.number_of_legs = number_of_legs

        #Find the starting point for the legs based on the base dimensions and origin
        base = self.base_params
        leg_base_origin = base["origin"] + base["vector"] * base["height"]
        base_leg_vector = self.calculate_vector_using_angles(first_leg_angle, twist_angle)
        
        #create lists for points and vectors
        vector_list = [base_leg_vector]
        origin_list = [leg_base_origin]

        #A tool for later use
        flip_vector = np.array([-1,-1,1])

        #Generate lists of values used for initial creation:
        vertical_angles = np.zeros(number_of_legs) #List of zeros
        vertical_angles.fill(general_leg_angle) #General leg angle as initial vertical leg angle
        twist_angles = np.zeros(number_of_legs) #No twist initially
        leg_heights = np.zeros(number_of_legs) #List of zeros
        leg_heights.fill(leg_height) #Fill with standarized leg height


        #Now loop through and add points and vectors to lists
        #Vectors
        for i in range(1, number_of_legs):
            vector = self.calculate_vector_using_angles(vertical_angles[i-1], twist_angles[i-1]) #-1 because we already have an element in the list
            if i%2 == 0:
                vector_list.append(vector) #just twist the vector 180 degrees to ensure stability
            else:
                vector_list.append(vector*flip_vector)
        #Origins
        for i in range(1, number_of_legs+1):
            point = np.array(origin_list[i-1] + (vector_list[i-1] * leg_heights[i-1]))
            origin_list.append(point)


        #Now append to the leg_params_dictionary all the dictionaries for the legs
        for i in range(0,number_of_legs):
            self.leg_params["leg"+str(i)] = {
                "origin": origin_list[i],
                "vector": vector_list[i],
                "height": leg_heights[i],
                "diameter": leg_diameter
            }

        #And for the joints, but they require one more iteration!
        for i in range(0, number_of_legs+1):
            self.joint_params["joint"+str(i)] = {
                "origin": origin_list[i],
                "diameter": joint_diameter,
            }

        return 0
    
    def generate_initial_hood(self, hood_diameter,
            thickness,
            hood_cutoff_length, 
            cutoff_factor,
            hood_direction, 
            randomize_initial_vector = False):

        key = list(self.joint_params)[-1] #Gets the key for the last joint
        joint = self.joint_params[key] #Finds the reference to the last joint
        origin = joint["origin"] #Point of last joint
        if randomize_initial_vector:
            hood_direction = convert_to_unit(get_random_vector()) #Get random unit vector
            sphere_center = origin + (hood_diameter/2. * hood_direction)
        else:
            sphere_center = origin + (hood_diameter/2. * hood_direction) # point for center of sphere

        #Save all the necessary hood parameters into dictionary
        self.hood_params = {
            "origin": origin,
            "center": sphere_center,
            "hood_direction": hood_direction,
            "outer_diameter": hood_diameter,
            "inner_diameter": hood_diameter - (thickness*2),
            "thickness": thickness,
            "cutoff_origin": origin + hood_cutoff_length*hood_direction,
            "cutoff_height": hood_diameter - hood_cutoff_length,
            "cutoff_factor": cutoff_factor
        }
    
    def generateInNX(self):

        #Create base cylinder
        base = Cylinder(
            self.base_params["origin"],
            self.base_params["diameter"],
            self.base_params["height"],
            self.base_params["vector"]
            )
        base.initForNX()

        #Create all legs
        for key in self.leg_params:
            leg = self.leg_params[key]
            instance = Cylinder(
                leg["origin"],
                leg["diameter"],
                leg["height"],
                leg["vector"]
            )
            instance.initForNX()

        #Create all joints
        for key in self.joint_params:
            joint = self.joint_params[key]
            instance = Sphere(
                joint["origin"],
                joint["diameter"]
            )
            instance.initForNX()

        #Create hood
        outer_hood = Sphere(
            self.hood_params["center"],
            self.hood_params["outer_diameter"],
        )
        outer_hood.initForNX()

        inner_hood = Sphere(
            self.hood_params["center"],
            self.hood_params["inner_diameter"],
        )
        inner_hood.initForNX()
        outer_hood.subtract(inner_hood)

        cutoff = Cylinder(
            self.hood_params["cutoff_origin"],
            self.hood_params["outer_diameter"],
            self.hood_params["cutoff_height"],
            self.hood_params["hood_direction"]
        )
        cutoff.initForNX()
        outer_hood.subtract(cutoff)


    def get_property_list(self):
        properties = []
        properties.append(self.base_params["origin"])
        properties.append(self.base_params["height"])
        properties.append(self.base_params["diameter"])
        for leg in self.leg_params:
            l = self.leg_params[leg]
            properties.append(l["height"])
            properties.append(l["vector"])
        properties.append(self.hood_params["outer_diameter"])
        properties.append(self.hood_params["hood_direction"])
        return properties


    def update_properties_from_list(self, p_list):
        print(p_list)
        self.base_params["origin"] = p_list[0]
        self.base_params["height"] = p_list[1]
        self.base_params["diameter"] = p_list[2]

        #Set vectors and joints
        vector_list = [] #Create array with base_vector
        origin_list = [p_list[0] + self.base_params['vector']*self.base_params["height"]] #Create array with base_origin
        leg_heights = []

        counter = 0 #Keeps track of where we are in the property list
        for i in range(0, self.number_of_legs+1):
            if i == 0:
                self.joint_params["joint"+str(i)]["origin"] = origin_list[i]
            else:
                leg_heights.append(p_list[3+counter])
                vector_list.append(p_list[3+counter+1])
                point = np.array(origin_list[i-1] + (vector_list[i-1] * leg_heights[i-1]))
                origin_list.append(point)
                counter+=2
                #Update leg dict
                self.leg_params["leg"+str(i-1)]["origin"] = origin_list[i-1]
                self.leg_params["leg"+str(i-1)]["vector"] = vector_list[i-1]
                self.leg_params["leg"+str(i-1)]["height"] = leg_heights[i-1]
                #Update joint dict
                self.joint_params["joint"+str(i)]["origin"] = origin_list[i]

        #Update hood parameters
        key = list(self.joint_params)[-1] #Find last joint
        joint = self.joint_params[key] #finds the point of the last joint

        self.hood_params["outer_diameter"] = p_list[3+counter]
        self.hood_params["hood_direction"] = p_list[4+counter]
        #Update dependant hood parameters
        self.hood_params["inner_diameter"] = self.hood_params["outer_diameter"] - (self.hood_params["thickness"]*2)
        self.hood_params["origin"] = joint["origin"] + self.hood_params["hood_direction"] * (self.hood_params["outer_diameter"] / 2.)
        self.hood_params["cutoff_height"] = self.hood_params["cutoff_factor"]*self.hood_params["outer_diameter"]
        self.hood_params["cutoff_origin"] = joint["origin"] + self.hood_params["hood_direction"] * self.hood_params["cutoff_height"]

        return 0


    def print_properties(self):
        p_list = self.get_property_list()
        print(p_list)


    def calculate_vector_using_angles(self, v_angle_deg, twist_deg):
        v_angle = math.radians(v_angle_deg)
        twist = math.radians(twist_deg)
        v = np.array([np.cos(twist)*np.cos(v_angle), np.sin(twist)*np.cos(v_angle), np.sin(v_angle)])
        return convert_to_unit(v)

    #This function detects any changes in key parameteres and update the skeleton to fit automatically
    def update_properties(self):
        
        #Set first joint and leg origin
        self.leg_params["leg0"]["origin"] = self.base_params["origin"] + self.base_params["vector"]*self.base_params["height"]
        self.joint_params["joint0"]["origin"] = self.leg_params["leg0"]["origin"]

        for i in range(1, len(self.leg_params)+1):
            if i != len(self.leg_params):
                last_leg = self.leg_params["leg"+str(i-1)]
                self.leg_params["leg"+str(i)]["origin"] = last_leg["origin"] + last_leg["vector"]*last_leg["height"]
                self.joint_params["joint"+str(i)]["origin"] = self.leg_params["leg"+str(i)]["origin"]
            else:
                last_leg = self.leg_params["leg"+str(i-1)]
                self.joint_params["joint"+str(i)]["origin"] = last_leg["origin"] + last_leg["vector"]*last_leg["height"]

                for j in range(0,2):
                    if (last_leg["vector"][j] < 0 and self.hood_params["hood_direction"][j] > 0) or (last_leg["vector"][j] > 0 and self.hood_params["hood_direction"][j] < 0):
                        self.hood_params["hood_direction"][j] = self.hood_params["hood_direction"][j]*(-1)

                print("Joint origin:", self.joint_params["joint"+str(i)]["origin"])
                self.hood_params["origin"] = self.joint_params["joint"+str(i)]["origin"] #Set hood origin aswell
                self.hood_params["center"] = self.joint_params["joint"+str(i)]["origin"] + self.hood_params["hood_direction"]*self.hood_params["outer_diameter"]/2. #Set hood origin aswell

        self.hood_params["cutoff_origin"] = self.hood_params["origin"] + self.hood_params["hood_direction"]*self.hood_params["cutoff_factor"]*self.hood_params["outer_diameter"]
        self.hood_params["cutoff_height"] = self.hood_params["outer_diameter"]-self.hood_params["outer_diameter"]*self.hood_params["cutoff_factor"]
        
        return 0