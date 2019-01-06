a = float('inf')
b = float('-inf')
c = float('nan')

print(a)
print(b)
print(c)

print('001'.center(50, '='))

import math
print(math.isinf(a))
print(math.isnan(c))


print(a + 45)
print(a * 10)
print(10 / a)

print('002'.center(50, '='))

print(a + b)

print(c + 23)
print(c / 2)
print(c * 2)

print(math.sqrt(c))

print('003'.center(50, '='))

d = float('nan')
print(c == d)

print(c is d)
