"""Provides a scripting component.
    Inputs:
        x: The x script variable
        y: The y script variable
    Output:
        a: The a output variable"""

__author__ = "jennihutson"

import rhinoscriptsyntax as rs

myCurvePts = rs.CurvePoints(myCurve)
origin = rs.CreatePoint(0,0,0)

sampleNumber = 100
zeroIndex = 0 

if myCurvePts[1].Y == 0:
    zeroIndex = 1
elif myCurvePts[1].Z == 0:
    zeroIndex = 2
    
startVert = myCurvePts[0]    

moveVect = origin - startVert
myCurve.Translate(moveVect)

if flip:
    if zeroIndex == 0 or zeroIndex == 1:
        rotAxis = rs.CreatePoint(0,0,1) - origin
    elif zeroIndex == 2:
        rotAxis = rs.CreatePoint(0,1,0) - origin
    myCurve.Rotate(180, rotAxis, origin)
    
newVerts = rs.DivideCurve(myCurve, nbPoints-1, False, True)
if zeroIndex == 0:
    if myCurvePts[0].Z > myCurvePts[len(myCurvePts)-1].Z:
        newVerts = [row[1] for row in reversed(newVerts)]
    else:
        newVerts = [row[1] for row in newVerts]
elif zeroIndex == 1:
    if myCurvePts[0].Z > myCurvePts[len(myCurvePts)-1].Z:
        newVerts = [row[0] for row in reversed(newVerts)]
    else:
        newVerts = [row[0] for row in newVerts]
else:
    if myCurvePts[0].Y > myCurvePts[len(myCurvePts)-1].Y:
        newVerts = [row[0] for row in reversed(newVerts)]
    else:
        newVerts = [row[0] for row in newVerts]
    
prevValues = []
for i in range(0, nbPoints):
    if len(values0) == 0:
        prevValues.append(0)
    elif len(values0) == 1:
        prevValues.append(values0[0])
    else:
        prevValues.append(values0[i])
        
values = []
for i in range(nbPoints):
    if mode == "additive" or mode == "":
        values.append(newVerts[i] + prevValues[i])
    elif mode == "multiplicative":
        values.append(newVerts[i] * prevValues[i])