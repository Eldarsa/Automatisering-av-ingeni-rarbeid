from shapes.sphere import Sphere
from shapes.block import Block
from shapes.cylinder import Cylinder
from shapes.cone import Cone
import numpy
import math
import NXOpen
import NXOpen.Annotations
import NXOpen.Features
import NXOpen.GeometricUtilities
import NXOpen.Preferences

def main():

	sphere_diameter = 30
	cyl_diameter = 20

	block1 = Block(0,0,0,50,20,20)
	block1.initForNX()

	sphere = Sphere(50,10,10, sphere_diameter)
	sphere.initForNX()

	cyl_subtract1 = Cylinder(0,10,10, cyl_diameter, 90)
	cyl_subtract1.initForNX()
	cyl_subtract2 = Cylinder(0,10,10, cyl_diameter, 90)
	cyl_subtract2.initForNX()
	sphere.subtract(cyl_subtract1)
	block1.subtract(cyl_subtract2)
	return 0

main()
