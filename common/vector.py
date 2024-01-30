'''----------------- 
# Author: Parker Clark
# Date: 1/25/2024
# Description: A class for vector functions. Used in common projects for CS309.
-----------------'''

#---Imports---#
import math

class Vector:

    #---Constructors---#
    def __init__(self, x: int = 0, y: int = 0, z: int = 0) -> None:
        '''
        Constructor: Creates a vector with given values or a null vector if no values are provided
        '''
        self.x = x
        self.y = y
        self.z = z

    #---Setters---#
    def setVector(self, x: int, y: int, z: int) -> None:
        '''
        A function that sets the values of a vector.
        '''
        self.x = x
        self.y = y
        self.z = z

    def getVector(self) -> 'Vector':
        '''
        A function that returns the values of a vector.
        '''
        return self
    
    def getLength(self) -> int:
        '''
        A function that returns the length of a vector.
        '''
        return math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)
        
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

        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
    
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

        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
    
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

        return Vector(self.x * scalar, self.y * scalar, self.z * scalar)

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

        return Vector(self.x / scalar, self.y / scalar, self.z / scalar)
    
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
            return self.x == other.x and self.y == other.y and self.z == other.z
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

        return self.x != other.x or self.y != other.y or self.z != other.z
    
    #---Functions---#

    def dotProduct(self, other: 'Vector') -> int:
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

        return int(self.x * other.x + self.y * other.y + self.z * other.z)
    
    def normalize(self) -> 'Vector':
        '''
        A function that 'normalize's a vector. Makes a vector have a length of 1.

        Returns
        ----------
        result: Vector
            A normalized vector.
        '''

        length = self.getLength()
        return Vector(self.x / length, self.y / length, self.z / length)