my_list = ['a', 'b', 'c']

for idx, val in enumerate(my_list):
    print(idx, val)

for idx, val in enumerate(my_list, 1):
    print(idx, val)


def parse_data(filename):
    with open(filename, 'rt') as f:
        for lineno, line in enumerate(f, 1):
            fildes = line.split()
            try:
                count = int(fildes[1])
            except ValueError as e:
                print('Line {}: Parse error: {}'.format(lineno, e))


from collections import defaultdict
word_summary = defaultdict(list)

with open('myfile.txt', 'r') as f:
    lines = f.readlines()

for idx, line in enumerate(lines):
    words = [w.strip().lower() for w in line.split()]
    for word in words:
        word_summary[words].append(idx)