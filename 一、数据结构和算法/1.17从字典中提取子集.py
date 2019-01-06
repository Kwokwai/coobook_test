prices = {
    'ACME': 45.23,
    'APPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

p1 = {key:value for key, value in prices.items() if value > 200}

teach_names = {'APPL', 'IBM', 'HPQ', 'MSFT'}
p2 = {key:value for key, value in prices.items() if key in teach_names}

p3 = dict((key, value) for key, value in prices.items() if value > 200)

p4 = {key:prices[key] for key in prices.keys() & teach_names}


print(p1)
print(p2)
print(p3)
print(p4)