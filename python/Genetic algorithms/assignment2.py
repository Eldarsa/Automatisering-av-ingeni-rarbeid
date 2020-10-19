# nx: threaded

from utilitiesA2 import *
from lamp import Lamp

import math
import random
import numpy as np

def main():

    #Define point in space to point light at    
    target = [0,15,0]

    #Define some initial directional parameters
    base_origin = [0,0,0]
    base_vector = [0,0,1]

    #How many legs should the lamp have?
    number_of_legs = 3
    number_of_joints = calculate_joints(number_of_legs)

    #Some general initial values
    initial_leg_length = 30
    leg_diameter = 10
    joint_diameter = leg_diameter * 1.2 #Multiply by a constant
    base_leg_angle = 45 #Angle of first leg (degrees)
    general_leg_angle = 45 #Angle of all other legs
    base_diameter = 30
    base_height = 10
    head_diameter = 30
    head_cutoff_point = head_diameter * 0.8 #Where the lamp head opens in reference to its leg-connection
    
    #Settings
    allow_joint_turn = False
    allow_head_turn = True
    allow_base_change = False
    limit_mutations = True
    limit_generations = False
    randomize_initial_creation = False

    #Generate the first lamp parameters - returns dictionaries cointaing all necessities
    #Denne delen her e ganske uklar foreløpg
    '''
    base_params = generate_base(base_diameter, base_height, base_origin, base_vector)
    leg_params = generate_legs(number_of_legs, leg_diameter, base_leg_angle)
    head_origin = calculate_head_origin()
    head_center = calculate_head_center()
    head_params = {
        "diameter": head_diameter,
        "center": head_center,
        "cutoff": head_cutoff_point
    }
    '''

    lamp = Lamp()
    lamp.generate_initial_base(base_height, base_diameter)
    lamp.generate_initial_legs(number_of_legs, 
        leg_diameter, 
        joint_diameter,
        initial_leg_length,
        base_leg_angle,
        general_leg_angle
        )
    lamp.generateInNX()


main()