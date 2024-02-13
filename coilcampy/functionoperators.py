import math
import point3

#passing in optional values?

def sinusoidal(amplitude, period, offset, nbPoints, values0, mode):
    offset = [0] * nbPoints if offset == [] else offset
    values0 = [0] * nbPoints if values0 == [] else values0
    values = []
    
    for i in range(0, nbPoints):
        if mode == "additive" or mode == "":
            values.append(amplitude * math.pow(math.sin(period*i + offset[i]), 2) + values0[i])
        elif mode == "multiplicative":
            values.append(amplitude * math.pow(math.sin(period*i + offset[i]), 2) * values0[i])
    return values



def square(amplitude, period, bumps, offset, nbPoints, values0, mode):
    offset = [0] * nbPoints if offset == [] else offset
    values0 = [0] * nbPoints if values0 == [] else values0
    bumps = None
    values = []

    for i in range(0, nbPoints):
        if mode == "additive" or mode == "":
            if bumps and bumps <= (i + offset[i])%period:
                values.append((amplitude * 0) + values0[i])
            else:
                values.append((amplitude * 1) + values0[i])
        elif mode == "multiplicative":
            if bumps and bumps <= (i + offset[i])%period:
                values.append((amplitude * 0) * values0[i])
            else:
                values.append((amplitude * 1) * values0[i])
       
       
       
                
def staircase(stepWidth, stepHeight, offset, nbPoints, values0, mode):
    offset = [0] * nbPoints if offset == None else offset
    values0 = [0] * nbPoints if values0 == [] else values0
    mode = "additive" if mode != "additive" or "multiplicative" else mode
    values = []
    index = 0

    for i in range(0, nbPoints):
        if mode == "additive":
            if i % stepWidth == 0 and i != 0:
                index += stepHeight
            values.append(index + offset[i] + values0[i])
        if mode == "multiplicative":
            if i % stepWidth == 0 and i != 0:
                index += stepHeight
            values.append((index + offset[i]) * values0[i])
    return values
                
                
                
def linear(amplitude, offset, nbPoints, values0, mode):
    offset = [0] * nbPoints if offset == [] else offset
    values0 = [0] * nbPoints if values0 == [] else values0
    mode = "additive" if mode != "additive" or "multiplicative" else mode
    values = []

    for i in range(0, nbPoints):
        if mode == "additive":
            values.append((amplitude * i + offset[i]) + values0[i]) 
        elif mode == "multiplicative":
            values.append((amplitude * i + offset[i]) * values0[i])
    return values
    


def exponential(amplitude, base, ampExp, offset, nbPoints, values0, mode):
    offset = [0] * nbPoints if offset == [] else offset
    values0 = [0] * nbPoints if values0 == [] else values0
    mode = "additive" if mode != "additive" or "multiplicative" else mode
    values = []

    for i in range(0, nbPoints):
        if mode == "additive":
            values.append(amplitude * math.pow(base,ampExp*i + offset[i]) + values0[i])
        elif mode == "multiplicative":
            values.append(amplitude * math.pow(base, ampExp*i + offset[i]) * values0[i])
    return values



def curveinterp(myCurve, flip, nbPoints, values0, mode):
    origin = rs.CreatePoint(0,0,0)

    sampleNumber = 100
    zeroIndex = 0 