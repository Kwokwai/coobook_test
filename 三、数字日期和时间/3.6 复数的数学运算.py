a = complex(2, 4)
b = 3 - 5j
print(a)
print(b)

print(a.real)
print(a.imag)
print(a.conjugate())

print('001'.center(50, '='))

print(a + b)
print(a * b)
print(a / b)
print(abs(a))


print('002'.center(50, '='))

import cmath
print(cmath.sin(a))
print(cmath.cos(a))
print(cmath.exp(a))

print('003'.center(50, '='))

import numpy as np

a = np.array([2 + 3j, 4 + 5j, 6 - 7j, 8 + 9j])
print(a)

print(a + 2)
print(np.sin(a))

print(cmath.sqrt(-1))