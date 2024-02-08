"""Provides a scripting component.
    Inputs:
        x: The x script variable
        y: The y script variable
    Output:
        a: The a output variable"""

__author__ = "sami_"
__version__ = "2022.06.29"

import rhinoscriptsyntax as rs
import math

from planager.Tool import Tool
import json
import os.path
import OpenGL as gl

class CC_ToolpathUnitGenerator(Tool, config=CONFIG):
    def state_updated(self, key):
        if key == "paths":
            self.outports["paths"] = self.state["paths"]
            
    def inports_updated(self, inportID): #from Array2D
        port_handlers = {
            "position": self.set_position
            "initialRadius": self.set_initial_radius
            "layerHeight": self.set_layer_height
            "nbLayers": self.set_nb_layers
            "nbPointsInLayer": self.set_nb_points_in_layer
            "radiusShapingParameter": self.set_radius_shaping
            "scalingRadiusShapingParameter": self.set_scale_rotate_translate_scaleradius
            "scaleShapingParameter": self.set_scale_rotate_translate_scaleradius
            "translateShapingParameter": self.set_scale_rotate_translate_scaleradius
            "rotateShapingParameter": self.set_scale_rotate_translate_scaleradius
        }
        port_handlers[inportID]()
        
        
   
    
    # First 5 inputs to be set for calculations - is this redundant?
    def set_position(self):
        if not self.inports["position"]:
            return
        self.state["position"] = int(self.inports["position"])
    
    def set_initial_radius(self):
        if not self.inports["initialRadius"]:
            return
        self.state["initialRadius"] = int(self.inports["initialRadius"])
        
    def set_layer_height(self):
        if not self.inports["layerHeight"]:
            return
        self.state["layerHeight"] = int(self.inports["layerHeight"])
    
    def set_nb_layers():
        if not self.inports["nbLayers"]:
            return
        self.state["nbLayers"] = int(self.inports["nbLayers"])

    def set_nb_points_in_layer():
        if not self.inports["nbPointsInLayer"]:
            return
        self.state["nbPointsInLayer"] = int(self.inports["nbPointsInLayer"])
    
        
        
        
    ## last 5 Parameters can be set to 0
    
    #radius shaping parameter is dependent on nbPointsInLayer
    def set_radius_shaping(): #check logic
        if not self.inports["nbPointsInLayer"]: #radiusShapingParameter is empty
            self.state["radiusShapingParameter"] = np.zeros(self.state["nbPointsInLayer"])
            return
        radsp = []
        for i in range(0, self.state["nbPoints"]):
            radsp.append(self.inports["radiusShapingParameter"][i])
            self.state["radiusShapingParameter"] = radsp
        
        
    #all other parameters are dependent on nbLayers 
    def set_scale_rotate_translate_scaleradius():
        if not self.inports["nbLayers"]:
            self.state["scaleShapingParameter"] = np.zeros(self.state["nbLayers"])
            self.state["translateShapingParameter"] = np.zeros(self.state["nbLayers"])
            self.state["rotateShapingParameter"] = np.zeros(self.state["nbLayers"])
            self.state["scalingRadiusShapingParameter"] = np.zeros(self.state["nbLayers"])
            return
            
        for j in range(0, nbLayers):
            if scaleShapingParameter == []:
                ssp.append(0)
            else:
                ssp.append(scaleShapingParameter[j])
                
            if rotateShapingParameter == []:
                rsp.append(0)
            else:
                rsp.append(rotateShapingParameter[j])
                
            if translateShapingParameter == []:
                tsp.append(rs.CreatePoint(0,0,0))
            else:
                tsp.append(translateShapingParameter[j])
                
        if scalingRadiusShapingParameter == []:
            #print(scalingRadius)
            for j in range(0, nbLayers):
                srsp.append(1)
        else:
            for j in range(0, nbLayers):
                srsp.append(scalingRadiusShapingParameter[j])

        
        
    
    def generate_toolpath(self): #oneliner from Mert
        path = []
        nbPoints = self.state["nbPoints"]
        nbLayers = self.state["nbLayers"]
        
        
        
        for j in range(0, nbLayers):
            for i in range(0, nbPoints):
                angle = 360/nbPoints
                path.append((position[0] + (radius+srsp[j]*radsp[i]+ssp[j])*math.cos(i*angle*math.pi/180 + rsp[j]*math.pi/180) + tsp[j].X, 
                             position.Y + (radius + srsp[j]*radsp[i] + ssp[j] )*math.sin(i*angle*math.pi/180 + rsp[j]*math.pi/180) + tsp[j].Y, 
                             position.Z+layerHeight*j))
                #path.append(rs.CreatePoint(position.X + (radius+radsp[i]+ssp[j])*math.cos(i*angle*math.pi/180 + rsp[j]*math.pi/180) + tsp[j].X, position.Y + (radius + radsp[i] + ssp[j] )*math.sin(i*angle*math.pi/180 + rsp[j]*math.pi/180) + tsp[j].Y, position.Z+layerHeight*j))



        
    
    




