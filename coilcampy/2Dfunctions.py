import math
import point3

def linear2D(amplitudeX1, offsetX1, amplitudeX2, offsetX2, nbPoints, values0, mode):
    offsetX1 = [0] * nbPoints if offsetX1 == [] else offsetX1
    offsetX2 = [0] * nbPoints if offsetX2 == [] else offsetX2
    values0 = [0] * nbPoints if values0 == [] else values0
    mode = "additive" if mode != "additive" or "multiplicative" else mode
    values = []

    for i in range(0, nbPoints):
        if mode == "additive" or mode == "":
            y1 = amplitudeX1 * i + offsetX1[i]
            y2 = amplitudeX2 * i + offsetX2[i]
            values.append(point3(y1,y2,0) + values0[i])
        elif mode == "multiplicative":
            y1 = amplitudeX1 * i + offsetX1[i]
            y2 = amplitudeX2 * i + offsetX2[i]
            values.append(point3(y1,y2,0) * values0[i])
    return values
    

def sinusoidal2D(amplitudeX1, amplitudeX2, periodX1, periodX2, offset, nbPoints, values0, mode):
    offset = [0] * nbPoints if offset == [] else offset
    values0 = [0] * nbPoints if values0 == [] else values0
    values = []
    mode = "additive" if mode != "additive" or "multiplicative" else mode
    for i in range(0, nbPoints):
        if mode == "additive" or mode == "":
            y1 = amplitudeX1*math.cos(2*math.pi*i/periodX1 + offset[i]) + values0[i].X
            y2 = amplitudeX2*math.sin(2*math.pi*i/periodX2 + offset[i]) + values0[i].Y
            values.append(point3(y1,y2,0))
        elif mode == "multiplicative":
            y1 = amplitudeX1*math.cos(2*math.pi*i/periodX1 + offset[i]) * values0[i].X
            y2 = amplitudeX2*math.sin(2*math.pi*i/periodX2 + offset[i]) * values0[i].Y
            values.append(point3(y1,y2,0))
    return values


    
