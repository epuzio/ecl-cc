import math

def pyextrusion(NozzleDiameter, LayerHeight, SegmentLen):
    #segment len needs some conversions n stuff
    points = []
    extrusion_multiplier = (NozzleDiameter/1.91)^2 #extrusion multiplier for correct filament thickness
    for l in SegmentLen:
        points.append((l*LayerHeight/NozzleDiameter * (4/math.pi + LayerHeight/NozzleDiameter)) * extrusion_multiplier)
    return points

def roundgcode(x, y, z, e, f):
    _x = int(x*100)/100.0
    _y = int(y*100)/100.0
    _z = int(z*100)/100.0
    _e = int(e*10000)/10000.0
    _f = int(f*100)/100.0
    return _x, _y, _z, _e, _f

def generategcode(nozzleDiameter, path, printSpeed, layerHeight): #main function
    '''
    printSpeed, nozzleDiameter, LayerHeight: float
    path: array of point3
    '''
    printSpeed = int(printSpeed*60)
    printSpeeds = [0] 
    printSpeeds.append(printSpeed * len(path)-1)
    
    segmentLen = [len(p) for p in path]
    
    extrude = pyextrusion(nozzleDiameter, layerHeight, segmentLen)
    
    path_x = [p.X for p in path]
    path_y = [p.Y for p in path]
    path_z = [p.Z for p in path]
    
    
    gcode = []
    #Start GCode:
    gcode.append(";;; START GCODE ;;;\nM82 ;absolute extrusion mode\nG28 ;Home\nG1 X207.5 Y202.5 Z20 F10000 ;Move X and Y to center, Z to 20mm high\nG1 E2000 F20000 ; !!Prime Extruder\nG92 E0\nG1 F30000 E-150\n;;; ======")
    
    
    x, y, z, e, f = roundgcode(path_x, path_y, path_z, extrude, printSpeed)
    for (x, y, z, e, f) in enumerate(zip(x, y, z, e, f)):
        gcode.append(f"G1 F{f} X{x} Y{y} Z{z} E{e}")
    
    
    #End GCode:
    gcode.append(";;; === END GCODE ===\nM83 ;Set to Relative Extrusion Mode\nG28 Z ;Home Z\n; === DEPRESSURIZE ===\nG91\nG91\nG1 E-1300 F4000\nG90\nG90")
    
    nbTubes = 0 #placeholder
    clayHeight = 0 #placeholder
    return gcode, Nbtubes, clayHeight