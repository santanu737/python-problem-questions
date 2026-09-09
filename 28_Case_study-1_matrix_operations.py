import numpy as np

# Define two 3x3 matrices using numpy arrays
A = np.array([
    [2, 1, 1],
    [1, 3, 2],
    [1, 0, 0]
])

B = np.array([
    [4, 2, 1],
    [3, 1, 5],
    [2, 6, 3]
])

print("Matrix A:\n", A)
print("\nMatrix B:\n", B)

# 1 - Find the inverse of matrix A
A_inv = np.linalg.inv(A)
print("\nInverse of Matrix A:\n", A_inv)

# 2 - Find the determinant of matrix B
det_B = np.linalg.det(B)
print("\nDeterminant of Matrix B:", det_B)

# 3 - Print the result of A x A_inverse (should give the identity matrix)
result = np.dot(A, A_inv)
print("\nA x A_inverse (should be the Identity matrix):\n", result)