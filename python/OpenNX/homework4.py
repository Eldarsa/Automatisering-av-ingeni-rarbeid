from shapes.cylinder import Cylinder

import math
import NXOpen
import NXOpen.Annotations
import NXOpen.Features
import NXOpen.GeometricUtilities
import NXOpen.Preferences

#********************PROGRAM*********************
def main():

    x = 0
    y = 0
    z = 0

    holes_along = 10
    holes_around = 20

    cyl_outer_dia = 50
    cyl_length = 100
    cyl_thickness = 0.5
    cyl_inner_dia = getInnerDiameter(cyl_outer_dia, cyl_thickness)

    hole_diameter = 4
    hole_height = cyl_thickness + 10

    initial_vector = [1,0,0]

    #These variables make the math of placing the holes correct
    horisontal_distribution = getHorisontalDistributionSpace(cyl_length, holes_along)
    angular_distribution = getAngularDistributionSpace(holes_around)
    coordinate_matrix = getCenterCoordinates(x,y,z,horisontal_distribution,
    angular_distribution, holes_along, holes_around, cyl_inner_dia)
    vectors = getDirectionalVectors(holes_around, angular_distribution)

    #Create main cylinder
    main_cylinder = Cylinder(x, y, z, cyl_outer_dia, cyl_length,
    initial_vector, "Grey", "Steel")
    
    #Make a hole in main cylinder
    inner_cylinder_subtract = Cylinder(x, y, z, cyl_inner_dia, cyl_length,
    initial_vector, "Grey", "Steel")

    #Initialize cylinders
    main_cylinder.initForNX()
    inner_cylinder_subtract.initForNX()
    main_cylinder.subtract(inner_cylinder_subtract)

    #Loop to subtract all peripheral holes
    for center in coordinate_matrix:
        for i in range(0,len(center)):
            print(center[i][0])
            print(i)
            print(vectors[i])
            print("Eldar")
            cyl = Cylinder(center[i][0], center[i][1], center[i][2], hole_diameter, 
            hole_height, vectors[i], "Red", "Steel")
            cyl.initForNX()
            main_cylinder.subtract(cyl)

    return 0

#********************FUNCTIONS*******************

def getInnerDiameter(inner_dia, thickness):
    return inner_dia - thickness * 2

def getHorisontalDistributionSpace(length, holes_along):
    return length / (holes_along + 1)

def getAngularDistributionSpace(holes_around):
    return math.radians(360 / holes_around)

def getCenterCoordinates(x, y, z, horisontal_distribution, angular_distribution, 
    holes_along, holes_around, cyl_inner_dia):

    coordinate_matrix = []
    for i in range(0, holes_along):
        coordinate_list = []
        for j in range(0, holes_around):
            coordinate_list.append(
                [
                    x + (i+1)*horisontal_distribution,
                    (y + cyl_inner_dia / 2 - 2) * math.cos(angular_distribution * j),
                    (z + cyl_inner_dia / 2 - 2) * math.sin(angular_distribution * j)
                ]
            )
        #Append a set of centers for holes around a given x
        coordinate_matrix.append(coordinate_list)
    return coordinate_matrix

def getDirectionalVectors(holes_around, angular_distribution):
        
    vector_list = []
    for i in range (0, holes_around):
        vector_list.append(
            [
                0,
                1*math.cos(angular_distribution * i),
                1*math.sin(angular_distribution * i)
            ]
        )
    return vector_list

#RUN
main()