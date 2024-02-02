###P_Round_Gcode
__author__ = "mert_toka"
__version__ = "2022.02.02"

import rhinoscriptsyntax as rs

_x = int(x*100)/100.0
_y = int(y*100)/100.0
_z = int(z*100)/100.0
_e = int(e*10000)/10000.0
_f = int(f*100)/100.0


#P##y_extrusion
__author__ = "mert_toka"
__version__ = "2022.04.29"

import rhinoscriptsyntax as rs
import math

# input
NozzleWidth
LayerHeight
SegmentLen

# output
E = 0

E = SegmentLen*LayerHeight/NozzleWidth * (4/math.pi + LayerHeight/NozzleWidth)
#E = (4*LayerHeight*SegmentLen*ExtrusionMultiplier) / (math.pi*NozzleWidth)


###PY_adjust EX
"""Provides a scripting component.
    Inputs:
        x: The x script variable
        y: The y script variable
    Output:
        a: The a output variable"""

__author__ = "mert_"
__version__ = "2022.10.18"

import rhinoscriptsyntax as rs

# Input
extrusions

min = 0.8
max = 1.5

# Output
modE = []

def map(value, istart, istop, ostart, ostop):
    return ostart + (ostop - ostart) * ((value - istart) / (istop - istart))

maxIdx = len(extrusions)
midIdx = maxIdx*0.5
for i, e in enumerate(extrusions):
    modE.append(e*map(i, 0, maxIdx-1, max, min))
    
#    if i < midIdx:
#        modE.append(e*map(i, 0, midIdx, max, min))
#    else:
#        modE.append(e*map(i, midIdx, maxIdx, min, max))