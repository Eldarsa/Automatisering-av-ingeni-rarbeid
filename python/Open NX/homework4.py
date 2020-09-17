from shapes.cylinder import cylinder

import math
import NXOpen
import NXOpen.Annotations
import NXOpen.Features
import NXOpen.GeometricUtilities
import NXOpen.Preferences

#Import vektorer?

#Center coordinates
x = 0
y = 0
z = 0

holes_along = 4
holes_around = 6

cyl_outer_dia = 50
cyl_length = 100
cyl_thickness = 0.5
cyl_inner_dia = getInnerDiameter(cyl_outer_dia, cyl_thickness)


def getInnerDiameter(inner_dia, thickness):
    return 0