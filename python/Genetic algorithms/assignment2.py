# nx: threaded

from GeneticAlgorithm import *
from utilitiesA2 import *
from lamp import Lamp

import math
import random
import numpy as np

from shapes.cylinder import Cylinder
from shapes.sphere import Sphere

import NXOpen
import NXOpen.Annotations
import NXOpen.Features
import NXOpen.GeometricUtilities
import NXOpen.Preferences

def main():

##################################__PARAMETERS__##########################################

    #Target point   
    target = np.array([100,100,100])

    #Define some initial directional parameters
    base_origin = np.array([0,0,0]) #Where lamp base is placed in the 3D-space
    base_vector = np.array([0,0,1]) #Lamp direction

    #How many legs should the lamp have?
    number_of_legs = 4
    number_of_joints = number_of_legs + 1

    #Number of lampcopies to perform selection on
    number_of_lamps = 8

    #Generational limits and parameteres
    max_generations = 30
    success_criteria = 10

    #Some general initial values
    initial_leg_length = 30
    leg_diameter = 5
    joint_diameter = leg_diameter * 1 #Multiply by a constant
    base_leg_angle = 45 #Angle of first leg (degrees)
    general_leg_angle = 45 #Angle of all other legs
    base_diameter = 40
    base_height = 10
    hood_diameter = 30.
    hood_thickness = 2
    hood_cutoff_factor = 0.8
    hood_cutoff_length = hood_diameter * hood_cutoff_factor #Where the lamp head opens in reference to its leg-connection
    hood_direction = np.array([-1,0,0]) #The direction of the first hood.
    
    #Optional settings
    allow_joint_turn = True
    allow_head_turn = True
    allow_base_change = False #Fix base in position or not
    allow_mutations = True
    mutation_range = 0.8 #How much percentwise a leg can mutate in one generation
    generations = 30 #False or an int!
    randomize_initial_creation = True #Mutate all parameteres of first lamp 



##################################__PROCEDURE__##########################################

    #SETUP INITIAL LAMP
    lamp = Lamp(origin = base_origin, base_vector = base_vector) #Instantiate lamp object
    lamp.generate_initial_base(base_height, base_diameter) #Generate Base
    #Generate legs:
    lamp.generate_initial_legs(number_of_legs, 
        leg_diameter, 
        joint_diameter,
        initial_leg_length,
        base_leg_angle,
        general_leg_angle,
        randomize_leg_height = False,
        randomize_leg_angle = False,
        randomize_leg_twist = False,
        )

    lamp.generate_initial_hood(hood_diameter,
        hood_thickness,
        hood_cutoff_length,
        hood_cutoff_factor,
        hood_direction,
        randomize_initial_vector = True)

    #SETUP GENETIC ALGORITHM
    GA = GeneticAlgorithm(allow_joint_turn = allow_joint_turn,
    allow_head_turn = allow_head_turn,
    allow_base_change = allow_base_change,
    allow_mutations = allow_mutations,
    generations = generations,
    mutation_range = mutation_range
    )

    #Mutate first lamp
    if randomize_initial_creation == True:
        GA.mutate(lamp, mutation_range_high = 0.8, mutation_range_low = 0.3, mutation_odds = 1)

    #Create new lamps
    lamplist = GA.createNewInstances(lamp, number_of_lamps)

    #Mutate all new lamps to create different initial lamps with different properties
    for lamp_x in lamplist:
        GA.mutate(lamp_x, mutation_range_high = 0.8, mutation_range_low = 0.3, mutation_odds = 0.1)

    #Perform selection and select the best lamp satisfying the requirements
    best_lamp = GA.perform_selection(lamplist, target, max_generations, success_criteria)


    #Generate target in NX
    target_sphere = Sphere(target, success_criteria, color = "RED")
    target_sphere.initForNX()
    
    #Generate final lamp in NX
    best_lamp.generateInNX()

main()