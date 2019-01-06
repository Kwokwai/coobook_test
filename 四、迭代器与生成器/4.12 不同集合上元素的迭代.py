
from itertools import chain

a = [1, 2, 3, 4]
b = ['x', 'y', 'z']

for x in chain(a, b):
    print(x)


active_items = set()
inactive_items = set()

for item in chain(active_items, inactive_items):
    print(item)