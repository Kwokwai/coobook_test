from datetime import datetime


text = '2012-09-20'

y = datetime.strptime(text, '%Y-%m-%d')
z = datetime.now()

diff = z - y
print(diff)

print(z)

nice_z = datetime.strftime(z, '%A %B %d, %Y')
print(nice_z)


def parse_ymd(s):
    year_s, mon_s, day_s = s.spilt('-')
    return datetime(int(year_s), int(mon_s), int(day_s))

