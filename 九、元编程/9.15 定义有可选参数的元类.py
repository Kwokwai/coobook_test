from abc import ABCMeta, abstractmethod


class IStream(metaclass=ABCMeta):
    @abstractmethod
    def read(self, maxsize=None):
        pass

    @abstractmethod
    def write(self, data):
        pass


class MyMeta(type):
    @classmethod
    def __prepare__(cls, name, bases, *, debug=False, synchronize=False):
        pass
        return super().__prepare__(name, bases)

    def __new__(cls, name, bases, ns, *, debug=False, synchronize=False):
        pass
        return super().__new__(cls, name, bases, ns)

    def __init__(self, name, bases, ns, *, debug=False, synchronize=False):
        pass
        super().__init__(name, bases, ns)


class Spam(metaclass=MyMeta, debug=True, synchronize=True):
    pass