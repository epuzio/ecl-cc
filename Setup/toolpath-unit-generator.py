"""Provides a scripting component.
    Inputs:
        x: The x script variable
        y: The y script variable
    Output:
        a: The a output variable"""

__author__ = "sami_"
__version__ = "2022.06.29"

import rhinoscriptsyntax as rs
import math

path = []
nbPoints = nbPointsInLayer 
radius = initialRadius

# check if shaping parameters are empty
radsp = []
for i in range(0, nbPoints):
    if radiusShapingParameter == []:
        radsp.append(0)
    else:
        radsp.append(radiusShapingParameter[i])

ssp = []
rsp = []
tsp = []
srsp = []
for j in range(0, nbLayers):
    if scaleShapingParameter == []:
        ssp.append(0)
    else:
        ssp.append(scaleShapingParameter[j])
        
    if rotateShapingParameter == []:
        rsp.append(0)
    else:
        rsp.append(rotateShapingParameter[j])
        
    if translateShapingParameter == []:
        tsp.append(rs.CreatePoint(0,0,0))
    else:
        tsp.append(translateShapingParameter[j])

if scalingRadiusShapingParameter == []:
    #print(scalingRadius)
    for j in range(0, nbLayers):
        srsp.append(1)
else:
    for j in range(0, nbLayers):
        srsp.append(scalingRadiusShapingParameter[j])


vectors = []
for j in range(0, nbLayers):
    for i in range(0, nbPoints):
        angle = 360/nbPoints
        path.append(rs.CreatePoint(position.X + (radius+srsp[j]*radsp[i]+ssp[j])*math.cos(i*angle*math.pi/180 + rsp[j]*math.pi/180) + tsp[j].X, position.Y + (radius + srsp[j]*radsp[i] + ssp[j] )*math.sin(i*angle*math.pi/180 + rsp[j]*math.pi/180) + tsp[j].Y, position.Z+layerHeight*j))
        #path.append(rs.CreatePoint(position.X + (radius+radsp[i]+ssp[j])*math.cos(i*angle*math.pi/180 + rsp[j]*math.pi/180) + tsp[j].X, position.Y + (radius + radsp[i] + ssp[j] )*math.sin(i*angle*math.pi/180 + rsp[j]*math.pi/180) + tsp[j].Y, position.Z+layerHeight*j))

