"""Solutions for the NumPy and SciPy questions shown in the exam image."""

import numpy as np
from scipy import integrate, optimize


def student_marks_analysis() -> None:
    marks = np.array(
        [
            [78, 65, 88],
            [92, 81, 95],
            [35, 60, 42],
            [66, 39, 70],
            [85, 90, 94],
        ]
    )

    print("Q1: Student marks analysis")
    print("Marks:\n", marks)
    print("Shape:", marks.shape)
    print("Dimensions:", marks.ndim)
    print("Total marks per student:", np.sum(marks, axis=1))
    print("Average marks per student:", np.mean(marks, axis=1))
    print("Subject-wise mean:", np.mean(marks, axis=0))
    print("Subject-wise maximum:", np.max(marks, axis=0))
    print("Subject-wise minimum:", np.min(marks, axis=0))

    passed = np.all(marks >= 40, axis=1)
    print("Passing students:", np.where(passed)[0] + 1)
    print("Failing students:", np.where(~passed)[0] + 1)

    averages = np.mean(marks, axis=1)
    top_students = np.where(averages > 80)[0] + 1
    print("Students with overall average above 80:", top_students)
    print()


def numpy_scipy_operations() -> None:
    # These two 2x2 matrices support addition, element-wise multiplication,
    # matrix multiplication, transpose, determinant, and inverse.
    a = np.array([[1, 2], [3, 4]], dtype=float)
    b_matrix = np.array([[5, 6], [7, 8]], dtype=float)

    print("Q2: NumPy and SciPy operations")
    print("A + B:\n", a + b_matrix)
    print("A * B (element-wise):\n", a * b_matrix)
    print("A @ B (matrix product):\n", a @ b_matrix)
    print("Transpose of A:\n", a.T)
    print("Determinant of A:", np.linalg.det(a))
    print("Inverse of A:\n", np.linalg.inv(a))

    rhs = np.array([9, 13], dtype=float)
    solution = np.linalg.solve(a, rhs)
    print("Solution of A x = b:", solution)
    print("Verification A @ x:", a @ solution)

    values = np.array([12, 15, 18, 21, 24], dtype=float)
    print("Mean:", np.mean(values))
    print("Median:", np.median(values))
    print("Population variance:", np.var(values))
    print("Population standard deviation:", np.std(values))

    integral, error = integrate.quad(lambda value: value**2, 0, 2)
    minimum = optimize.minimize_scalar(
        lambda value: (value - 3) ** 2 + 2,
        bounds=(0, 6),
        method="bounded",
    )
    print("Integral of x^2 from 0 to 2:", integral, "(error:", error, ")")
    print("Minimum of (x - 3)^2 + 2:", minimum.fun, "at x =", minimum.x)


if __name__ == "__main__":
    student_marks_analysis()
    numpy_scipy_operations()
