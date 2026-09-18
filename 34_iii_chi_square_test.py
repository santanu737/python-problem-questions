
# Problem 4(iii): Chi-Square Test
# Used to find out whether two categorical variables are associated or not,
# based on a contingency table of observed frequencies.
 
from scipy import stats
 
# Example contingency table (rows = category A, columns = category B)
data = [[10, 20, 30],
        [6, 9, 17]]
 
chi2, p, dof, expected = stats.chi2_contingency(data)
 

print(chi2)
print("p val",p)
print(dof)
print(expected)

threshold = 0.05
if p < threshold:
    print("Result: Reject the null hypothesis ")
else:
    print("Result: Fail to reject the null hypothesis ")
 