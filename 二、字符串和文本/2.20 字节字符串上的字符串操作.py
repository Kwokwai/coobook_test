data = b'Hello World'

print(data[0:5])

print(data.startswith(b'Hello'))

print(data.split())
print(data.replace(b'Hello', b'Hello Cruel'))

data = bytearray(b'Hello World')

print('001'.center(50, '='))

print(data[0:5])
print(data.startswith(b'Hello'))
print(data.split())

print(data.replace(b'Hello', b'Hello Cruel'))

data = b'FOO:BAR, SPAM'
import re
print(re.split(b'[:,]', data))

print('002'.center(50, '='))
a = 'Hello World'
print(a[0])
b = b'Hello World'
print(b[0])
print(b[1])


print('003'.center(50, '='))
s = b'Hello World'
print(s)
print(s.decode('ascii'))

print('{:10s} {:10d} {:10.2f}'.format('ACME', 100, 490.1).encode('ascii'))