'''----------------- 
# Author: Parker Clark
# Date: 1/25/2024
# Description: A class for utility functions. Used in common projects for CS330.
-----------------'''

#---Imports---#
import math
from vector import *

class Utility:
    #---Constructor---#
    def __init__(self):
        '''
        Constructor: Creates a utility object.
        '''
        pass
    
    #---Line Functions---#

    @staticmethod
    def closestPointOnLine(self, point: Vector, lineStart: Vector, lineEnd: Vector) -> Vector:
        '''
        A function that returns the closest point on a line to a given point.

        Parameters
        ----------
        point: Vector
            The point to find the closest point on the line to.

        lineStart: Vector
            The start point of the line.

        lineEnd: Vector
            The end point of the line.

        Returns
        ----------
        result: Vector
            The closest point on the line to the given point.
        '''

        fromPoint = point - lineStart
        lineDirection = lineEnd - lineStart

        # Find the closest point on the line to the given point.
        lineClosest = Vector.dotProduct(fromPoint, lineDirection) / Vector.dotProduct(lineDirection, lineDirection)
        return (lineStart + (lineClosest * (lineDirection)))
    
    @staticmethod
    def closestPointOnSegment(self, point: Vector, lineStart: Vector, lineEnd: Vector) -> Vector:
        '''
        A function that returns the closest point on a line segment to a given point.

        Parameters
        ----------
        point: Vector
            The point to find the closest point on the line to.

        lineStart: Vector
            The start point of the line.

        lineEnd: Vector
            The end point of the line.

        Returns
        ----------
        result: Vector
            The closest point on the line to the given point.
        '''

        fromPoint = point - lineStart
        lineDirection = lineEnd - lineStart

        # Find the closest point on the line to the given point.
        lineClosest = Vector.dotProduct(fromPoint, lineDirection) / Vector.dotProduct(lineDirection, lineDirection)

        # If the closest point is outside the line segment, return the closest endpoint.
        if lineClosest <= 0:
            return lineStart
        elif lineClosest >= 1:
            return lineEnd
        else:
            return (lineStart + (lineClosest * (lineDirection)))
        

    #---Path Functions---#
        
    
    def pathAssemble():
        pass
        

