"""Provides a scripting component.
    Inputs:
        x: The x script variable
        y: The y script variable
    Output:
        a: The a output variable"""

__author__ = "sami_"
__version__ = "2022.06.29"

import math
import point3

def toolpathunitgenerator(position, initialRadius, layerHeight, nbLayers, nbPointsInLayer,
                          radiusShapingParameter = [], scalingRadiusShapingParameter = [], scaleShapingParameter = [], 
                          translateShapingParameter = [], rotateShapingParameter = []):
    path = []
    radsp = radiusShapingParameter if radiusShapingParameter != [] else [0] * nbPointsInLayer
    ssp = scaleShapingParameter if scaleShapingParameter != [] else [0] * nbLayers
    rsp = rotateShapingParameter if rotateShapingParameter != [] else [0] * nbLayers
    tsp = translateShapingParameter if translateShapingParameter != [] else [point3(0, 0, 0)] * nbLayers
    srsp = scalingRadiusShapingParameter if scaleShapingParameter != [] else [1] * nbLayers

    for j in range(0, nbLayers):
        for i in range(0, nbPointsInLayer):
            angle = 360/nbPointsInLayer
            path.append(point3(position.X + (initialRadius+srsp[j]*radsp[i]+ssp[j])*math.cos(i*angle*math.pi/180 + rsp[j]*math.pi/180) + tsp[j].X, 
                               position.Y + (initialRadius + srsp[j]*radsp[i] + ssp[j] )*math.sin(i*angle*math.pi/180 + rsp[j]*math.pi/180) + tsp[j].Y, 
                               position.Z+layerHeight*j))
    return path
