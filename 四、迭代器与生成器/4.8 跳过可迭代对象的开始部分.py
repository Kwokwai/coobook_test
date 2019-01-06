from itertools import dropwhile, islice


with open('/etc/passwd') as f:
    for line in dropwhile(lambda line: line.startswith('#'), f):
        print(line, end='')


items = ['a', 'b', 'c', 1, 4, 10, 15]

for x in islice(items, 3, None):
    print(x)


with open('/etc/passwd') as f:
    while True:
        line = next(f, '')
        if not line.startswith('#'):
            break

    while line:
        print(line, end='')
        line = next(f, None)

with open('/etc/passwd') as f:
    lines = (line for line in f if not line.startswith('#'))
    for line in lines:
        print(line, end='')