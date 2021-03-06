import pandas


rats = pandas.read_csv('rats.csv', skip_footer=1)
print(rats)

print(rats['Currenr Activity'].unque())


crew_dispatched = rats[rats['Current Activity'] ==' Dispatch Crew']

print(len(crew_dispatched))

print(crew_dispatched['ZIP Code'].value_counts()[:10])

dates = crew_dispatched.groupby('Completion Date')

print(len(dates))

date_counts = dates.size()
print(date_counts)

date_counts.sort()
print(date_counts[-10:])