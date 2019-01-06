items = ['a', 'b', 'c']

from itertools import permutations, combinations, combinations_with_replacement


for p in permutations(items):
    print(p)

print('001'.center(50, '='))


for p in permutations(items, 2):
    print(p)


for c in combinations(items, 3):
    print(c)


for c in combinations(items, 2):
    print(c)

for c in combinations(items, 1):
    print(c)

for c in combinations_with_replacement(items, 3):
    print(c)