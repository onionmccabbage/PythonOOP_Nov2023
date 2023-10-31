import arcpy
import datetime
from math import ceil
from math import floor
import os

class Toolbox(object):
    def __init__(self):
        '''Toolbox definition...'''
        self.label = '3D Fences'
        self.alias = '3DFences'
        self.tools = [ParallelFences, FeatureFences]

class ParallelFences(object):
    def __init__(self):
        '''Parallel Fences Definition'''
        self.label = "Parallel Fences"
        self.description = "Creates time enabled parallel fence diagrams"
        self.canRunInBackground = False

class FeatureFences(object):
    def __init__(self):
        '''Feature Fences Definition'''
        self.label = "Feature Fences"
        self.description = "Creates time enabled feature fence diagrams"
        self.canRunInBackground = False

###################################################

import math

class River(object):
    def __init__(self, shape):
        self.shape = shape
    def sinuosity(self):
        channel = self.shape.length
        deltaX = self.shape.firstPoint.X - self.shape.lastPoint.X
        deltaY = self.shape.firstPoint.Y - self.shape.lastPoint.Y
        valley = math.sqrt(pow(deltaX, 2) + pow(deltaY, 2))
        return channel/valley