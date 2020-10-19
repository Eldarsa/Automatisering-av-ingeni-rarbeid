# nx: threaded

from utilitiesA2 import *
from shapes.cylinder import Cylinder
from shapes.sphere import Sphere

import random
import numpy as np
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
        head_params = dict(), #dictionary
        joint_params = dict() #nested dictionary (because several origins)
        ):

        #Store all the variables needed to create a lamp
        self.origin = np.array(origin)
        self.base_vector = np.array(base_vector)
        self.base_params = base_params
        self.leg_params = leg_params
        self.head_params = head_params
        self.joint_params = joint_params

        self.joint_origin_list = self.updateJointOrigins()
        self.leg_origin_list = self.updateLegOrigins()

        self.randomizing_span = 3 #This means that a randomized value can span X times the initial value

    #Disse to funksjonene kan snart bli overflødige
    def updateJointOrigins(self):
        origin_list = []
        for joint in self.joint_params:
            origin_list.append(joint["origin"])
        return origin_list

    #Og med det mener jeg også denne
    def updateLegOrigins(self):
        origin_list = []
        for leg in self.leg_params:
            origin_list.append(leg["origin"])
        return origin_list

    def getJointOrigins(self):
        return self.joint_origin_list

    def getLegOrigins(self):
        return self.leg_origin_list

    def generate_initial_base(self, height, diameter):
        self.base_params = {
            "origin": self.origin,
            "vector": self.base_vector,
            "height": height,
            "diameter": diameter
        }
        return self.base_params #just in case of printing for check or whatever

    #This function generates a basic leg skeleton
    def generate_initial_legs(self, 
        number_of_legs,
        leg_diameter,
        joint_diameter,
        leg_height,
        first_leg_angle,
        general_leg_angle = 45,
        twist_angle = 0, #How much each joint twists sideways between legs
        randomize_leg_height = False,
        randomize_leg_angle = False,
        randomize_leg_twist = False,
        ):

        #Reset leg_param dict
        self.leg_params = dict()

        #Find the starting point for the legs based on the base dimensions and origin
        base = self.base_params
        leg_base_origin = base["origin"] + base["vector"] * base["height"]
        base_leg_vector = calculate_vector_using_angles(first_leg_angle, twist_angle)
        
        #create lists for points and vectors
        vector_list = np.array([base_leg_vector])
        origin_list = np.array([leg_base_origin])

        #A tool for later use
        flip_vector = np.array([-1,-1,1])

        #Generate some randomized values for parameters
        vertical_angles = np.array([])
        if randomize_leg_angle == True:
            for i in range(0, number_of_legs):
                np.append(vertical_angles, random.randint(0,90))
        else:
            vertical_angles = np.zeros(number_of_legs)

        twist_angles = np.array([])
        if randomize_leg_twist == True:
            for i in range(0, number_of_legs):
                np.append(twist_angles, random.randint(-90,90))
        else:
            twist_angles = np.zeros(number_of_legs)

        leg_heights = np.array([])
        if randomize_leg_height == True:
            for i in range(0,number_of_legs):
                random_height = randomize_from_reference(leg_height, self.randomizing_span)
                np.append(leg_heights, random_height)
        else:
            leg_heights = np.zeros(number_of_legs)

        #Now loop through and add points and vectors to lists
        for i in range(1, number_of_legs):
            vector = calculate_vector_using_angles(vertical_angles[i-1], twist_angles[i-1]) #-1 because we already have an element in the list
            if i%2 == 0:
                np.append(vector_list, vector*flip_vector) #just twist the vector 180 degrees to ensure stability
            else:
                np.append(vector_list, vector)
        
        for i in range(1, number_of_legs + 1):
            point = origin_list[i-1] + vector_list[i] * leg_heights[i]
            np.append(origin_list, point)
        
        #Make sure to set these lists ass class variables for later reference
        self.joint_origin_list = origin_list
        self.leg_origin_list = origin_list

        #Now append to the leg_params_dictionary all the dictionaries for the legs
        for i in range(0,number_of_legs):
            self.leg_params["leg"+i] = {
                "origin": origin_list[i],
                "vector": vector_list[i],
                "height": leg_heights[i],
                "diameter": leg_diameter
            }

        #And for the joints, but they require one more iteration!
        for i in range(0, number_of_legs+1):
            self.joint_params["joint"+i] = {
                "origin": origin_list[i],
                "diameter": joint_diameter,
            }
        return 0

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
        for leg in self.leg_params:
            instance = Cylinder(
                leg["origin"],
                leg["diameter"],
                leg["height"],
                leg["vector"]
            )
            instance.initForNX()

        #Create all joints
        for joint in self.joint_params:
            instance = Sphere(
                joint["origin"],
                joint["diameter"]
            )
            instance.initForNX()

        '''Gjenstår å lage for hodet!!
        '''

        return 0