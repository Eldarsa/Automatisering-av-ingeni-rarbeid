from shapes.cylinder import Cylinder
from shapes.block import Block

import math
import NXOpen
import NXOpen.Annotations
import NXOpen.Features
import NXOpen.GeometricUtilities
import NXOpen.Preferences

cylinder = Cylinder(0,0,0, [0,0,1], 100, 50,"RED", "Steel")
cylinder.initForNX()

cylinder2 = Cylinder(0,0,0, [0,0,1], 100, 40,"RED", "Steel")

cylinder.subtractFromCylinder(cylinder2)