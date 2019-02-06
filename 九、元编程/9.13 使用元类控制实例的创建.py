# -*- encoding: utf-8 -*-


class Spam:
    def __init__(self, name):
        self.name = name


a = Spam('Kwok')
b = Spam('Kwong')


class NoInstance(type):
    def __call__(self, *args, **kwargs):
        raise TypeError("Can't instantiate directly")


class Spam(metaclass=NoInstance):
    @staticmethod
    def grok(x):
        print('Spam.Grok')

Spam.grok(42)


class Singleton(type):
    def __init__(self, *args, **kwargs):
        self.__instance = None
        super().__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        if self.__instance is None:
            self.__instance = super().__call__(*args, **kwargs)
            return self.__instance
        else:
            return self.__instance


class Spam1(metaclass=Singleton):
    def __init__(self):
        print('Creating Spam')


a = Spam1()

b = Spam1()

print(a is b)


import weakref


class Cached(type):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__cache = weakref.WeakValueDictionary()

    def __call__(self, *args):
        if args in self.__cache:
            return self.__cache[args]
        else:
            obj = super().__call__(*args)
            self.__cache[args] = obj
            return obj


class Spam2(metaclass=Cached):
    def __init__(self, name):
        print('Creating Spam({!r})'.format(name))
        self.name = name

c = Spam2('Kwok')

d = Spam2('kwong')

e = Spam2('kwok')

print(c is d)

print(c is e)