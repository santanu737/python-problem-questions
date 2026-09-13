# note to myself (and anyone else running this) -
# first time i ran this it gave "ModuleNotFoundError: No module named scipy"
# turned out scipy was installed in my anaconda python not the normal one
# so if u get same error just run this in terminal first ->  pip install numpy scipy
# and make sure vs code is using the python where scipy is installed
# (ctrl+shift+p -> python: select interpreter -> pick the anaconda one if u have it)

import numpy as np
from scipy import linalg

# I. Solve: 2x+3y=8, 4x+5y=14
A1 = np.array([[2, 3], [4, 5]])
B1 = np.array([8, 14])
x, y = linalg.solve(A1, B1)
print("I. x =", x, " y =", y)

# II. Two cars: same direction meet in 11 hrs, opposite direction meet in 1 hr find out velocity of both cars
D = 200  # assumed distance between P and Q (km)
A2 = np.array([[1, -1], [1, 1]])
B2 = np.array([D / 11, D])
s1, s2 = linalg.solve(A2, B2)
print("II. Speed1 =", round(s1, 2), " Speed2 =", round(s2, 2))

# III. 4x4 matrix -> transpose and rank
M1 = np.array([[4, 2, 7, 1], [3, 6, 5, 8], [9, 1, 2, 4], [0, 5, 3, 7]])
print("III. Transpose:\n", M1.T)
print("     Rank:", np.linalg.matrix_rank(M1))

# IV. Square matrix -> eigenvalues/eigenvectors + PLU decomposition
M2 = np.array([[4, 1, 2, 0], [1, 3, 0, 1], [2, 0, 5, 1], [0, 1, 1, 2]])
eigvals, eigvecs = linalg.eig(M2)
P, L, U = linalg.lu(M2)
print("IV. Eigenvalues:", eigvals.real)
print("    Eigenvectors:\n", eigvecs)
print("    P:\n", P, "\n    L:\n", L, "\n    U:\n", U)

# V. Square matrix -> QR, SVD, lstsq
M3 = np.array([[2, 1, 1], [1, 3, 2], [1, 0, 4]])
Q, R = linalg.qr(M3)
Us, S, Vt = linalg.svd(M3)
b = np.array([5, 10, 8])
sol, res, rank, sv = linalg.lstsq(M3, b)
print("V. QR -> Q:\n", Q, "\n   R:\n", R)
print("   SVD -> U:\n", Us, "\n   S:", S, "\n   Vt:\n", Vt)
print("   lstsq solution:", sol)