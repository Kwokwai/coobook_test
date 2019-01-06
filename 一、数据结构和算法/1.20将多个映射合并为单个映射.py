a = {'x':1, 'z':3}
b = {'y':2, 'z':4}

from collections import ChainMap
c = ChainMap(a, b)
print(c['x'])
print(c['y'])
print(c['z'])

print('*'*50)

print(len(c))
print(list(c.keys()))
print(list(c.values()))


print('-'*50)

c['z'] = 10
c['w'] = 40
del c['x']

print(a)

values = ChainMap()
values['x'] = 1
values = values.new_child()
values['x'] = 2
values = values.new_child()
values['x'] = 3

print('='*50)

print(values)

values = values.parents
print(values['x'])

values = values.parents
print(values['x'])

print(values)


a = {'x':1, 'z':3}
b = {'y':2, 'z':4}

merged = dict(b)
merged.update(a)

print('='*50)
print(merged['x'])
print(merged['y'])
print(merged['z'])