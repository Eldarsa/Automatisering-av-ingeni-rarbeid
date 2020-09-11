# NX 1911
# Journal created by Eldar on Wed Sep  9 15:44:05 2020 W. Europe Daylight Time
#
import math
import NXOpen
import NXOpen.Annotations
import NXOpen.Features
import NXOpen.GeometricUtilities
import NXOpen.Preferences
def main() : 

    theSession  = NXOpen.Session.GetSession()
    workPart = theSession.Parts.Work
    displayPart = theSession.Parts.Display
    rotMatrix1 = NXOpen.Matrix3x3()
    
    rotMatrix1.Xx = -0.077756201877709444
    rotMatrix1.Xy = 0.98137465629618481
    rotMatrix1.Xz = -0.1756637613428074
    rotMatrix1.Yx = -0.20912077779185917
    rotMatrix1.Yy = 0.15622284863933075
    rotMatrix1.Yz = 0.96533047287379448
    rotMatrix1.Zx = 0.97479355422842584
    rotMatrix1.Zy = 0.11179537352933165
    rotMatrix1.Zz = 0.19307853607316597
    translation1 = NXOpen.Point3d(-53.583149362584649, -66.58496568714142, 35.106040227029119)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix1, translation1, 0.86451141643753715)
    
    # ----------------------------------------------
    #   Menu: Orient View->Trimetric
    # ----------------------------------------------
    workPart.ModelingViews.WorkView.Orient(NXOpen.View.Canned.Trimetric, NXOpen.View.ScaleAdjustment.Fit)
    
    # ----------------------------------------------
    #   Menu: Insert->Sketch
    # ----------------------------------------------
    markId1 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Enter Sketch")
    
    markId2 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Update Model from Sketch")
    
    theSession.BeginTaskEnvironment()
    
    markId3 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    sketchInPlaceBuilder1 = workPart.Sketches.CreateSketchInPlaceBuilder2(NXOpen.Sketch.Null)
    
    origin1 = NXOpen.Point3d(0.0, 0.0, 0.0)
    normal1 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    plane1 = workPart.Planes.CreatePlane(origin1, normal1, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    sketchInPlaceBuilder1.PlaneReference = plane1
    
    unit1 = workPart.UnitCollection.FindObject("MilliMeter")
    expression1 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression2 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    sketchAlongPathBuilder1 = workPart.Sketches.CreateSketchAlongPathBuilder(NXOpen.Sketch.Null)
    
    theSession.SetUndoMarkName(markId3, "Create Sketch Dialog")
    
    datumAxis1 = workPart.Datums.FindObject("DATUM_CSYS(0) X axis")
    direction1 = workPart.Directions.CreateDirection(datumAxis1, NXOpen.Sense.Forward, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    datumPlane1 = workPart.Datums.FindObject("DATUM_CSYS(0) XY plane")
    datumCsys1 = workPart.Features.FindObject("DATUM_CSYS(0)")
    point1 = datumCsys1.FindObject("POINT 1")
    xform1 = workPart.Xforms.CreateXformByPlaneXDirPoint(datumPlane1, direction1, point1, NXOpen.SmartObject.UpdateOption.WithinModeling, 0.625, False, False)
    
    cartesianCoordinateSystem1 = workPart.CoordinateSystems.CreateCoordinateSystem(xform1, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    sketchInPlaceBuilder1.Csystem = cartesianCoordinateSystem1
    
    origin2 = NXOpen.Point3d(0.0, 0.0, 0.0)
    normal2 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    plane2 = workPart.Planes.CreatePlane(origin2, normal2, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    plane2.SetMethod(NXOpen.PlaneTypes.MethodType.Coincident)
    
    geom1 = [NXOpen.NXObject.Null] * 1 
    geom1[0] = datumPlane1
    plane2.SetGeometry(geom1)
    
    plane2.SetFlip(False)
    
    plane2.SetExpression(None)
    
    plane2.SetAlternate(NXOpen.PlaneTypes.AlternateType.One)
    
    plane2.Evaluate()
    
    origin3 = NXOpen.Point3d(0.0, 0.0, 0.0)
    normal3 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    plane3 = workPart.Planes.CreatePlane(origin3, normal3, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    expression3 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression4 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    plane3.SynchronizeToPlane(plane2)
    
    plane3.SetMethod(NXOpen.PlaneTypes.MethodType.Coincident)
    
    geom2 = [NXOpen.NXObject.Null] * 1 
    geom2[0] = datumPlane1
    plane3.SetGeometry(geom2)
    
    plane3.SetAlternate(NXOpen.PlaneTypes.AlternateType.One)
    
    plane3.Evaluate()
    
    markId4 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Create Sketch")
    
    theSession.DeleteUndoMark(markId4, None)
    
    markId5 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Create Sketch")
    
    theSession.Preferences.Sketch.CreateInferredConstraints = True
    
    theSession.Preferences.Sketch.ContinuousAutoDimensioning = True
    
    theSession.Preferences.Sketch.DimensionLabel = NXOpen.Preferences.SketchPreferences.DimensionLabelType.Expression
    
    theSession.Preferences.Sketch.TextSizeFixed = True
    
    theSession.Preferences.Sketch.FixedTextSize = 3.0
    
    theSession.Preferences.Sketch.DisplayParenthesesOnReferenceDimensions = True
    
    theSession.Preferences.Sketch.DisplayReferenceGeometry = False
    
    theSession.Preferences.Sketch.DisplayShadedRegions = True
    
    theSession.Preferences.Sketch.ConstraintSymbolSize = 3.0
    
    theSession.Preferences.Sketch.DisplayObjectColor = False
    
    theSession.Preferences.Sketch.DisplayObjectName = True
    
    theSession.Preferences.Sketch.EditDimensionOnCreation = True
    
    nXObject1 = sketchInPlaceBuilder1.Commit()
    
    sketch1 = nXObject1
    feature1 = sketch1.Feature
    
    markId6 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "update")
    
    nErrs1 = theSession.UpdateManager.DoUpdate(markId6)
    
    sketch1.Activate(NXOpen.Sketch.ViewReorient.TrueValue)
    
    theSession.DeleteUndoMark(markId5, None)
    
    theSession.SetUndoMarkName(markId3, "Create Sketch")
    
    sketchInPlaceBuilder1.Destroy()
    
    sketchAlongPathBuilder1.Destroy()
    
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression2)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression1)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    plane1.DestroyPlane()
    
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression4)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression3)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    plane3.DestroyPlane()
    
    theSession.DeleteUndoMarksUpToMark(markId2, None, True)
    
    markId7 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Open Sketch")
    
    theSession.ActiveSketch.SetName("SKETCH_000")
    
    markId8 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Profile short list")
    
    # ----------------------------------------------
    #   Dialog Begin Profile
    # ----------------------------------------------
    # ----------------------------------------------
    #   Menu: Insert->Curve->Circle...
    # ----------------------------------------------
    theSession.DeleteUndoMark(markId8, "Curve")
    
    markId9 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Profile short list")
    
    markId10 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Curve")
    
    theSession.SetUndoMarkVisibility(markId10, "Curve", NXOpen.Session.MarkVisibility.Visible)
    
    nXMatrix1 = theSession.ActiveSketch.Orientation
    
    center1 = NXOpen.Point3d(0.0, 0.0, 0.0)
    arc1 = workPart.Curves.CreateArc(center1, nXMatrix1, 101.28216520960319, 0.0, ( 360.0 * math.pi/180.0 ))
    
    theSession.ActiveSketch.AddGeometry(arc1, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    geom1_1 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_1.Geometry = arc1
    geom1_1.PointType = NXOpen.Sketch.ConstraintPointType.ArcCenter
    geom1_1.SplineDefiningPointIndex = 0
    geom2_1 = NXOpen.Sketch.ConstraintGeometry()
    
    datumCsys2 = workPart.Features.FindObject("SKETCH(1:1B)")
    point2 = datumCsys2.FindObject("POINT 1")
    geom2_1.Geometry = point2
    geom2_1.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    geom2_1.SplineDefiningPointIndex = 0
    sketchGeometricConstraint1 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_1, geom2_1)
    
    dimObject1_1 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject1_1.Geometry = arc1
    dimObject1_1.AssocType = NXOpen.Sketch.AssocType.NotSet
    dimObject1_1.AssocValue = 0
    dimObject1_1.HelpPoint.X = 0.0
    dimObject1_1.HelpPoint.Y = 0.0
    dimObject1_1.HelpPoint.Z = 0.0
    dimObject1_1.View = NXOpen.NXObject.Null
    dimOrigin1 = NXOpen.Point3d(0.0, 3.0749999999999997, 0.0)
    sketchDimensionalConstraint1 = theSession.ActiveSketch.CreateDiameterDimension(dimObject1_1, dimOrigin1, NXOpen.Expression.Null, NXOpen.Sketch.DimensionOption.CreateAsAutomatic)
    
    dimension1 = sketchDimensionalConstraint1.AssociatedDimension
    
    expression5 = sketchDimensionalConstraint1.AssociatedExpression
    
    theSession.ActiveSketch.Update()
    
    # ----------------------------------------------
    #   Dialog Begin Circle
    # ----------------------------------------------
    # ----------------------------------------------
    #   Menu: Task->Finish Sketch
    # ----------------------------------------------
    theSession.Preferences.Sketch.SectionView = False
    
    markId11 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Deactivate Sketch")
    
    theSession.ActiveSketch.Deactivate(NXOpen.Sketch.ViewReorient.TrueValue, NXOpen.Sketch.UpdateLevel.Model)
    
    theSession.DeleteUndoMarksSetInTaskEnvironment()
    
    theSession.EndTaskEnvironment()
    
    # ----------------------------------------------
    #   Menu: Insert->Design Feature->Extrude...
    # ----------------------------------------------
    markId12 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    extrudeBuilder1 = workPart.Features.CreateExtrudeBuilder(NXOpen.Features.Feature.Null)
    
    section1 = workPart.Sections.CreateSection(0.0094999999999999998, 0.01, 0.5)
    
    extrudeBuilder1.Section = section1
    
    extrudeBuilder1.AllowSelfIntersectingSection(True)
    
    unit2 = extrudeBuilder1.Draft.FrontDraftAngle.Units
    
    expression6 = workPart.Expressions.CreateSystemExpressionWithUnits("2.00", unit2)
    
    extrudeBuilder1.DistanceTolerance = 0.01
    
    extrudeBuilder1.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    targetBodies1 = [NXOpen.Body.Null] * 1 
    targetBodies1[0] = NXOpen.Body.Null
    extrudeBuilder1.BooleanOperation.SetTargetBodies(targetBodies1)
    
    extrudeBuilder1.Limits.StartExtend.Value.SetFormula("0")
    
    extrudeBuilder1.Limits.EndExtend.Value.SetFormula("25")
    
    extrudeBuilder1.Offset.StartOffset.SetFormula("0")
    
    extrudeBuilder1.Offset.EndOffset.SetFormula("5")
    
    smartVolumeProfileBuilder1 = extrudeBuilder1.SmartVolumeProfile
    
    smartVolumeProfileBuilder1.OpenProfileSmartVolumeOption = False
    
    smartVolumeProfileBuilder1.CloseProfileRule = NXOpen.GeometricUtilities.SmartVolumeProfileBuilder.CloseProfileRuleType.Fci
    
    theSession.SetUndoMarkName(markId12, "Extrude Dialog")
    
    extrudeBuilder1.Limits.StartExtend.Value.SetFormula("0")
    
    extrudeBuilder1.Limits.EndExtend.Value.SetFormula("25")
    
    extrudeBuilder1.Draft.FrontDraftAngle.SetFormula("2")
    
    extrudeBuilder1.Draft.BackDraftAngle.SetFormula("2")
    
    extrudeBuilder1.Offset.StartOffset.SetFormula("0")
    
    extrudeBuilder1.Offset.EndOffset.SetFormula("5")
    
    section1.DistanceTolerance = 0.01
    
    section1.ChainingTolerance = 0.0094999999999999998
    
    section1.SetAllowedEntityTypes(NXOpen.Section.AllowTypes.OnlyCurves)
    
    markId13 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, None)
    
    curves1 = [NXOpen.ICurve.Null] * 1 
    curves1[0] = arc1
    seedPoint1 = NXOpen.Point3d(61.073719363754407, 19.844054343484853, 0.0)
    regionBoundaryRule1 = workPart.ScRuleFactory.CreateRuleRegionBoundary(sketch1, curves1, seedPoint1, 0.01)
    
    section1.AllowSelfIntersection(True)
    
    rules1 = [None] * 1 
    rules1[0] = regionBoundaryRule1
    helpPoint1 = NXOpen.Point3d(0.0, 0.0, 0.0)
    section1.AddToSection(rules1, NXOpen.NXObject.Null, NXOpen.NXObject.Null, NXOpen.NXObject.Null, helpPoint1, NXOpen.Section.Mode.Create, False)
    
    theSession.DeleteUndoMark(markId13, None)
    
    markId14 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "section mark")
    
    markId15 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, None)
    
    theSession.DeleteUndoMark(markId15, None)
    
    direction2 = workPart.Directions.CreateDirection(sketch1, NXOpen.Sense.Forward, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    extrudeBuilder1.Direction = direction2
    
    expression7 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    theSession.DeleteUndoMark(markId14, None)
    
    markId16 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Extrude")
    
    extrudeBuilder1.ParentFeatureInternal = False
    
    feature2 = extrudeBuilder1.CommitFeature()
    
    theSession.DeleteUndoMark(markId16, None)
    
    theSession.SetUndoMarkName(markId12, "Extrude")
    
    expression8 = extrudeBuilder1.Limits.StartExtend.Value
    expression9 = extrudeBuilder1.Limits.EndExtend.Value
    extrudeBuilder1.Destroy()
    
    workPart.Expressions.Delete(expression6)
    
    workPart.Expressions.Delete(expression7)
    
    markId17 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    extrudeBuilder2 = workPart.Features.CreateExtrudeBuilder(NXOpen.Features.Feature.Null)
    
    section2 = workPart.Sections.CreateSection(0.0094999999999999998, 0.01, 0.5)
    
    extrudeBuilder2.Section = section2
    
    extrudeBuilder2.AllowSelfIntersectingSection(True)
    
    expression10 = workPart.Expressions.CreateSystemExpressionWithUnits("2.00", unit2)
    
    extrudeBuilder2.DistanceTolerance = 0.01
    
    extrudeBuilder2.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    targetBodies2 = [NXOpen.Body.Null] * 1 
    targetBodies2[0] = NXOpen.Body.Null
    extrudeBuilder2.BooleanOperation.SetTargetBodies(targetBodies2)
    
    extrudeBuilder2.Limits.StartExtend.Value.SetFormula("0")
    
    extrudeBuilder2.Limits.EndExtend.Value.SetFormula("25")
    
    extrudeBuilder2.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    targetBodies3 = [NXOpen.Body.Null] * 1 
    targetBodies3[0] = NXOpen.Body.Null
    extrudeBuilder2.BooleanOperation.SetTargetBodies(targetBodies3)
    
    extrudeBuilder2.Draft.FrontDraftAngle.SetFormula("2")
    
    extrudeBuilder2.Draft.BackDraftAngle.SetFormula("2")
    
    extrudeBuilder2.Offset.StartOffset.SetFormula("0")
    
    extrudeBuilder2.Offset.EndOffset.SetFormula("5")
    
    smartVolumeProfileBuilder2 = extrudeBuilder2.SmartVolumeProfile
    
    smartVolumeProfileBuilder2.OpenProfileSmartVolumeOption = False
    
    smartVolumeProfileBuilder2.CloseProfileRule = NXOpen.GeometricUtilities.SmartVolumeProfileBuilder.CloseProfileRuleType.Fci
    
    theSession.SetUndoMarkName(markId17, "Extrude Dialog")
    
    section2.DistanceTolerance = 0.01
    
    section2.ChainingTolerance = 0.0094999999999999998
    
    # ----------------------------------------------
    #   Dialog Begin Extrude
    # ----------------------------------------------
    section2.SetAllowedEntityTypes(NXOpen.Section.AllowTypes.OnlyCurves)
    
    extrudeBuilder2.Destroy()
    
    section2.Destroy()
    
    workPart.Expressions.Delete(expression10)
    
    theSession.UndoToMark(markId17, None)
    
    theSession.DeleteUndoMark(markId17, None)
    
    # ----------------------------------------------
    #   Menu: Insert->Design Feature->Hole...
    # ----------------------------------------------
    markId18 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    holePackageBuilder1 = workPart.Features.CreateHolePackageBuilder(NXOpen.Features.HolePackage.Null)
    
    holePackageBuilder1.StartHoleData.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Subtract
    
    targetBodies4 = [NXOpen.Body.Null] * 1 
    targetBodies4[0] = NXOpen.Body.Null
    holePackageBuilder1.StartHoleData.BooleanOperation.SetTargetBodies(targetBodies4)
    
    holePackageBuilder1.MiddleHoleData.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Subtract
    
    targetBodies5 = []
    holePackageBuilder1.MiddleHoleData.BooleanOperation.SetTargetBodies(targetBodies5)
    
    holePackageBuilder1.EndHoleData.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Subtract
    
    targetBodies6 = [NXOpen.Body.Null] * 1 
    targetBodies6[0] = NXOpen.Body.Null
    holePackageBuilder1.EndHoleData.BooleanOperation.SetTargetBodies(targetBodies6)
    
    holePackageBuilder1.Tolerance = 0.01
    
    holePackageBuilder1.ScrewStandard = "ISO"
    
    holePackageBuilder1.ScrewClearanceHoleDiameter.SetFormula("1.7")
    
    holePackageBuilder1.ScrewClearanceStartChamferOffset.SetFormula("0.2")
    
    holePackageBuilder1.ScrewClearanceEndChamferOffset.SetFormula("0.2")
    
    holePackageBuilder1.MiddleHoleData.HoleDiameter.SetFormula("1.7")
    
    holePackageBuilder1.MiddleHoleData.StartChamferOffset.SetFormula("0.2")
    
    holePackageBuilder1.MiddleHoleData.EndChamferOffset.SetFormula("0.2")
    
    holePackageBuilder1.EndHoleData.HoleDiameter.SetFormula("1.7")
    
    holePackageBuilder1.EndHoleData.ScrewClearanceStartChamferOffset.SetFormula("0.2")
    
    holePackageBuilder1.EndHoleData.ScrewClearanceEndChamferOffset.SetFormula("0.2")
    
    holePackageBuilder1.StartHoleData.HoleDiameter.SetFormula("1.7")
    
    holePackageBuilder1.StartHoleData.StartChamferOffset.SetFormula("0.2")
    
    holePackageBuilder1.StartHoleData.EndChamferOffset.SetFormula("0.2")
    
    holePackageBuilder1.ThreadSize = "M1.0 x 0.25"
    
    holePackageBuilder1.EndHoleData.ThreadSize = "M1.0 x 0.25"
    
    holePackageBuilder1.ThreadStandard = "Metric Coarse"
    
    holePackageBuilder1.TapDrillDiameter.SetFormula("0.75")
    
    holePackageBuilder1.ThreadedReliefDepth.SetFormula("0.5")
    
    holePackageBuilder1.ThreadedReliefDiameter.SetFormula("1")
    
    holePackageBuilder1.ThreadedReliefChamferOffset.SetFormula("0.08")
    
    holePackageBuilder1.ThreadedStartChamferDiameter.SetFormula("1")
    
    holePackageBuilder1.ThreadedEndChamferDiameter.SetFormula("1")
    
    holePackageBuilder1.ThreadedHoleDepth.SetFormula("2")
    
    holePackageBuilder1.ThreadDepth.SetFormula("1.5")
    
    holePackageBuilder1.EndHoleData.TapDrillDiameter.SetFormula("0.75")
    
    holePackageBuilder1.EndHoleData.ThreadedStartChamferDiameter.SetFormula("1")
    
    holePackageBuilder1.EndHoleData.ThreadedEndChamferDiameter.SetFormula("1")
    
    holePackageBuilder1.EndHoleData.ThreadedReliefDepth.SetFormula("0.5")
    
    holePackageBuilder1.EndHoleData.ThreadedReliefDiameter.SetFormula("1")
    
    holePackageBuilder1.EndHoleData.ThreadedReliefChamferOffset.SetFormula("0.08")
    
    holePackageBuilder1.DrillSizeStandard = "ISO"
    
    holePackageBuilder1.DrillSizeHoleDiameter.SetFormula("0.35")
    
    holePackageBuilder1.DrillSizeStartChamferOffset.SetFormula("0.03")
    
    holePackageBuilder1.DrillSizeEndChamferOffset.SetFormula("0.03")
    
    holePackageBuilder1.GeneralTaperedHoleDepth.SetFormula("25")
    
    holePackageBuilder1.CounterboreDepthLimitOption = NXOpen.Features.HolePackageBuilder.CounterBoreDepthLimitOptions.Value
    
    holePackageBuilder1.CounterboreDepthLimitOption = NXOpen.Features.HolePackageBuilder.CounterBoreDepthLimitOptions.Value
    
    holePackageBuilder1.CounterboreDepthLimitOption = NXOpen.Features.HolePackageBuilder.CounterBoreDepthLimitOptions.Value
    
    holePackageBuilder1.NeckChamferEnabled = True
    
    holePackageBuilder1.ScrewClearanceStartChamferEnabled = True
    
    holePackageBuilder1.ScrewClearanceEndChamferEnabled = True
    
    holePackageBuilder1.StartHoleData.StartChamferEnabled = True
    
    holePackageBuilder1.StartHoleData.EndChamferEnabled = True
    
    holePackageBuilder1.MiddleHoleData.StartChamferEnabled = True
    
    holePackageBuilder1.MiddleHoleData.EndChamferEnabled = True
    
    holePackageBuilder1.EndHoleData.ScrewClearanceStartChamferEnabled = True
    
    holePackageBuilder1.EndHoleData.ScrewClearanceEndChamferEnabled = True
    
    holePackageBuilder1.EndHoleData.ThreadedStartChamferEnabled = True
    
    holePackageBuilder1.EndHoleData.ThreadedEndChamferEnabled = True
    
    holePackageBuilder1.ThreadSize = "M10 x 1.5"
    
    holePackageBuilder1.TapDrillDiameter.SetFormula("8.5")
    
    holePackageBuilder1.ThreadedReliefDepth.SetFormula("5")
    
    holePackageBuilder1.ThreadedReliefDiameter.SetFormula("10")
    
    holePackageBuilder1.ThreadedReliefChamferOffset.SetFormula("0.6")
    
    holePackageBuilder1.ThreadedStartChamferDiameter.SetFormula("10")
    
    holePackageBuilder1.ThreadedEndChamferDiameter.SetFormula("10")
    
    holePackageBuilder1.ThreadedHoleDepth.SetFormula("20")
    
    holePackageBuilder1.ThreadDepth.SetFormula("15")
    
    holePackageBuilder1.RadialEngageOption = "0.75"
    
    holePackageBuilder1.ThreadedStartChamferEnabled = True
    
    holePackageBuilder1.ThreadedEndChamferEnabled = True
    
    holePackageBuilder1.EndHoleData.ThreadSize = "M10 x 1.5"
    
    holePackageBuilder1.EndHoleData.TapDrillDiameter.SetFormula("8.5")
    
    holePackageBuilder1.EndHoleData.ThreadedStartChamferDiameter.SetFormula("10")
    
    holePackageBuilder1.EndHoleData.ThreadedEndChamferDiameter.SetFormula("10")
    
    holePackageBuilder1.EndHoleData.ThreadedReliefDepth.SetFormula("5")
    
    holePackageBuilder1.EndHoleData.ThreadedReliefDiameter.SetFormula("10")
    
    holePackageBuilder1.EndHoleData.ThreadedReliefChamferOffset.SetFormula("0.6")
    
    holePackageBuilder1.EndHoleData.RadialEngageOption = "0.75"
    
    holePackageBuilder1.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Subtract
    
    targetBodies7 = [NXOpen.Body.Null] * 1 
    body1 = workPart.Bodies.FindObject("EXTRUDE(2)")
    targetBodies7[0] = body1
    holePackageBuilder1.BooleanOperation.SetTargetBodies(targetBodies7)
    
    holePackageBuilder1.ScrewStandard = "ISO"
    
    holePackageBuilder1.ScrewClearanceHoleDiameter.SetFormula("11")
    
    holePackageBuilder1.ScrewClearanceStartChamferOffset.SetFormula("0.6")
    
    holePackageBuilder1.ScrewClearanceEndChamferOffset.SetFormula("0.6")
    
    holePackageBuilder1.MiddleHoleData.HoleDiameter.SetFormula("11")
    
    holePackageBuilder1.MiddleHoleData.StartChamferOffset.SetFormula("0.6")
    
    holePackageBuilder1.MiddleHoleData.EndChamferOffset.SetFormula("0.6")
    
    holePackageBuilder1.EndHoleData.HoleDiameter.SetFormula("11")
    
    holePackageBuilder1.EndHoleData.ScrewClearanceStartChamferOffset.SetFormula("0.6")
    
    holePackageBuilder1.EndHoleData.ScrewClearanceEndChamferOffset.SetFormula("0.6")
    
    holePackageBuilder1.StartHoleData.HoleDiameter.SetFormula("11")
    
    holePackageBuilder1.StartHoleData.StartChamferOffset.SetFormula("0.6")
    
    holePackageBuilder1.StartHoleData.EndChamferOffset.SetFormula("0.6")
    
    holePackageBuilder1.ThreadStandard = "Metric Coarse"
    
    holePackageBuilder1.DrillSizeStandard = "ISO"
    
    theSession.SetUndoMarkName(markId18, "Hole Dialog")
    
    expression11 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    holePackageBuilder1.HolePosition.DistanceTolerance = 0.01
    
    holePackageBuilder1.HolePosition.ChainingTolerance = 0.0094999999999999998
    
    holePackageBuilder1.HolePosition.SetAllowedEntityTypes(NXOpen.Section.AllowTypes.OnlyPoints)
    
    markId19 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "section mark")
    
    markId20 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, None)
    
    extrude1 = feature2
    edge1 = extrude1.FindObject("EDGE * 130 * 140 {(-50.6410826048016,87.7129280218088,25)(101.2821652096032,0,25)(-50.6410826048016,-87.7129280218088,25) EXTRUDE(2)}")
    point3 = workPart.Points.CreatePoint(edge1, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    xform2, nXObject2 = workPart.Xforms.CreateExtractXform(edge1, NXOpen.SmartObject.UpdateOption.WithinModeling, False)
    
    points1 = [NXOpen.Point.Null] * 1 
    points1[0] = point3
    curveDumbRule1 = workPart.ScRuleFactory.CreateRuleCurveDumbFromPoints(points1)
    
    holePackageBuilder1.HolePosition.AllowSelfIntersection(True)
    
    rules2 = [None] * 1 
    rules2[0] = curveDumbRule1
    helpPoint2 = NXOpen.Point3d(0.0, 0.0, 0.0)
    holePackageBuilder1.HolePosition.AddToSection(rules2, NXOpen.NXObject.Null, NXOpen.NXObject.Null, NXOpen.NXObject.Null, helpPoint2, NXOpen.Section.Mode.Create, False)
    
    theSession.DeleteUndoMark(markId19, None)
    
    scaleAboutPoint1 = NXOpen.Point3d(44.747656250000027, 49.62921875, 0.0)
    viewCenter1 = NXOpen.Point3d(-44.747656250000027, -49.62921875, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint1, viewCenter1)
    
    scaleAboutPoint2 = NXOpen.Point3d(35.79812500000002, 39.703374999999994, 0.0)
    viewCenter2 = NXOpen.Point3d(-35.79812500000002, -39.703374999999994, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint2, viewCenter2)
    
    scaleAboutPoint3 = NXOpen.Point3d(28.638500000000018, 31.762699999999999, 0.0)
    viewCenter3 = NXOpen.Point3d(-28.638500000000018, -31.762699999999999, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint3, viewCenter3)
    
    scaleAboutPoint4 = NXOpen.Point3d(22.91080000000003, 25.410160000000019, 0.0)
    viewCenter4 = NXOpen.Point3d(-22.91080000000002, -25.410159999999994, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint4, viewCenter4)
    
    scaleAboutPoint5 = NXOpen.Point3d(10.066866666666686, 23.778633333333342, 0.0)
    viewCenter5 = NXOpen.Point3d(-10.066866666666686, -23.778633333333342, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint5, viewCenter5)
    
    markId21 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Hole")
    
    holePackageBuilder1.ParentFeatureInternal = False
    
    holePackageBuilder1.StartHoleData.ScrewType = "General Screw Clearance"
    
    holePackageBuilder1.StartHoleData.ScrewSize = "M10"
    
    holePackageBuilder1.StartHoleData.FitOption = "Normal (H13)"
    
    holePackageBuilder1.MiddleHoleData.FitOption = "Normal (H13)"
    
    holePackageBuilder1.EndHoleData.FitOption = "Normal (H13)"
    
    nXObject3 = holePackageBuilder1.Commit()
    
    theSession.DeleteUndoMark(markId21, None)
    
    theSession.SetUndoMarkName(markId18, "Hole")
    
    expression12 = holePackageBuilder1.GeneralTipAngle
    expression13 = holePackageBuilder1.GeneralSimpleHoleDiameter
    expression14 = holePackageBuilder1.GeneralSimpleHoleDepth
    holePackageBuilder1.Destroy()
    
    workPart.Expressions.Delete(expression11)
    
    markId22 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    holePackageBuilder2 = workPart.Features.CreateHolePackageBuilder(NXOpen.Features.HolePackage.Null)
    
    holePackageBuilder2.StartHoleData.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Subtract
    
    targetBodies8 = [NXOpen.Body.Null] * 1 
    targetBodies8[0] = NXOpen.Body.Null
    holePackageBuilder2.StartHoleData.BooleanOperation.SetTargetBodies(targetBodies8)
    
    holePackageBuilder2.MiddleHoleData.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Subtract
    
    targetBodies9 = []
    holePackageBuilder2.MiddleHoleData.BooleanOperation.SetTargetBodies(targetBodies9)
    
    holePackageBuilder2.EndHoleData.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Subtract
    
    targetBodies10 = [NXOpen.Body.Null] * 1 
    targetBodies10[0] = NXOpen.Body.Null
    holePackageBuilder2.EndHoleData.BooleanOperation.SetTargetBodies(targetBodies10)
    
    holePackageBuilder2.Tolerance = 0.01
    
    holePackageBuilder2.ScrewStandard = "ISO"
    
    holePackageBuilder2.ScrewClearanceHoleDiameter.SetFormula("1.7")
    
    holePackageBuilder2.ScrewClearanceStartChamferOffset.SetFormula("0.2")
    
    holePackageBuilder2.ScrewClearanceEndChamferOffset.SetFormula("0.2")
    
    holePackageBuilder2.MiddleHoleData.HoleDiameter.SetFormula("1.7")
    
    holePackageBuilder2.MiddleHoleData.StartChamferOffset.SetFormula("0.2")
    
    holePackageBuilder2.MiddleHoleData.EndChamferOffset.SetFormula("0.2")
    
    holePackageBuilder2.EndHoleData.HoleDiameter.SetFormula("1.7")
    
    holePackageBuilder2.EndHoleData.ScrewClearanceStartChamferOffset.SetFormula("0.2")
    
    holePackageBuilder2.EndHoleData.ScrewClearanceEndChamferOffset.SetFormula("0.2")
    
    holePackageBuilder2.StartHoleData.HoleDiameter.SetFormula("1.7")
    
    holePackageBuilder2.StartHoleData.StartChamferOffset.SetFormula("0.2")
    
    holePackageBuilder2.StartHoleData.EndChamferOffset.SetFormula("0.2")
    
    holePackageBuilder2.ThreadSize = "M1.0 x 0.25"
    
    holePackageBuilder2.EndHoleData.ThreadSize = "M1.0 x 0.25"
    
    holePackageBuilder2.ThreadStandard = "Metric Coarse"
    
    holePackageBuilder2.TapDrillDiameter.SetFormula("0.75")
    
    holePackageBuilder2.ThreadedReliefDepth.SetFormula("0.5")
    
    holePackageBuilder2.ThreadedReliefDiameter.SetFormula("1")
    
    holePackageBuilder2.ThreadedReliefChamferOffset.SetFormula("0.08")
    
    holePackageBuilder2.ThreadedStartChamferDiameter.SetFormula("1")
    
    holePackageBuilder2.ThreadedEndChamferDiameter.SetFormula("1")
    
    holePackageBuilder2.ThreadedHoleDepth.SetFormula("2")
    
    holePackageBuilder2.ThreadDepth.SetFormula("1.5")
    
    holePackageBuilder2.EndHoleData.TapDrillDiameter.SetFormula("0.75")
    
    holePackageBuilder2.EndHoleData.ThreadedStartChamferDiameter.SetFormula("1")
    
    holePackageBuilder2.EndHoleData.ThreadedEndChamferDiameter.SetFormula("1")
    
    holePackageBuilder2.EndHoleData.ThreadedReliefDepth.SetFormula("0.5")
    
    holePackageBuilder2.EndHoleData.ThreadedReliefDiameter.SetFormula("1")
    
    holePackageBuilder2.EndHoleData.ThreadedReliefChamferOffset.SetFormula("0.08")
    
    holePackageBuilder2.DrillSizeStandard = "ISO"
    
    holePackageBuilder2.DrillSizeHoleDiameter.SetFormula("0.35")
    
    holePackageBuilder2.DrillSizeStartChamferOffset.SetFormula("0.03")
    
    holePackageBuilder2.DrillSizeEndChamferOffset.SetFormula("0.03")
    
    holePackageBuilder2.CounterboreDepthLimitOption = NXOpen.Features.HolePackageBuilder.CounterBoreDepthLimitOptions.Value
    
    holePackageBuilder2.CounterboreDepthLimitOption = NXOpen.Features.HolePackageBuilder.CounterBoreDepthLimitOptions.Value
    
    holePackageBuilder2.CounterboreDepthLimitOption = NXOpen.Features.HolePackageBuilder.CounterBoreDepthLimitOptions.Value
    
    holePackageBuilder2.ThreadSize = "M10 x 1.5"
    
    holePackageBuilder2.TapDrillDiameter.SetFormula("8.5")
    
    holePackageBuilder2.ThreadedReliefDepth.SetFormula("5")
    
    holePackageBuilder2.ThreadedReliefDiameter.SetFormula("10")
    
    holePackageBuilder2.ThreadedReliefChamferOffset.SetFormula("0.6")
    
    holePackageBuilder2.ThreadedStartChamferDiameter.SetFormula("10")
    
    holePackageBuilder2.ThreadedEndChamferDiameter.SetFormula("10")
    
    holePackageBuilder2.ThreadedHoleDepth.SetFormula("20")
    
    holePackageBuilder2.ThreadDepth.SetFormula("15")
    
    holePackageBuilder2.RadialEngageOption = "0.75"
    
    holePackageBuilder2.StartHoleData.CounterboreDiameter.SetFormula("38")
    
    holePackageBuilder2.StartHoleData.CounterboreDepth.SetFormula("25")
    
    holePackageBuilder2.StartHoleData.CountersinkDiameter.SetFormula("50")
    
    holePackageBuilder2.StartHoleData.CountersinkAngle.SetFormula("90")
    
    holePackageBuilder2.StartHoleData.HoleDiameter.SetFormula("11")
    
    holePackageBuilder2.StartHoleData.ReliefDepth.SetFormula("1.2")
    
    holePackageBuilder2.StartHoleData.StartChamferEnabled = True
    
    holePackageBuilder2.StartHoleData.StartChamferOffset.SetFormula("0.6")
    
    holePackageBuilder2.StartHoleData.StartChamferAngle.SetFormula("45")
    
    holePackageBuilder2.StartHoleData.NeckChamferOffset.SetFormula("0.6")
    
    holePackageBuilder2.StartHoleData.NeckChamferAngle.SetFormula("45")
    
    holePackageBuilder2.StartHoleData.EndChamferEnabled = True
    
    holePackageBuilder2.StartHoleData.EndChamferOffset.SetFormula("0.6")
    
    holePackageBuilder2.StartHoleData.EndChamferAngle.SetFormula("45")
    
    holePackageBuilder2.StartHoleData.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Subtract
    
    targetBodies11 = [NXOpen.Body.Null] * 1 
    targetBodies11[0] = NXOpen.Body.Null
    holePackageBuilder2.StartHoleData.BooleanOperation.SetTargetBodies(targetBodies11)
    
    holePackageBuilder2.MiddleHoleData.HoleDiameter.SetFormula("11")
    
    holePackageBuilder2.MiddleHoleData.StartChamferEnabled = True
    
    holePackageBuilder2.MiddleHoleData.StartChamferOffset.SetFormula("0.6")
    
    holePackageBuilder2.MiddleHoleData.StartChamferAngle.SetFormula("45")
    
    holePackageBuilder2.MiddleHoleData.EndChamferEnabled = True
    
    holePackageBuilder2.MiddleHoleData.EndChamferOffset.SetFormula("0.6")
    
    holePackageBuilder2.MiddleHoleData.EndChamferAngle.SetFormula("45")
    
    holePackageBuilder2.MiddleHoleData.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Subtract
    
    targetBodies12 = []
    holePackageBuilder2.MiddleHoleData.BooleanOperation.SetTargetBodies(targetBodies12)
    
    holePackageBuilder2.EndHoleData.ThreadSize = "M10 x 1.5"
    
    holePackageBuilder2.EndHoleData.TapDrillDiameter.SetFormula("8.5")
    
    holePackageBuilder2.EndHoleData.ThreadedStartChamferDiameter.SetFormula("10")
    
    holePackageBuilder2.EndHoleData.ThreadedEndChamferDiameter.SetFormula("10")
    
    holePackageBuilder2.EndHoleData.ThreadedReliefDepth.SetFormula("5")
    
    holePackageBuilder2.EndHoleData.ThreadedReliefDiameter.SetFormula("10")
    
    holePackageBuilder2.EndHoleData.ThreadedReliefChamferOffset.SetFormula("0.6")
    
    holePackageBuilder2.EndHoleData.RadialEngageOption = "0.75"
    
    holePackageBuilder2.EndHoleData.TapDrillDiameter.SetFormula("8.5")
    
    holePackageBuilder2.EndHoleData.ThreadLengthOption = NXOpen.GeometricUtilities.EndHoleData.ThreadLengthOptions.Custom
    
    holePackageBuilder2.EndHoleData.ThreadDepth.SetFormula("25")
    
    holePackageBuilder2.EndHoleData.HoleDiameter.SetFormula("11")
    
    holePackageBuilder2.EndHoleData.HoleDepth.SetFormula("50")
    
    holePackageBuilder2.EndHoleData.TipAngle.SetFormula("118")
    
    holePackageBuilder2.EndHoleData.ThreadedReliefDiameter.SetFormula("10")
    
    holePackageBuilder2.EndHoleData.ThreadedReliefAngle.SetFormula("118")
    
    holePackageBuilder2.EndHoleData.ThreadedReliefDepth.SetFormula("5")
    
    holePackageBuilder2.EndHoleData.ThreadedReliefChamferOffset.SetFormula("0.6")
    
    holePackageBuilder2.EndHoleData.ThreadedReliefChamferAngle.SetFormula("45")
    
    holePackageBuilder2.EndHoleData.ScrewClearanceStartChamferEnabled = True
    
    holePackageBuilder2.EndHoleData.ScrewClearanceStartChamferOffset.SetFormula("0.6")
    
    holePackageBuilder2.EndHoleData.ScrewClearanceStartChamferAngle.SetFormula("45")
    
    holePackageBuilder2.EndHoleData.ThreadedStartChamferEnabled = True
    
    holePackageBuilder2.EndHoleData.ThreadedStartChamferDiameter.SetFormula("10")
    
    holePackageBuilder2.EndHoleData.ThreadedStartChamferAngle.SetFormula("45")
    
    holePackageBuilder2.EndHoleData.ScrewClearanceEndChamferEnabled = True
    
    holePackageBuilder2.EndHoleData.ScrewClearanceEndChamferOffset.SetFormula("0.6")
    
    holePackageBuilder2.EndHoleData.ScrewClearanceEndChamferAngle.SetFormula("45")
    
    holePackageBuilder2.EndHoleData.ThreadedEndChamferEnabled = True
    
    holePackageBuilder2.EndHoleData.ThreadedEndChamferDiameter.SetFormula("10")
    
    holePackageBuilder2.EndHoleData.ThreadedEndChamferAngle.SetFormula("45")
    
    holePackageBuilder2.EndHoleData.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Subtract
    
    targetBodies13 = [NXOpen.Body.Null] * 1 
    targetBodies13[0] = NXOpen.Body.Null
    holePackageBuilder2.EndHoleData.BooleanOperation.SetTargetBodies(targetBodies13)
    
    holePackageBuilder2.TapDrillDiameter.SetFormula("8.5")
    
    holePackageBuilder2.ThreadLengthOption = NXOpen.Features.HolePackageBuilder.ThreadLengthOptions.Custom
    
    holePackageBuilder2.ThreadDepth.SetFormula("15")
    
    holePackageBuilder2.GeneralCounterboreDiameter.SetFormula("38")
    
    holePackageBuilder2.GeneralDistanceFromSelected.SetFormula("5")
    
    holePackageBuilder2.ScrewClearanceDistanceFromSelected.SetFormula("5")
    
    holePackageBuilder2.GeneralCounterboreDepth.SetFormula("25")
    
    holePackageBuilder2.GeneralCountersinkDiameter.SetFormula("50")
    
    holePackageBuilder2.GeneralCountersinkAngle.SetFormula("90")
    
    holePackageBuilder2.GeneralSimpleHoleDiameter.SetFormula("25")
    
    holePackageBuilder2.GeneralCounterboreHoleDiameter.SetFormula("25")
    
    holePackageBuilder2.GeneralCountersinkHoleDiameter.SetFormula("25")
    
    holePackageBuilder2.GeneralTaperedHoleDiameter.SetFormula("25")
    
    holePackageBuilder2.DrillSizeHoleDiameter.SetFormula("0.35")
    
    holePackageBuilder2.ScrewClearanceCounterboreDiameter.SetFormula("18")
    
    holePackageBuilder2.ScrewClearanceCounterboreDepth.SetFormula("10.8")
    
    holePackageBuilder2.ScrewClearanceCountersinkDiameter.SetFormula("22.73")
    
    holePackageBuilder2.ScrewClearanceCountersinkAngle.SetFormula("90")
    
    holePackageBuilder2.ScrewClearanceHoleDiameter.SetFormula("11")
    
    holePackageBuilder2.GeneralTaperAngle.SetFormula("10")
    
    holePackageBuilder2.PitchMultiplier.SetFormula("1")
    
    holePackageBuilder2.GeneralSimpleHoleDepth.SetFormula("50")
    
    holePackageBuilder2.GeneralCounterboreHoleDepth.SetFormula("50")
    
    holePackageBuilder2.GeneralCountersinkHoleDepth.SetFormula("50")
    
    holePackageBuilder2.GeneralTaperedHoleDepth.SetFormula("25")
    
    holePackageBuilder2.GeneralTipAngle.SetFormula("118")
    
    holePackageBuilder2.DrillSizeHoleDepth.SetFormula("50")
    
    holePackageBuilder2.DrillSizeTipAngle.SetFormula("118")
    
    holePackageBuilder2.ScrewClearanceHoleDepth.SetFormula("50")
    
    holePackageBuilder2.ScrewClearanceTipAngle.SetFormula("118")
    
    holePackageBuilder2.ThreadedHoleDepth.SetFormula("20")
    
    holePackageBuilder2.ThreadedTipAngle.SetFormula("118")
    
    holePackageBuilder2.ScrewClearanceReliefDepth.SetFormula("1.2")
    
    holePackageBuilder2.ThreadedReliefDiameter.SetFormula("10")
    
    holePackageBuilder2.ThreadedReliefAngle.SetFormula("118")
    
    holePackageBuilder2.ThreadedReliefDepth.SetFormula("5")
    
    holePackageBuilder2.ThreadedReliefChamferOffset.SetFormula("0.6")
    
    holePackageBuilder2.ThreadedReliefChamferAngle.SetFormula("45")
    
    holePackageBuilder2.DrillSizeStartChamferOffset.SetFormula("0.03")
    
    holePackageBuilder2.DrillSizeStartChamferAngle.SetFormula("45")
    
    holePackageBuilder2.ScrewClearanceStartChamferEnabled = True
    
    holePackageBuilder2.ScrewClearanceStartChamferOffset.SetFormula("0.6")
    
    holePackageBuilder2.ScrewClearanceStartChamferAngle.SetFormula("45")
    
    holePackageBuilder2.ThreadedStartChamferEnabled = True
    
    holePackageBuilder2.ThreadedStartChamferDiameter.SetFormula("10")
    
    holePackageBuilder2.ThreadedStartChamferAngle.SetFormula("45")
    
    holePackageBuilder2.DrillSizeEndChamferOffset.SetFormula("0.03")
    
    holePackageBuilder2.DrillSizeEndChamferAngle.SetFormula("45")
    
    holePackageBuilder2.ScrewClearanceEndChamferEnabled = True
    
    holePackageBuilder2.ScrewClearanceEndChamferOffset.SetFormula("0.6")
    
    holePackageBuilder2.ScrewClearanceEndChamferAngle.SetFormula("45")
    
    holePackageBuilder2.ThreadedEndChamferEnabled = True
    
    holePackageBuilder2.ThreadedEndChamferDiameter.SetFormula("10")
    
    holePackageBuilder2.ThreadedEndChamferAngle.SetFormula("45")
    
    holePackageBuilder2.NeckChamferEnabled = True
    
    holePackageBuilder2.ScrewClearanceNeckChamferOffset.SetFormula("0.6")
    
    holePackageBuilder2.ScrewClearanceNeckChamferAngle.SetFormula("45")
    
    holePackageBuilder2.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Subtract
    
    targetBodies14 = [NXOpen.Body.Null] * 1 
    targetBodies14[0] = body1
    holePackageBuilder2.BooleanOperation.SetTargetBodies(targetBodies14)
    
    holePackageBuilder2.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Subtract
    
    targetBodies15 = [NXOpen.Body.Null] * 1 
    targetBodies15[0] = body1
    holePackageBuilder2.BooleanOperation.SetTargetBodies(targetBodies15)
    
    holePackageBuilder2.ScrewStandard = "ISO"
    
    holePackageBuilder2.ThreadStandard = "Metric Coarse"
    
    holePackageBuilder2.DrillSizeStandard = "ISO"
    
    theSession.SetUndoMarkName(markId22, "Hole Dialog")
    
    expression15 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    holePackageBuilder2.HolePosition.DistanceTolerance = 0.01
    
    holePackageBuilder2.HolePosition.ChainingTolerance = 0.0094999999999999998
    
    # ----------------------------------------------
    #   Dialog Begin Hole
    # ----------------------------------------------
    holePackageBuilder2.HolePosition.SetAllowedEntityTypes(NXOpen.Section.AllowTypes.OnlyPoints)
    
    rotMatrix2 = NXOpen.Matrix3x3()
    
    rotMatrix2.Xx = 0.80149667269343927
    rotMatrix2.Xy = 0.59752241705765374
    rotMatrix2.Xz = 0.023875610461910259
    rotMatrix2.Yx = -0.17700932849552195
    rotMatrix2.Yy = 0.19891930078027553
    rotMatrix2.Yz = 0.96389771729299989
    rotMatrix2.Zx = 0.57120117409448234
    rotMatrix2.Zy = -0.77678701900242109
    rotMatrix2.Zz = 0.26520019951429297
    translation2 = NXOpen.Point3d(-13.890884714107205, -12.38489295555933, 1.3777378654495189)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix2, translation2, 1.2195121951219514)
    
    holePackageBuilder2.Destroy()
    
    workPart.Expressions.Delete(expression15)
    
    theSession.UndoToMark(markId22, None)
    
    theSession.DeleteUndoMark(markId22, None)
    
    markId23 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Edit Feature Parameters")
    
    markId24 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
    holePackage1 = nXObject3
    holePackageBuilder3 = workPart.Features.CreateHolePackageBuilder(holePackage1)
    
    holePackageBuilder3.StartHoleData.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Subtract
    
    targetBodies16 = [NXOpen.Body.Null] * 1 
    targetBodies16[0] = NXOpen.Body.Null
    holePackageBuilder3.StartHoleData.BooleanOperation.SetTargetBodies(targetBodies16)
    
    holePackageBuilder3.MiddleHoleData.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Subtract
    
    targetBodies17 = []
    holePackageBuilder3.MiddleHoleData.BooleanOperation.SetTargetBodies(targetBodies17)
    
    holePackageBuilder3.EndHoleData.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Subtract
    
    targetBodies18 = [NXOpen.Body.Null] * 1 
    targetBodies18[0] = NXOpen.Body.Null
    holePackageBuilder3.EndHoleData.BooleanOperation.SetTargetBodies(targetBodies18)
    
    targetBodies19 = [NXOpen.Body.Null] * 1 
    targetBodies19[0] = body1
    holePackageBuilder3.BooleanOperation.SetTargetBodies(targetBodies19)
    
    holePackageBuilder3.HolePosition.PrepareMappingData()
    
    theSession.SetUndoMarkName(markId24, "Hole Dialog")
    
    holePackageBuilder3.HolePosition.DistanceTolerance = 0.01
    
    holePackageBuilder3.HolePosition.ChainingTolerance = 0.0094999999999999998
    
    # ----------------------------------------------
    #   Dialog Begin Hole
    # ----------------------------------------------
    holePackageBuilder3.DrillSizeHoleDiameter.SetFormula("100")
    
    holePackageBuilder3.DrillSizeHoleDiameter.SetFormula("100")
    
    holePackageBuilder3.DrillSizeHoleDiameter.SetFormula("100")
    
    holePackageBuilder3.DrillSizeHoleDiameter.SetFormula("100")
    
    holePackageBuilder3.DrillSizeHoleDiameter.SetFormula("100")
    
    holePackageBuilder3.DrillSizeHoleDiameter.SetFormula("100")
    
    markId25 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Hole")
    
    theSession.DeleteUndoMark(markId25, None)
    
    markId26 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Hole")
    
    holePackageBuilder3.StartHoleData.ScrewType = "General Screw Clearance"
    
    holePackageBuilder3.StartHoleData.ScrewSize = "M1.6"
    
    holePackageBuilder3.StartHoleData.FitOption = "Close (H12)"
    
    holePackageBuilder3.MiddleHoleData.FitOption = "Close (H12)"
    
    holePackageBuilder3.EndHoleData.FitOption = "Close (H12)"
    
    nXObject4 = holePackageBuilder3.Commit()
    
    theSession.DeleteUndoMark(markId26, None)
    
    theSession.SetUndoMarkName(markId24, "Hole")
    
    holePackageBuilder3.HolePosition.CleanMappingData()
    
    expression16 = holePackageBuilder3.DrillSizeTipAngle
    expression17 = holePackageBuilder3.DrillSizeHoleDepth
    expression18 = holePackageBuilder3.DrillSizeHoleDiameter
    holePackageBuilder3.Destroy()
    
    theSession.DeleteUndoMark(markId24, None)
    
    theSession.Preferences.Modeling.UpdatePending = False
    
    nErrs2 = theSession.UpdateManager.DoUpdate(markId23)
    
    theSession.Preferences.Modeling.UpdatePending = False
    
    rotMatrix3 = NXOpen.Matrix3x3()
    
    rotMatrix3.Xx = 0.77381885803120309
    rotMatrix3.Xy = 0.63245084966493637
    rotMatrix3.Xz = 0.034789333327738564
    rotMatrix3.Yx = -0.38592937371872948
    rotMatrix3.Yy = 0.42721753882385094
    rotMatrix3.Yz = 0.81764521219314112
    rotMatrix3.Zx = 0.50225779581441976
    rotMatrix3.Zy = -0.64613550999724079
    rotMatrix3.Zz = 0.57467034834264041
    translation3 = NXOpen.Point3d(-14.027306249930056, -10.556736641811097, -2.490638994904824)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix3, translation3, 1.219512195121951)
    
    # ----------------------------------------------
    #   Menu: File->Save
    # ----------------------------------------------
    markId27 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    theSession.SetUndoMarkName(markId27, "Name Parts Dialog")
    
    theSession.UndoToMark(markId27, None)
    
    theSession.DeleteUndoMark(markId27, None)
    
    rotMatrix4 = NXOpen.Matrix3x3()
    
    rotMatrix4.Xx = 0.77381885803120309
    rotMatrix4.Xy = 0.63245084966493637
    rotMatrix4.Xz = 0.034789333327738564
    rotMatrix4.Yx = -0.2636968802589032
    rotMatrix4.Yy = 0.27172804473814732
    rotMatrix4.Yz = 0.92554190885367893
    rotMatrix4.Zx = 0.57590652913212559
    rotMatrix4.Zy = -0.7253756216339825
    rotMatrix4.Zz = 0.37704360124806102
    translation4 = NXOpen.Point3d(-14.027306249930056, -11.905445350067819, -0.020304656222581485)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix4, translation4, 1.219512195121951)
    
    # ----------------------------------------------
    #   Menu: Insert->Detail Feature->Edge Blend...
    # ----------------------------------------------
    markId28 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    edgeBlendBuilder1 = workPart.Features.CreateEdgeBlendBuilder(NXOpen.Features.Feature.Null)
    
    expression19 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression20 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    blendLimitsData1 = edgeBlendBuilder1.LimitsListData
    
    origin4 = NXOpen.Point3d(0.0, 0.0, 0.0)
    normal4 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    plane4 = workPart.Planes.CreatePlane(origin4, normal4, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    facePlaneSelectionBuilder1 = workPart.FacePlaneSelectionBuilderData.Create()
    
    expression21 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression22 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    theSession.SetUndoMarkName(markId28, "Edge Blend Dialog")
    
    scCollector1 = workPart.ScCollectors.CreateCollector()
    
    seedEdges1 = [NXOpen.Edge.Null] * 1 
    edge2 = nXObject2
    seedEdges1[0] = edge2
    edgeMultipleSeedTangentRule1 = workPart.ScRuleFactory.CreateRuleEdgeMultipleSeedTangent(seedEdges1, 0.5, True)
    
    rules3 = [None] * 1 
    rules3[0] = edgeMultipleSeedTangentRule1
    scCollector1.ReplaceRules(rules3, False)
    
    scCollector1.AddEvaluationFilter(NXOpen.ScEvaluationFiltertype.LaminarEdge)
    
    markId29 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Edge Blend")
    
    edgeBlendBuilder1.Tolerance = 0.01
    
    edgeBlendBuilder1.AllInstancesOption = False
    
    edgeBlendBuilder1.RemoveSelfIntersection = True
    
    edgeBlendBuilder1.PatchComplexGeometryAreas = True
    
    edgeBlendBuilder1.LimitFailingAreas = True
    
    edgeBlendBuilder1.ConvexConcaveY = False
    
    edgeBlendBuilder1.RollOverSmoothEdge = True
    
    edgeBlendBuilder1.RollOntoEdge = True
    
    edgeBlendBuilder1.MoveSharpEdge = True
    
    edgeBlendBuilder1.TrimmingOption = False
    
    edgeBlendBuilder1.OverlapOption = NXOpen.Features.EdgeBlendBuilder.Overlap.AnyConvexityRollOver
    
    edgeBlendBuilder1.BlendOrder = NXOpen.Features.EdgeBlendBuilder.OrderOfBlending.ConvexFirst
    
    edgeBlendBuilder1.SetbackOption = NXOpen.Features.EdgeBlendBuilder.Setback.SeparateFromCorner
    
    edgeBlendBuilder1.BlendFaceContinuity = NXOpen.Features.EdgeBlendBuilder.FaceContinuity.Tangent
    
    csIndex1 = edgeBlendBuilder1.AddChainset(scCollector1, "10")
    
    feature3 = edgeBlendBuilder1.CommitFeature()
    
    theSession.DeleteUndoMark(markId29, None)
    
    theSession.SetUndoMarkName(markId28, "Edge Blend")
    
    workPart.FacePlaneSelectionBuilderData.Destroy(facePlaneSelectionBuilder1)
    
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression22)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression21)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    edgeBlendBuilder1.Destroy()
    
    workPart.Expressions.Delete(expression19)
    
    workPart.Expressions.Delete(expression20)
    
    markId30 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    edgeBlendBuilder2 = workPart.Features.CreateEdgeBlendBuilder(NXOpen.Features.Feature.Null)
    
    expression23 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression24 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    blendLimitsData2 = edgeBlendBuilder2.LimitsListData
    
    origin5 = NXOpen.Point3d(0.0, 0.0, 0.0)
    normal5 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    plane5 = workPart.Planes.CreatePlane(origin5, normal5, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    facePlaneSelectionBuilder2 = workPart.FacePlaneSelectionBuilderData.Create()
    
    expression25 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression26 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    theSession.SetUndoMarkName(markId30, "Edge Blend Dialog")
    
    # ----------------------------------------------
    #   Dialog Begin Edge Blend
    # ----------------------------------------------
    workPart.FacePlaneSelectionBuilderData.Destroy(facePlaneSelectionBuilder2)
    
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression26)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression25)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    edgeBlendBuilder2.Destroy()
    
    workPart.Expressions.Delete(expression23)
    
    workPart.Expressions.Delete(expression24)
    
    theSession.UndoToMark(markId30, None)
    
    theSession.DeleteUndoMark(markId30, None)
    
    # ----------------------------------------------
    #   Menu: Insert->Detail Feature->Edge Blend...
    # ----------------------------------------------
    markId31 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    edgeBlendBuilder3 = workPart.Features.CreateEdgeBlendBuilder(NXOpen.Features.Feature.Null)
    
    expression27 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression28 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    blendLimitsData3 = edgeBlendBuilder3.LimitsListData
    
    origin6 = NXOpen.Point3d(0.0, 0.0, 0.0)
    normal6 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    plane6 = workPart.Planes.CreatePlane(origin6, normal6, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    facePlaneSelectionBuilder3 = workPart.FacePlaneSelectionBuilderData.Create()
    
    expression29 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression30 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    theSession.SetUndoMarkName(markId31, "Edge Blend Dialog")
    
    scCollector2 = workPart.ScCollectors.CreateCollector()
    
    seedEdges2 = [NXOpen.Edge.Null] * 1 
    edge3 = extrude1.FindObject("EDGE * 120 * 140 {(-50.6410826048016,87.7129280218088,0)(101.2821652096032,0,0)(-50.6410826048016,-87.7129280218088,0) EXTRUDE(2)}")
    seedEdges2[0] = edge3
    edgeMultipleSeedTangentRule2 = workPart.ScRuleFactory.CreateRuleEdgeMultipleSeedTangent(seedEdges2, 0.5, True)
    
    rules4 = [None] * 1 
    rules4[0] = edgeMultipleSeedTangentRule2
    scCollector2.ReplaceRules(rules4, False)
    
    scCollector2.AddEvaluationFilter(NXOpen.ScEvaluationFiltertype.LaminarEdge)
    
    markId32 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Edge Blend")
    
    edgeBlendBuilder3.Tolerance = 0.01
    
    edgeBlendBuilder3.AllInstancesOption = False
    
    edgeBlendBuilder3.RemoveSelfIntersection = True
    
    edgeBlendBuilder3.PatchComplexGeometryAreas = True
    
    edgeBlendBuilder3.LimitFailingAreas = True
    
    edgeBlendBuilder3.ConvexConcaveY = False
    
    edgeBlendBuilder3.RollOverSmoothEdge = True
    
    edgeBlendBuilder3.RollOntoEdge = True
    
    edgeBlendBuilder3.MoveSharpEdge = True
    
    edgeBlendBuilder3.TrimmingOption = False
    
    edgeBlendBuilder3.OverlapOption = NXOpen.Features.EdgeBlendBuilder.Overlap.AnyConvexityRollOver
    
    edgeBlendBuilder3.BlendOrder = NXOpen.Features.EdgeBlendBuilder.OrderOfBlending.ConvexFirst
    
    edgeBlendBuilder3.SetbackOption = NXOpen.Features.EdgeBlendBuilder.Setback.SeparateFromCorner
    
    edgeBlendBuilder3.BlendFaceContinuity = NXOpen.Features.EdgeBlendBuilder.FaceContinuity.Tangent
    
    csIndex2 = edgeBlendBuilder3.AddChainset(scCollector2, "10")
    
    feature4 = edgeBlendBuilder3.CommitFeature()
    
    theSession.DeleteUndoMark(markId32, None)
    
    theSession.SetUndoMarkName(markId31, "Edge Blend")
    
    workPart.FacePlaneSelectionBuilderData.Destroy(facePlaneSelectionBuilder3)
    
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression30)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression29)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    edgeBlendBuilder3.Destroy()
    
    workPart.Expressions.Delete(expression27)
    
    workPart.Expressions.Delete(expression28)
    
    markId33 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    edgeBlendBuilder4 = workPart.Features.CreateEdgeBlendBuilder(NXOpen.Features.Feature.Null)
    
    expression31 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression32 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    blendLimitsData4 = edgeBlendBuilder4.LimitsListData
    
    origin7 = NXOpen.Point3d(0.0, 0.0, 0.0)
    normal7 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    plane7 = workPart.Planes.CreatePlane(origin7, normal7, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    facePlaneSelectionBuilder4 = workPart.FacePlaneSelectionBuilderData.Create()
    
    expression33 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression34 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    theSession.SetUndoMarkName(markId33, "Edge Blend Dialog")
    
    # ----------------------------------------------
    #   Dialog Begin Edge Blend
    # ----------------------------------------------
    workPart.FacePlaneSelectionBuilderData.Destroy(facePlaneSelectionBuilder4)
    
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression34)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression33)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    edgeBlendBuilder4.Destroy()
    
    workPart.Expressions.Delete(expression31)
    
    workPart.Expressions.Delete(expression32)
    
    theSession.UndoToMark(markId33, None)
    
    theSession.DeleteUndoMark(markId33, None)
    
    # ----------------------------------------------
    #   Menu: Insert->Detail Feature->Edge Blend...
    # ----------------------------------------------
    markId34 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    edgeBlendBuilder5 = workPart.Features.CreateEdgeBlendBuilder(NXOpen.Features.Feature.Null)
    
    expression35 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression36 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    blendLimitsData5 = edgeBlendBuilder5.LimitsListData
    
    origin8 = NXOpen.Point3d(0.0, 0.0, 0.0)
    normal8 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    plane8 = workPart.Planes.CreatePlane(origin8, normal8, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    facePlaneSelectionBuilder5 = workPart.FacePlaneSelectionBuilderData.Create()
    
    expression37 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression38 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    theSession.SetUndoMarkName(markId34, "Edge Blend Dialog")
    
    scCollector3 = workPart.ScCollectors.CreateCollector()
    
    seedEdges3 = [NXOpen.Edge.Null] * 1 
    edge4 = extrude1.FindObject("EDGE * 130 SIMPLE HOLE(3:1A) 3 {(25,43.3012701892219,25)(-50,0,25)(25,-43.3012701892219,25) EXTRUDE(2)}")
    seedEdges3[0] = edge4
    edgeMultipleSeedTangentRule3 = workPart.ScRuleFactory.CreateRuleEdgeMultipleSeedTangent(seedEdges3, 0.5, True)
    
    rules5 = [None] * 1 
    rules5[0] = edgeMultipleSeedTangentRule3
    scCollector3.ReplaceRules(rules5, False)
    
    scCollector3.AddEvaluationFilter(NXOpen.ScEvaluationFiltertype.LaminarEdge)
    
    seedEdges4 = [NXOpen.Edge.Null] * 2 
    seedEdges4[0] = edge4
    edge5 = extrude1.FindObject("EDGE * 120 SIMPLE HOLE(3:1A) 3 {(-25,43.3012701892219,0)(50,0,0)(-25,-43.3012701892219,0) EXTRUDE(2)}")
    seedEdges4[1] = edge5
    edgeMultipleSeedTangentRule4 = workPart.ScRuleFactory.CreateRuleEdgeMultipleSeedTangent(seedEdges4, 0.5, True)
    
    rules6 = [None] * 1 
    rules6[0] = edgeMultipleSeedTangentRule4
    scCollector3.ReplaceRules(rules6, False)
    
    markId35 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Edge Blend")
    
    edgeBlendBuilder5.Tolerance = 0.01
    
    edgeBlendBuilder5.AllInstancesOption = False
    
    edgeBlendBuilder5.RemoveSelfIntersection = True
    
    edgeBlendBuilder5.PatchComplexGeometryAreas = True
    
    edgeBlendBuilder5.LimitFailingAreas = True
    
    edgeBlendBuilder5.ConvexConcaveY = False
    
    edgeBlendBuilder5.RollOverSmoothEdge = True
    
    edgeBlendBuilder5.RollOntoEdge = True
    
    edgeBlendBuilder5.MoveSharpEdge = True
    
    edgeBlendBuilder5.TrimmingOption = False
    
    edgeBlendBuilder5.OverlapOption = NXOpen.Features.EdgeBlendBuilder.Overlap.AnyConvexityRollOver
    
    edgeBlendBuilder5.BlendOrder = NXOpen.Features.EdgeBlendBuilder.OrderOfBlending.ConvexFirst
    
    edgeBlendBuilder5.SetbackOption = NXOpen.Features.EdgeBlendBuilder.Setback.SeparateFromCorner
    
    edgeBlendBuilder5.BlendFaceContinuity = NXOpen.Features.EdgeBlendBuilder.FaceContinuity.Tangent
    
    csIndex3 = edgeBlendBuilder5.AddChainset(scCollector3, "13")
    
    try:
        # Blend faces overlap. Try blending the edges in separate features.
        feature5 = edgeBlendBuilder5.CommitFeature()
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(3620010)
        
    theSession.UndoToMarkWithStatus(markId35, None)
    
    theSession.DeleteUndoMark(markId35, None)
    
    markId36 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Edge Blend")
    
    edgeBlendBuilder5.Tolerance = 0.01
    
    edgeBlendBuilder5.AllInstancesOption = False
    
    edgeBlendBuilder5.RemoveSelfIntersection = True
    
    edgeBlendBuilder5.PatchComplexGeometryAreas = True
    
    edgeBlendBuilder5.LimitFailingAreas = True
    
    edgeBlendBuilder5.ConvexConcaveY = False
    
    edgeBlendBuilder5.RollOverSmoothEdge = True
    
    edgeBlendBuilder5.RollOntoEdge = True
    
    edgeBlendBuilder5.MoveSharpEdge = True
    
    edgeBlendBuilder5.TrimmingOption = False
    
    edgeBlendBuilder5.OverlapOption = NXOpen.Features.EdgeBlendBuilder.Overlap.AnyConvexityRollOver
    
    edgeBlendBuilder5.BlendOrder = NXOpen.Features.EdgeBlendBuilder.OrderOfBlending.ConvexFirst
    
    edgeBlendBuilder5.SetbackOption = NXOpen.Features.EdgeBlendBuilder.Setback.SeparateFromCorner
    
    edgeBlendBuilder5.BlendFaceContinuity = NXOpen.Features.EdgeBlendBuilder.FaceContinuity.Tangent
    
    csIndex4 = edgeBlendBuilder5.AddChainset(scCollector3, "12")
    
    feature6 = edgeBlendBuilder5.CommitFeature()
    
    theSession.DeleteUndoMark(markId36, None)
    
    theSession.SetUndoMarkName(markId34, "Edge Blend")
    
    workPart.FacePlaneSelectionBuilderData.Destroy(facePlaneSelectionBuilder5)
    
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression38)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression37)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    edgeBlendBuilder5.Destroy()
    
    workPart.Expressions.Delete(expression35)
    
    workPart.Expressions.Delete(expression36)
    
    markId37 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    edgeBlendBuilder6 = workPart.Features.CreateEdgeBlendBuilder(NXOpen.Features.Feature.Null)
    
    expression39 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression40 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    blendLimitsData6 = edgeBlendBuilder6.LimitsListData
    
    origin9 = NXOpen.Point3d(0.0, 0.0, 0.0)
    normal9 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    plane9 = workPart.Planes.CreatePlane(origin9, normal9, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    facePlaneSelectionBuilder6 = workPart.FacePlaneSelectionBuilderData.Create()
    
    expression41 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression42 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    theSession.SetUndoMarkName(markId37, "Edge Blend Dialog")
    
    # ----------------------------------------------
    #   Dialog Begin Edge Blend
    # ----------------------------------------------
    workPart.FacePlaneSelectionBuilderData.Destroy(facePlaneSelectionBuilder6)
    
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression42)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression41)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    edgeBlendBuilder6.Destroy()
    
    workPart.Expressions.Delete(expression39)
    
    workPart.Expressions.Delete(expression40)
    
    theSession.UndoToMark(markId37, None)
    
    theSession.DeleteUndoMark(markId37, None)
    
    rotMatrix5 = NXOpen.Matrix3x3()
    
    rotMatrix5.Xx = 0.99138966074459067
    rotMatrix5.Xy = 0.12979009094267915
    rotMatrix5.Xz = -0.017351451288555253
    rotMatrix5.Yx = 0.04234961568032429
    rotMatrix5.Yy = -0.44319184294932557
    rotMatrix5.Yz = -0.89542587654976491
    rotMatrix5.Zx = -0.1239074276242416
    rotMatrix5.Zy = 0.88698112868102996
    rotMatrix5.Zz = -0.44487237129683893
    translation5 = NXOpen.Point3d(-13.375546442226378, 10.856651967475228, 10.253645000588662)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix5, translation5, 1.219512195121951)
    
    # ----------------------------------------------
    #   Menu: Tools->Journal->Stop Recording
    # ----------------------------------------------
    
if __name__ == '__main__':
    main()