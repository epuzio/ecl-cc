"""Provides a scripting component.
    Inputs:
        x: The x script variable
        y: The y script variable
    Output:
        a: The a output variable"""

__author__ = "sami_"
__version__ = "2022.06.28"

import rhinoscriptsyntax as rs
import math

values = []
nb = nbPoints

# check type of input for offset
offsets = []
for i in range(0, nb):
    if len(offset) == 0:
        offsets.append(0)
    elif len(offset) == 1:
        offsets.append(offset[0])
    else:
        offsets.append(offset[i])
        
prevValues = []
for i in range(0, nb):
    if len(values0) == 0:
        prevValues.append(rs.CreatePoint(0,0))
    elif len(values0) == 1:
        prevValues.append(values0[0])
    else:
        prevValues.append(values0[i])


for i in range(0, nb):
    if mode == "additive" or mode == "":
        y1 = amplitudeX1*math.cos(2*math.pi*i/periodX1 + offsets[i]) + prevValues[i].X
        y2 = amplitudeX2*math.sin(2*math.pi*i/periodX2 + offsets[i]) + prevValues[i].Y
        values.append(rs.CreatePoint(y1,y2,0))
    elif mode == "multiplicative":
        y1 = amplitudex1*math.cos(2*math.pi*i/periodX1 + offsets[i]) * prevValues[i].X
        y2 = amplitudeX2*math.sin(2*math.pi*i/periodX2 + offsets[i]) * prevValues[i].Y
        values.append(rs.CreatePoint(y1,y2,0))