from functools import total_ordering


class Room:
    def __init__(self, name, lenght, width):
        self.name = name
        self.lenght = lenght
        self.width = width


@total_ordering
class House:
    def __init__(self, name, style):
        self.name = name
        self.style = style
        self.rooms = list()

    @property
    def living_space_footage(self):
        return sum(r.square_feet for r in self.rooms)

    def add_room(self):
        return '{}: {} square foot {}'.format(
            self.name,
            self.living_space_footage,
            self.style
        )

    def __str__(self):
        return '{}: {} square foot {}'.format(
            self.name,
            self.living_space_footage,
            self.style
        )

    def __eq__(self, other):
        return self.living_space_footage == other.living_space_footage

    def __lt__(self, other):
        return self.living_space_footage < other.living_space_footage


class House1:
    def __eq__(self, other):
        pass
    def __lt__(self, other):
        pass
    # Methods created by @total_ordering
    __le__ = lambda self, other: self < other or self == other
    __gt__ = lambda self, other: not (self < other or self == other)
    __ge__ = lambda self, other: not (self < other)
    __ne__ = lambda self, other: not self == other