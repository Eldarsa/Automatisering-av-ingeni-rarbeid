#Basic class in Python
#NXPython/shapes/Block.py
from shapes.block import Block

import math
import NXOpen
import NXOpen.Annotations
import NXOpen.Features
import NXOpen.GeometricUtilities
import NXOpen.Preferences

'''
block = Block(0, 0, 0, 100, 100, 100, "RED", "Steel")
block.initForNX()
block = Block(0, 0, 0, 100, 100, 100, "RED", "Steel")
block.initForNX()
block2 = Block(100, 100, 0, 100, 100, 100, "RED", "Steel")
block2.initForNX()
block3 = Block(200, 200, 0, 100, 100, 100, "RED", "Steel")
block3.initForNX()
block4 = Block(100, 100, 100, 100, 100, 100, "RED", "Steel")
block4.initForNX()
'''

for i in range(1, 5):
	blockN = Block(10*i, 0, i*20, 10, 10, 10, "RED", "Steel")
	blockN.initForNX()