from collections import defaultdict


d = {}
paris = {}
for key, value in paris:
    if key not in d:
        d[key] = []
    d[key].append(value)


d = defaultdict(list)
for key, value in paris:
    d[key].append(value)