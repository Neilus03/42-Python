'''
from vector import Vector

# Define two vectors
v1 = Vector([[1], [2], [3]], (3, 1))
v2 = Vector([[1, 2, 3]], (1, 3))

# Print the original vectors
print("Original vectors:\n")
print("v1:", v1.values,'shape:', v1.shape)
print("v2:", v2.values,'shape:', v2.shape)

try:
    # Transpose the vectors
    v1.T()
    v2.T()
except Exception as e:
    print(f"An error occurred during vector transposition: {e}")

# Print the transposed vectors
print("\nTransposed vectors:\n")
print("v1:", v1.values,'shape:', v1.shape)
print("v2:", v2.values,'shape:', v2.shape)


# Vector dot product
print("\nVector dot product:\n")
v3 = Vector([[4], [5], [6]], (3, 1))
print("v1:", v1.values,'shape:', v1.shape)
print("v3:", v3.values,'shape:', v3.shape)
try:
    v4 = v1.dot(v3)
    print("v4 = v1 ⋅ v3 =", v4)
except Exception as e:
    print(f"An error occurred during vector dot product: {e}")


# Vector addition
print("\nVector addition:\n")
print("v1:", v1.values,'shape:', v1.shape)
print("v3:", v3.values,'shape:', v3.shape)
try:  
    v5 = v1.__add__(v3)  
    print("v5 = v1 + v3 =", v5.values,'shape:', v5.shape)
except Exception as e:
    print(f"An error occurred during vector addition: {e}")


# Scalar multiplication
print("\nScalar multiplication:\n")
print("v1:", v1.values,'shape:', v1.shape)
try:
    v6 = v1.__mul__(2) 
    print("v6 = v1 x 2 =", v6.values,'shape:', v6.shape)
except Exception as e:
    print(f"An error occurred during scalar multiplication: {e}")


# Scalar division
print("\nScalar division:\n")
print("v1:", v1.values,'shape:', v1.shape)
try:
    v7 = v1.__truediv__(2)
    print("v7 = v1 / 2 =", v7.values,'shape:', v7.shape)
except Exception as e:
    print(f"An error occurred during scalar division: {e}")
'''
from vector import Vector

# Define two vectors
v1 = Vector([[1], [2], [3]], (3, 1))
v2 = Vector([[1, 2, 3]], (1, 3))

# Print the original vectors
print("Original vectors:\n")
print("v1:", v1.values, 'shape:', v1.shape)
print("v2:", v2.values, 'shape:', v2.shape)

try:
    # Transpose the vectors
    v1 = v1.T()
    v2 = v2.T()
except Exception as e:
    print(f"An error occurred during vector transposition: {e}")

# Print the transposed vectors
print("\nTransposed vectors:\n")
print("v1:", v1.values, 'shape:', v1.shape)
print("v2:", v2.values, 'shape:', v2.shape)


# Vector dot product
print("\nVector dot product:\n")
v3 = Vector([[4], [5], [6]], (3, 1))
print("v1:", v1.values, 'shape:', v1.shape)
print("v3:", v3.values, 'shape:', v3.shape)
try:
    v4 = v1.dot(v3)
    print("v4 = v1 ⋅ v3 =", v4)
except Exception as e:
    print(f"An error occurred during vector dot product: {e}")


# Vector addition
print("\nVector addition:\n")
print("v1:", v1.values, 'shape:', v1.shape)
print("v3:", v3.values, 'shape:', v3.shape)
try:  
    v5 = v1.__add__(v3.T())  
    print("v5 = v1 + v3 =", v5.values, 'shape:', v5.shape)
except Exception as e:
    print(f"An error occurred during vector addition: {e}")


# Scalar multiplication
print("\nScalar multiplication:\n")
print("v1:", v1.values, 'shape:', v1.shape)
try:
    v6 = v1.__mul__(2) 
    print("v6 = v1 x 2 =", v6.values, 'shape:', v6.shape)
except Exception as e:
    print(f"An error occurred during scalar multiplication: {e}")


# Scalar division
print("\nScalar division:\n")
print("v1:", v1.values, 'shape:', v1.shape)
try:
    v7 = v1.__truediv__(2)
    print("v7 = v1 / 2 =", v7.values, 'shape:', v7.shape)
except Exception as e:
    print(f"An error occurred during scalar division: {e}")
