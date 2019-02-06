import logging


a = logging.getLogger('foo')
b = logging.getLogger('bar')

print(a is b)

c = logging.getLogger('foo')

print(a is c)


# class Spam:
#     def __init__(self, name):
#         self.name = name
#
#
# import weakref
#
# _spam_cache = weakref.WeakKeyDictionary()
# def get_spam(name):
#     if name not in _spam_cache:
#         s = Spam(name)
#         _spam_cache[name] = s
#     else:
#         s = _spam_cache[name]
#     return s
#
#
# a = get_spam('foo')
# b = get_spam('bar')
#
# print(a is b)
#
# c = get_spam('foo')

# print(a is c)


import weakref

class CachedSpamManager:
    def __init__(self):
        self._cache = weakref.WeakKeyDictionary()

    def get_spam(self, name):
        if name not in self._cache:
            s = Spam1(name)
            self._cache[name] = s
        else:
            s = self._cache[name]
        return s

    def clear(self):
        self._cache.clear()


class Spam1:
    manager = CachedSpamManager()
    def __init__(self, name):
        self.name = name

    def get_spam(name):
        return Spam1.manager.get_spam(name)

a = Spam1('foo')
b = Spam1('foo')

print(a is b)