

with open('somefile.txt', 'rt') as f:
    data = f.read()


with open('somefile.txt', 'rt') as f:
    for line in f:
        print(line)


with open('somefile.txt', 'wt') as f:
    f.write('1111')
    f.write('2222')


with open('somefile.txt', 'wt') as f:
    print('1111', file=f)
    print('2222', file=f)

