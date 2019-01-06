import json


data = {
    'name': 'ACME',
    'shares': 100,
    'price': 542.23
}
json_str = json.dumps(data)

print(type(json_str))


data = json.loads(json_str)

print(type(data))
