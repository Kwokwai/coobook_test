from datetime import datetime
from pytz import timezone


d = datetime(2012,12, 21, 9, 30, 0)

print(d)

central = timezone('US/Central')

loc_d = central.localize(d)
print(loc_d)

bang_d = loc_d.astimezone(timezone('Asia/Kolkata'))
print(bang_d)


d = datetime(2013, 3, 10, 1, 45)
loc_d = central.localize(d)
print(loc_d)

from datetime import timedelta
later = central.normalize(loc_d + timedelta(minutes=30))

print(later)