# Problem 4(ii): Independent Two-Sample T-Test
# Compare two independent samples of marks to check if their means differ significantly.

from scipy import stats

marks1 = [12, 17, 16, 13, 19]
marks2 = [18, 17, 16, 20, 19]

t, p = stats.ttest_ind(marks1, marks2)
print("t-statistic:", t)
print("p-value:", p)

threshold = 0.05
if p < threshold:
    print("Result: Reject the null hypothesis ")
else:
    print("Result: Fail to reject the null hypothesis ")