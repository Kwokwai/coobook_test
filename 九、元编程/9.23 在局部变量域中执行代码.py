
# a = 13
# exec('b = a + 1')
# print(b)


# def test():
#     a = 13
#     exec('b = a + 1')
#     print(b)
#
# test()

def test():
    a = 13
    loc = locals()
    exec('b = a + 1')
    b = loc['b']
    print(b)

test()

def test1():
    x = 0
    exec('x += 1')
    print(x)

test1()

print('001'.center(50, '='))

def test2():
    x = 0
    loc = locals()
    print('before:', loc)
    exec('x += 1')
    print('after:', loc)
    print('x =', x)

test2()

print('002'.center(50, '='))

def test3():
    x = 0
    loc = locals()
    print(loc)
    exec('x += 1')
    print(loc)
    locals()
    print(loc)

test3()

print('003'.center(50, '='))

def test4():
    a = 13
    loc = {'a': a}
    glb = {}
    exec('b = a + 1', glb, loc)
    b = loc['b']
    print(b)

test4()
