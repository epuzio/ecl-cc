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
import numpy as np

class CC_ToolpathUnitGenerator(Tool, config=CONFIG):
    def state_updated(self, key):
        if key == "paths":
            self.outports["paths"] = self.state["paths"]
            
    def inports_updated(self, inportID): #from CA, redundant??
        if inportID == "position":
            self.state["position"] = int(self.inports["position"])
        if inportID == "initialRadius":
            self.state["initialRadius"] = int(self.inports["initialRadius"])
        if inportID == "layerHeight":
            self.state["layerHeight"] = int(self.inports["layerHeight"])
        if inportID == "nbLayers":
            self.state["nbLayers"] = int(self.inports["nbLayers"])
        if inportID == "nbPointsInLayer":
            self.state["nbPointsInLayer"] = int(self.inports["nbPointsInLayer"])
            
            
        if inportID == "radiusShapingParameter":
            if self.inports["radiusShapingParameter"]:
                self.state["radiusShapingParameter"] = int(self.inports["radiusShapingParameter"]) * int(self.state["nbPointsInLayer"])
            else:
                self.state["radiusShapingParameter"] = np.zeros(self.state["nbPointsInLayer"])
        
        if inportID == "scaleShapingParameter":
            if self.inports["scaleShapingParameter"]:
                self.state["scaleShapingParameter"] = int(self.inports["scaleShapingParameter"]) * int(self.state["nbLayers"])
            else:
                self.state["radiusShapingParameter"] = np.zeros(self.state["nbLayers"])
        
        if inportID == "radiusShapingParameter":
            if self.inports["radiusShapingParameter"]:
                self.state["radiusShapingParameter"] = int(self.inports["radiusShapingParameter"]) * int(self.state["nbPointsInLayer"])
            else:
                self.state["radiusShapingParameter"] = np.zeros(self.state["nbPointsInLayer"])
        
        
        
      
        
        
    ## last 5 Parameters can be set to 0 if not used
        
    #all other parameters are dependent on nbLayers 
    def set_scale_rotate_translate_scaleradius():
        if not self.inports["scaleShapingParameter"]:
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



        
    
    




