from planager.Tool import Tool

# importing the module
import json
import os.path

import rhinoinside
rhinoinside.load()
import System
import Rhino

# Opening JSON file
with open(os.path.join(os.path.dirname(__file__), "CC_BooleanUnion.tool")) as json_file:
    CONFIG = json.load(json_file)

'''
Takes in two toolpaths as parameters, toolpaths (typically?) created by Toolpath Unit Generator
path0 and path1 are arrays of (x, y, z) points (Point3D in Rhino)
'''


class CC_BooleanUnion(Tool, config=CONFIG): #copied from Array2D!
    def state_updated(self, key):
        if key == "paths":
            self.outports["paths"] = self.state["paths"]
    def inports_updated(self, inportID): #set(?) inport values
        port_handlers = {
            "path0": self.set_path1,
            "path1": self.set_path1,
            "radius": self.set_radius,
            "tolerance": self.set_tolerance,
        }
        port_handlers[inportID]()    

    ### SET PORTS
    def set_path0(self):
        if not self.inports["path0"]:
            return
        self.set_paths()
        self.merge_toolpaths()

    def set_path1(self):
        if not self.inports["path1"]:
            return
        self.set_paths()
        self.merge_toolpaths()
        
    def set_radius(self):
        if not self.inports["radius"]:
            return
        self.state["radius"] = int(self.inports["radius"])
        self.merge_toolpaths()
        
    def set_tolerance(self):
        if not self.inports["tolerance"]:
            return
        self.state["tolerance"] = int(self.inports["tolerance"])
        self.merge_toolpaths()

    ### CALCULATIONS (From Sam's code)
    
    def set_paths(self): #Set path0 > path1
        if len(self.inports["path0"]) < len(self.inports["path1"]):
            self.state["path0"], self.state["path1"] = self.inports["path1"], self.inports["path0"]
        self.state["path0"], self.state["path1"] = self.inports["path0"], self.inports["path1"]
    
    def merge_toolpaths(self):
        path0 = self.state["path0"]
        path1 = self.state["path1"]
        index0 = 0
        index1 = 0
        globalIndex = 0
        path = []
        
        
        if len(path0) != 0:
            currentHeight = path0[0].Z if path0[0].Z <= path1[0].Z else path1[0].Z
            
            while (index0 < len(path0) or index1 < len(path1)):
            
                curves = []
                
                # manage first path
                points0 = []
                if index0 < len(path0):
                    currentHeight = path0[index0].Z
                    points0.append(rs.CreatePoint(path0[index0].X, path0[index0].Y, path0[index0].Z))
                    globalIndex += 1
                    index0 += 1
                    
                    # add the points of same height to one array
                    for i in range(index0, len(path0)):
                        if (path0[i].Z == points0[0].Z):
                            points0.append(rs.CreatePoint(path0[i].X, path0[i].Y, path0[i].Z))
                            index0 += 1
                            globalIndex += 1
                        else:
                            break
                    # close the curve by adding the first point to the end of the array and add curve0 to curves
                    points0.append(points0[0])
                    curve0 = rs.AddPolyline(points0)
                    rs.CloseCurve(curve0)
                    curves.append(curve0)
                
                #manage second path
                points1 = []
                if index1 < len(path1) and path1[index1].Z == currentHeight:
                    points1.append(rs.CreatePoint(path1[index1].X, path1[index1].Y, path1[index1].Z))
                    index1 += 1
                    globalIndex += 1
                    for i in range(index1, len(path1)):
                        if (path1[i].Z == points1[0].Z):
                            points1.append(rs.CreatePoint(path1[i].X, path1[i].Y, path1[i].Z))
                            index1 += 1
                            globalIndex += 1
                        else:
                            break
                    points1.append(points1[0])
                    curve1 = rs.AddPolyline(points1)
                    rs.CloseCurve(curve1)
                    curves.append(curve1)
                
                #if two curves try boolean
                if len(curves) >= 2:
                    a = rs.CurveBooleanUnion(curves)
                    
                    if (len(a) == 1):
                        rs.coercecurve(a)
                        b = rg.Curve.CreateFilletCornersCurve(rs.coercecurve(a), radius, tolerance, 0.0)
                        fillet.append(b)
                        newCurve = sc.doc.Objects.AddCurve(b)
                        points = rs.CurvePoints(newCurve)
                        for i in range(0, len(points)-1):
                            path.append(rs.CreatePoint(points[i].X, points[i].Y, points[i].Z))
                    else:
                        for i in range(0, len(points0)):
                            path.append(rs.CreatePoint(points0[i].X, points0[i].Y, points0[i].Z))
                            
                        stops.append(len(path)-1)
                        stopPoints.append(path[len(path)-1])
                    
                        for i in range(0, len(points1)):
                            path.append(rs.CreatePoint(points1[i].X, points1[i].Y, points1[i].Z))
                        
                        stops.append(len(path)-1)
                        stopPoints.append(path[len(path)-1])
                else:
                    if index0 < len(path0):
                        for i in range(0, len(points0)):
                            path.append(rs.CreatePoint(points0[i].X, points0[i].Y, points0[i].Z))
                    elif index1 < len(path1):
                        for i in range(0, len(points1)):
                            path.append(rs.CreatePoint(points1[i].X, points1[i].Y, points1[i].Z))



#combine two shapes into one!

# Union
# The union of the two input toolpaths. Works only between layers of the same height and if the two paths start at the same Z.
# ** the number of layers (nbLayers) in the two toolpaths MUST be the same 
# (Point3D) Path0: first toolpath
# (Point3D) Path1: second toolpath
# (float, optional) Radius: radius of the fillet curve added at the intersection between path0 and path1
# (float, optional) Tolerance: fillet tolerance 
# Out: Console output
# Path: Ordered array of points (point3d)
# stops: point indices at which a clay extrusion stop is required
# stopPoints: points in the final path at which a clay extrusion stop is required, stops are required when a layer is non-continuous
# Fillet: Fillet curves generated at the intersections of the boolean, useful to visualize where it breaks 

