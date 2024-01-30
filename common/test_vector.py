'''----------------- 
# Author: Parker Clark
# Date: 1/29/2024
# Description: A unit test for the vector class. Used in common projects for CS309 (I got bored).
-----------------'''

#---Imports---#
import math
import unittest
from vector import Vector

class TestVector(unittest.TestCase):
    def test_default_constructor(self):
        v1 = Vector()
        self.assertEqual(v1.x, 0)
        self.assertEqual(v1.y, 0)
        self.assertEqual(v1.z, 0)

    def test_parameterized_constructor(self):
        v2 = Vector(1, 2, 3)
        self.assertEqual(v2.x, 1)
        self.assertEqual(v2.y, 2)
        self.assertEqual(v2.z, 3)

    def test_length(self):
        v3 = Vector(1, 2, 3)
        self.assertEqual(v3.getLength(), math.sqrt(14))

    def test_addition(self):
        v4 = Vector(1, 2, 3)
        v5 = Vector(4, 5, 6)
        self.assertEqual(v4 + v5, Vector(5, 7, 9))
    
    def test_subtraction(self):
        v6 = Vector(1, 2, 3)
        v7 = Vector(4, 5, 6)
        self.assertEqual(v7 - v6, Vector(3, 3, 3))
    
    def test_multiplication(self):
        v8 = Vector(1, 2, 3)
        self.assertEqual(v8 * 2, Vector(2, 4, 6))
    
    def test_division(self):
        v9 = Vector(1, 2, 3)
        self.assertEqual(v9 / 2, Vector(0.5, 1, 1.5))
    
    def test_dot_product(self):
        v10 = Vector(1, 2, 3)
        v11 = Vector(4, 5, 6)
        self.assertEqual(v10.dotProduct(v11), 32)
    
    def test_normalization(self):
        v14 = Vector(1, 2, 3)
        self.assertEqual(v14.normalize(), Vector(1 / math.sqrt(14), 2 / math.sqrt(14), 3 / math.sqrt(14)))
    
    def test_equality(self):
        v15 = Vector(1, 2, 3)
        v16 = Vector(1, 2, 3)
        self.assertEqual(v15, v16)
    
    def test_inequality(self):
        v17 = Vector(1, 2, 3)
        v18 = Vector(4, 5, 6)
        self.assertNotEqual(v17, v18)

if __name__ == '__main__':
    unittest.main()
