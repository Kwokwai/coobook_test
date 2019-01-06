a = [1, 2, 3, 4]

for x in reversed(a):
    print(x)


class Countdown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1

    def __reversed__(self):
        n = 1
        while n <= self.start:
            yield n
            n += 1

for rr in reversed(Countdown(30)):
    print(rr)

print('001'.center(50, '='))

for rr in Countdown(30):
    print(rr)