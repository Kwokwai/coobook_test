import collections
import bisect

class A(collections.Iterable):
    pass


class SortedItems(collections.Sequence):
    def __init__(self, initial=None):
        self._items = sorted(initial) if initial is not None else []

    def __getitem__(self, index):
        return self._items[index]

    def __len__(self):
        return len(self._items)

    def add(self, item):
        bisect.insort(self._items, item)


items = SortedItems([5, 1, 3])

print(list(items))
# print(items[0], items[-1])
#
# items.add(2)
#
# print(list(items))
