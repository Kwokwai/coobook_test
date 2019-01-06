prices = {
    'ACME': 45.23,
    'APPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}


min_price = min(zip(prices.values(), prices.keys()))
max_price = max(zip(prices.values(), prices.keys()))

print(min_price)
print(max_price)

prices_sorted = sorted(zip(prices.values(), prices.keys()))
print(prices_sorted)

# prices_and_name = zip(prices.values(), prices.keys())
# print(min(prices_and_name))
# print(max(prices_and_name))

print(min(prices))
print(max(prices))

print('-----------------------------------')

print(min(prices.values()))
print(max(prices.values()))


print('***********************************')

print(min(prices, key=lambda k: prices[k]))
print(max(prices, key=lambda k: prices[k]))