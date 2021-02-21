from itertools import permutations

data = ['A', 'B', 'C']

# [('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'), ('C', 'A', 'B'), ('C', 'B', 'A')]
result = list(permutations(data, 3))
