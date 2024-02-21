'''----------------- 
# Author: Parker Clark
# Date: 1/25/2024
# Description: A class for path functions. Used in Program Assignment 2.
-----------------'''

#---Imports---#
import math
from utility import Vector
from utility import Utility

class Path:

    #---Constructor---#
    def __init__(self, ID, x, y):
        '''
        Constructor: Creates a path object, maintains the same logic as path.assemble().

        Members
        ----------
        ID: const int
            The function ID of the given path being assembled.
        
        x: int
            The starting x coordinate of the path to be assembled.
        
        y: int
            The starting y coordinate of the path to be assembled.
        
        pathSegments: int
            Count of path segments.
        
        distance: list (int)
            Total distance of the path segments in a list.
        
        param: list (int)
            Prepared list of path parameters. 
        '''

        # Define members
        self.ID = ID
        self.x = x
        self.y = y

        # Setup variables to build the path
        self.pathSegments = len(x) - 1
        self.distance = (self.pathSegments + 1) * [0] # Replicate pathSegments into a list of itself to calculate distance

        # Insert endpoints of S into path struct
        for i in range(1, self.pathSegments + 1):
            self.distance[i] = self.distance[i-1] + Utility.distanceBetweenPoints(Vector(self.x[i-1], self.y[i-1]), Vector(self.x[i], self.y[i]))

        self.param = (self.pathSegments + 1) * [0] # Replicate pathSegments into a list for line parameter

        for i in range(1, self.pathSegments + 1):
            self.param[i] = self.distance / max(self.distance)

    def getPosition(self, param):
        '''
        A function that returns path position from a given parameter.

        Parameters
        ----------
        param: int
            Path parameter to grab position from.

        Returns
        ----------
        position: int
            The current position of the path.
        '''

        for i in range(self.pathSegments+1):
            if param > self.param[i]:
                index = i
            else: # Break the loop, if the given param is not greater then whats already in the object
                break
        
        # Define point positions on the line
        pointA = Vector(self.x[index], self.y[index])
        pointB = Vector (self.x[index +1], self.y[index + 1])

        T = (param - self.param[i]) / (self.param[i+1]- self.param[i])
        position = pointA + (T * (pointB - pointA))
        return(position)
    
    def getParam(self, position):
        '''
        A function that returns path parameter given position.

        Parameters
        ----------
        position: Vector
            The current position of the path expressed as a Vector.

        Returns
        ----------
        param: int
            Path parameter that derived from position.
        '''

        closestDistance = float('inf') # Create closestDistance at 'infinity'

        for i in range(self.pathSegments):
            
            # Generate points off of the segment
            pointA = Vector(self.x[i], self.y[i])
            pointB = Vector (self.x[i +1], self.y[i + 1])

            checkPoint = Utility.closestPointOnSegment(position, pointA, pointB)
            checkDistance = Utility.distanceBetweenPoints(position, checkPoint)

            if checkDistance < closestDistance:
                closestPoint = checkPoint
                closestDistance =  checkDistance
                closestSegment = i
        
        # Set variables to calculate param
        pointA = Vector(self.x[closestSegment], self.y[closestSegment])
        paramA = self.param[closestSegment]

        pointB = Vector(self.x[closestSegment + 1], self.y[closestSegment + 1])
        paramB = self.param[closestSegment]

        # Calculate and return the param
        T = Vector(closestPoint - pointA).getLength() / Vector(pointB - pointA).getLength()
        return (paramA + (T * (paramB - paramA)))

