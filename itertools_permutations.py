# HakerRank challenge: itertools.permutations()

# Permutations means all orders by which elements can be arranged.
# itertools - is module which allows to do permutations in Python.
# The number of permutations = factorial of length(number of elements).
# For example we have 3 elements. 3! = 3x2x1 = 6 (total amount of permutations)

from itertools import permutations
string, k = input().split()
print(*[''.join(i) for i in permutations(sorted(string), int(k))], sep='\n')

# Print function comment
# *(asterick, call the sep argument at the end