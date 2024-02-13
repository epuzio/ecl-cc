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
index = 0

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
        prevValues.append(0)
    elif len(values0) == 1:
        prevValues.append(values0[0])
    else:
        prevValues.append(values0[i])

for i in range(0, nbPoints):
    if mode == "additive" or mode == "":
        if i % stepWidth == 0 and i != 0:
            index += stepHeight
        values.append(index + offsets[i] + prevValues[i])
    if mode == "multiplicative":
        if i % stepWidth == 0 and i != 0:
            index += stepHeight
        values.append((index + offsets[i]) * prevValues[i])
