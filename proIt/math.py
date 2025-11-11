# it is all about math
import math


def combinations(n, k):
    return math.comb(n, k)  # available in Python 3.8+


n = 10
k = 3
result = combinations(n, k)

print(f"Number of ways to choose {k} students from {n}: {result}")

# Number of ways to choose 3 students from 10: 120
Explanation:
    # We used math.comb(), which directly computes  C(n,k)
    # Alternatively, you could use factorials manually:
    # ------------------------------
