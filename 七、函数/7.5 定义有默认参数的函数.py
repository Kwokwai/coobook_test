

def spam(a, b=42):
    return a, b

print(spam(1))
print(spam(1, 2))


def spam(a, b=None):
    if b is None:
        b = []


_no_value = object()

def spam(a, b=_no_value):
    if b is _no_value:
        print('No b value supplied')


print(spam(1))
print(spam(1, 2))
print(spam(1, None))

print('001'.center(50, '='))

x = 42
def spam(a, b=x):
    return a, b


print(spam(1))

