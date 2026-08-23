"""
Program to calculate the sum of the series:
S = 1/1! + 4/2! + 9/3! + 16/4! + ... + n^2/n!
General term: i^2 / i!
"""

# import math

# def series(t):
#     i = 1
#     s = 0
#     while i <= t:
#         s += (math.pow(i, 2)) / math.factorial(i)
#         i += 1
#     print(f"Sum = {s}")

# series(5)




# OR 



import math

def seriesSum(n):
    s = 0
    for i in range(1, n + 1):
        s += (math.pow(i, 2)) / math.factorial(i)
    return s

print(seriesSum(5))
print(seriesSum(20))

