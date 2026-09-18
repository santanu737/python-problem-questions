# Problem 2: Cumulative Probability
# Use SciPy to calculate cumulative probability for a standard normal variate.
# Find the probability that the standard normal variate is less than 1.5.

from scipy import stats

p = stats.norm.cdf(1.5)
print("Cumulative probability (P(X < 1.5)):", p)