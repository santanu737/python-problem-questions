
# Problem 1: Descriptive Statistics
# Write a Python program using SciPy to calculate descriptive statistics
# (mean, mode, SD, and all features together) for a marks dataset of 10 students.

from scipy import stats

marks=[18,16,12,17,15,19,20,16,18,15]

res = stats.describe(marks)
print(res)

print("mean is",res.mean)
print("variance",res.variance)
