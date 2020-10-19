#NXPython/shapes/cone.py
import math
import NXOpen
import NXOpen.Annotations
import NXOpen.Features
import NXOpen.GeometricUtilities
import NXOpen.Preferences

class Cone:

    def __init__(self, x, y, z, base_diameter, top_diameter, height, half_angle = 45, direction = [1,0,0], color ="Grey", material="Plastic"):
        self.base_diameter = base_diameter
        self.top_diameter = top_diameter
        self.height = height
        self.half_angle = half_angle
        self.x = x
        self.y = y
        self.z = z
        self.direction = direction
        self.color = color
        self.material = material

    def initForNX(self):
        theSession  = NXOpen.Session.GetSession()
        workPart = theSession.Parts.Work
		
        #The cone
        conebuilder1 = workPart.Features.CreateConeBuilder(NXOpen.Features.Cone.Null)
        
        conebuilder1.BaseDiameter.RightHandSide = str(self.base_diameter) # Writing the right hand side of the expression
        conebuilder1.TopDiameter.RightHandSide = str(self.top_diameter)
        conebuilder1.Height.RightHandSide = str(self.height)
        #conebuilder1.HalfAngle.RightHandSide = str(self.half_angle)
        conebuilder1.Axis.Point = workPart.createNXOpen.Point3d(float(self.x), float(self.y), float(self.z))
        conebuilder1.Axis.Direction = NXOpen.Vector3d(float(self.direction[0]),float(self.direction[1]),float(self.direction[2]))
        conebuilder1.BooleanOption.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
        
        self.body = conebuilder1.Commit().GetBodies()[0]
        conebuilder1.Destroy() 
		
    def subtract(self, tool):
        theSession = NXOpen.Session.GetSession()
        workPart = theSession.Parts.Work

        subtractfeaturebuilder1 = workPart.Features.CreateBooleanBuilder(NXOpen.Features.BooleanFeature.Null)

        subtractfeaturebuilder1.Target = self.body  #bodyTarget_.GetBodies()[0] # From where to subtract
        subtractfeaturebuilder1.Tool = tool.body # What to subtract
        subtractfeaturebuilder1.Operation = NXOpen.Features.FeatureBooleanType.Subtract

        subtractfeaturebuilder1.Commit()
        subtractfeaturebuilder1.Destroy()