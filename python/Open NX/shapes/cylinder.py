import math
import NXOpen
import NXOpen.Annotations
import NXOpen.Features
import NXOpen.GeometricUtilities
import NXOpen.Preferences

class Cylinder:

    def __init__(self, x, y, z, direction_vector, height, diameter, color, material):
        self.x = x
        self.y = y
        self.z = z
        self.direction = direction_vector
        self.diameter = diameter
        self.height = height
        self.color = color
        self.material = material

    def initForNX(self):
        theSession = NXOpen.Session.GetSession()
        workPart = theSession.Parts.Work

        #  The cylinder
        cylinderbuilder1 = workPart.Features.CreateCylinderBuilder(NXOpen.Features.Cylinder.Null)
        
        cylinderbuilder1.Diameter.RightHandSide = str(self.diameter)
        cylinderbuilder1.Height.RightHandSide = str(self.height)
        #cylinderbuilder1.Diameter = self.diameter
        #cylinderbuilder1.Height = self.height
        cylinderbuilder1.Origin = NXOpen.Point3d(float(self.x), float(self.y), float(self.z))
        cylinderbuilder1.Direction = NXOpen.Vector3d(float(self.direction[0]), float(self.direction[1]), float(self.direction[2]))
        cylinderbuilder1.BooleanOption.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create


        self.body = cylinderbuilder1.Commit()
        cylinderbuilder1.Commit()
        cylinderbuilder1.Destroy()

    def subtractFromCylinder(self, object1):
        theSession = NXOpen.Session.GetSession()
        workPart = theSession.Parts.Work

        bodyTarget_ = self.body.CommitFeature()

        subtractfeaturebuilder1 = workPart.Features.CreateBooleanBuilder(NXOpen.Features.BooleanFeature.Null)

        subtractfeaturebuilder1.Target = bodyTarget_.GetBodies()[0] # From where to subtract
        subtractfeaturebuilder1.Tool = object1.GetBodies()[0] # What to subtract
        subtractfeaturebuilder1.Operation = NXOpen.Features.FeatureBooleanType.Subtract

        subtractfeaturebuilder1.Commit()
        subtractfeaturebuilder1.Destroy()
