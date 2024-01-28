import math
from vector import Vector
import math

# Test default constructor
v1 = Vector()
assert v1.x == 0
assert v1.y == 0
assert v1.z == 0

# Test parameterized constructor
v2 = Vector(1, 2, 3)
assert v2.x == 1
assert v2.y == 2
assert v2.z == 3

# Test setVector method
v3 = Vector()
v3.setVector(4, 5, 6)
assert v3.x == 4
assert v3.y == 5
assert v3.z == 6

# Test getVector method
v4 = Vector(7, 8, 9)
assert v4.getVector() == v4

# Test getLength method
v5 = Vector(3, 4, 5)
assert v5.getLength() == math.sqrt(50)

# Test addition operator
v6 = Vector(1, 2, 3)
v7 = Vector(4, 5, 6)
v8 = v6 + v7
assert v8.x == 5
assert v8.y == 7
assert v8.z == 9

# Test subtraction operator
v9 = Vector(7, 8, 9)
v10 = Vector(4, 5, 6)
v11 = v9 - v10
assert v11.x == 3
assert v11.y == 3
assert v11.z == 3

# Test multiplication operator
v12 = Vector(2, 3, 4)
scalar = 5
v13 = v12 * scalar
assert v13.x == 10
assert v13.y == 15
assert v13.z == 20

# Test division operator
v14 = Vector(10, 15, 20)
scalar = 5
v15 = v14 / scalar
assert v15.x == 2
assert v15.y == 3
assert v15.z == 4

# Test equality operator
v16 = Vector(1, 2, 3)
v17 = Vector(1, 2, 3)
v18 = Vector(4, 5, 6)
assert v16 == v17
assert not v16 == v18

# Test inequality operator
v19 = Vector(1, 2, 3)
v20 = Vector(4, 5, 6)
v21 = Vector(7, 8, 9)
assert v19 != v20
assert not v19 != v21

# Test dotProduct method
v22 = Vector(1, 2, 3)
v23 = Vector(4, 5, 6)
dot_product = v22.dotProduct(v23)
assert dot_product == 32

# Test normalize method
v24 = Vector(3, 4, 5)
v25 = v24.normalize()
assert math.isclose(v25.getLength(), 1)