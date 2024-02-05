from planager.Tool import Tool

# importing the module
import json
import os.path

# Opening JSON file
with open(os.path.join(os.path.dirname(__file__), "CC_BooleanUnion.tool")) as json_file:
    CONFIG = json.load(json_file)


class CC_BooleanUnion(Tool, config=CONFIG):
    def state_updated(self, key):
        self.outports["bool"] = self.state["bool"]

    def setup(self):
        self.outports["bool"] = self.state["bool"]


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

