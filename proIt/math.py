# it is all about math
import math


def combinations(n, k):
    return math.comb(n, k)  # available in Python 3.8+


n = 10
k = 3
result = combinations(n, k)

print(f"Number of ways to choose {k} students from {n}: {result}")

# Number of ways to choose 3 students from 10: 120
# Explanation:
# We used math.comb(), which directly computes  C(n,k)
# Alternatively, you could use factorials manually:
# ------------------------------

# Here’s another small discrete math example — checking
# if a graph is connected.

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}


def is_connected(graph):
    visited = set()

    def dfs(node):
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                dfs(neighbor)

    # Start from any node
    start = next(iter(graph))
    dfs(start)

    return len(visited) == len(graph)


print("Graph connected:", is_connected(graph))

# -------------------------------------
# discrete math problem using sets and logic, and we’ll solve it in Python step-by-step.
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

union = A | B                  # A ∪ B
intersection = A & B           # A ∩ B
difference = A - B             # A − B
sym_diff = A ^ B               # A ⊕ B

print("A ∪ B =", union)
print("A ∩ B =", intersection)
print("A - B =", difference)
print("A ⊕ B =", sym_diff)
