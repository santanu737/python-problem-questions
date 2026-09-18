# Problem 3: Standard Normal Interval
# Find out the interval of a standard normal distribution based on a given
# confidence level (e.g. 90%).

from scipy import stats

interval = stats.norm.interval(0.90)
print("90% interval of standard normal distribution:", interval)