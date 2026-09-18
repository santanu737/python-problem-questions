# Problem 4(i): One-Sample T-Test
# Perform a one-sample t-test on the given dataset against a population mean of 50.

from scipy import stats

marks = [18, 15, 12, 20, 19]
population_mean = 50

t, p = stats.ttest_1samp(marks, population_mean)
print("t-statistic:", t)
print("p-value:", p)

threshold = 0.05
if p < threshold:
    print("Result: Reject the null hypothesis .")
else:
    print("Result: Fail to reject the null hypothesis.")