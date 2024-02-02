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
offsetsX1 = []
offsetsX2 = []
for i in range(0, nb):
    if len(offsetX1) == 0:
        offsetsX1.append(0)
    elif len(offsetX1) == 1:
        offsetsX1.append(offsetX1[0])
    else:
        offsetsX1.append(offsetX1[i])
    
    if len(offsetX2) == 0:
        offsetsX2.append(offsetX2[i])
    elif len(offsetX2) == 1:
        offsetsX2.append(offsetX2[0])
    else:
        offsetsX2.append(offsetX2[i])
        
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
        y1 = amplitudeX1 * i + offsetsX1[i]
        y2 = amplitudeX2 * i + offsetsX2[i]
        values.append( rs.CreatePoint(y1,y2,0) + prevValues[i])
    elif mode == "multiplicative":
        y1 = amplitudeX1 * i + offsetsX1[i]
        y2 = amplitudeX2 * i + offsetsX2[i]
        values.append( rs.CreatePoint(y1,y2,0) * prevValues[i])