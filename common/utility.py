'''----------------- 
# Author: Parker Clark
# Date: 1/25/2024
# Description: A class for utility and vector functions. Used in common projects for CS330.
-----------------'''


#---Imports---#
import math

class Vector:

    #---Constructors---#
    def __init__(self, x: int = 0, y: int = 0) -> None:
        '''
        Constructor: Creates a vector with given values or a null vector if no values are provided
        '''
        self.x = x
        self.y = y

    #---Setters---#
    def setVector(self, x: int, y: int) -> None:
        '''
        A function that sets the values of a vector.
        '''
        self.x = x
        self.y = y

    def getVector(self) -> 'Vector':
        '''
        A function that returns the values of a vector.
        '''
        return self
    
    def getLength(self) -> int:
        '''
        A function that returns the length of a vector.
        '''
        return math.sqrt(math.pow(self.x, 2) + math.pow(self.y, 2))
        
    #---Operations---#
    def __add__(self, other: 'Vector') -> 'Vector':
        '''
        A function that adds two vectors together. Overloads the '+' operator for vectors.

        Parameters
        ----------
        other: Vector
            The vector to be added to the current vector.

        Returns
        ----------
        result: Vector
            A resultant vector post addition.
        '''

        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other: 'Vector') -> 'Vector':
        '''
        A function that subtracts two vectors together. Overloads the '-' operator for vectors.

        Parameters
        ----------
        other: Vector
            The vector to be subtracted from the current vector.

        Returns
        ----------
        result: Vector
            A resultant vector post subtraction.
        '''

        return Vector(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar: int) -> 'Vector':
        '''
        A function that multiplies a vector by a scalar. Overloads the '*' operator for vectors.

        Parameters
        ----------
        scalar: int
            The scalar to multiply the vector by.
        
        Returns
        ----------
        result: Vector
            A resultant vector post multiplication.
        '''

        return Vector(self.x * scalar, self.y * scalar)

    def __truediv__(self, scalar: int) -> 'Vector':
        '''
        A function that divides a vector by a scalar. Overloads the '/' operator for vectors.

        Parameters
        ----------
        scalar: int
            The scalar to divide the vector by.
        
        Returns
        ----------
        result: Vector
            A resultant vector post division.
        '''

        return Vector(self.x / scalar, self.y / scalar)
    
    def __eq__(self, other: 'Vector') -> bool:
        '''
        A function that checks if two vectors are equal. Overloads the '==' operator for vectors.

        Parameters
        ----------
        other: Vector
            The vector to be compared to the current vector.

        Returns
        ----------
        result: bool
            A boolean value representing whether the two vectors are equal.
        '''
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        return False
    
    def __ne__(self, other: 'Vector') -> bool:
        '''
        A function that checks if two vectors are not equal. Overloads the '!=' operator for vectors.

        Parameters
        ----------
        other: Vector
            The vector to be compared to the current vector.

        Returns
        ----------
        result: bool
            A boolean value representing whether the two vectors are not equal.
        '''

        return self.x != other.x or self.y != other.y
    
    #---Functions---#
    @staticmethod
    def dotProduct(a: 'Vector', b: 'Vector') -> int:
        '''
        A function that calculates the dot product of two vectors.

        Parameters
        ----------
        other: Vector
            The vector to be multiplied by the current vector.
        
        Returns
        ----------
        result: int
            An integer representing the dot product of the two vectors.
        '''

        return int(a.x * b.x + a.y * b.y)
    
    def normalize(self) -> 'Vector':
        '''
        A function that 'normalize's a vector. Makes a vector have a length of 1.

        Returns
        ----------
        result: Vector
            An updated vector object with normalized values.
        '''

        length = self.getLength()

        self.x /= length
        self.y /= length
    
    def null(self) -> 'Vector':
        '''
        A function that sets a vector to a null vector.

        Returns
        ----------
        result: Vector
            A null vector.
        '''

        return Vector(0, 0)

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
        

