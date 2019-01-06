import random

values = [1, 2, 3, 4, 5, 6]

print(random.choices(values))
print(random.choices(values))
print(random.choices(values))
print(random.choices(values))

print('001'.center(50, '='))

print(random.sample(values, 2))
print(random.sample(values, 2))
print(random.sample(values, 2))
print(random.sample(values, 2))

print('002'.center(50, '='))

random.shuffle(values)
print(values)

print(random.randint(0, 10))
print(random.randint(0, 10))
print(random.randint(0, 10))
print(random.randint(0, 10))
print(random.randint(0, 10))

print('003'.center(50, '='))

print(random.random())
print(random.random())
print(random.random())
print(random.getrandbits(200))

print('004'.center(50, '='))

print(random.seed())
print(random.seed(12345))
print(random.seed(b'bytedata'))