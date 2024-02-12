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

    def test_parameterized_constructor(self):
        v2 = Vector(1, 2)
        self.assertEqual(v2.x, 1)
        self.assertEqual(v2.y, 2)

    def test_length(self):
        v3 = Vector(1, 2)
        self.assertEqual(v3.getLength(), math.sqrt(5))

    def test_addition(self):
        v4 = Vector(1, 2)
        v5 = Vector(4, 5)
        self.assertEqual(v4 + v5, Vector(5, 7))
    
    def test_subtraction(self):
        v6 = Vector(1, 2)
        v7 = Vector(4, 5)
        self.assertEqual(v7 - v6, Vector(3, 3))
    
    def test_multiplication(self):
        v8 = Vector(1, 2)
        self.assertEqual(v8 * 2, Vector(2, 4))
    
    def test_division(self):
        v9 = Vector(1, 2)
        self.assertEqual(v9 / 2, Vector(0.5, 1))
    
    def test_normalization(self):
        v14 = Vector(1, 2)
        v14.normalize()
        self.assertAlmostEqual(v14.x, 1 / math.sqrt(5), places=3)
        self.assertAlmostEqual(v14.y, 2 / math.sqrt(5), places=3)
    
    def test_equality(self):
        v15 = Vector(1, 2)
        v16 = Vector(1, 2)
        self.assertEqual(v15, v16)
    
    def test_inequality(self):
        v17 = Vector(1, 2)
        v18 = Vector(4, 5)
        self.assertNotEqual(v17, v18)

if __name__ == '__main__':
    unittest.main()
