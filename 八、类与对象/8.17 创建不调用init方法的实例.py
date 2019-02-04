

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day


d = Date.__new__(Date)

print(d)

date = {'year':2012, 'month':8, 'day':29}
for key, value in date.items():
    setattr(d, key, value)

print(d.year)

print(d.month)


from time import localtime


class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def today(cls):
        d = cls.__new__(cls)
        t = localtime()
        d.year = t.tm_year
        d.month = t.tm_mon
        d.day = t.tm_mday
        return d

