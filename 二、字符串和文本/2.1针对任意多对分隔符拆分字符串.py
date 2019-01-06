line = 'asdf fjdk; afed, fjek,asdf,    foo'
import re
print(re.split(r'[;,\s]\s*', line))


fields = re.split(r'(;|,|\s)\s*', line)
print(fields)

values = fields[::2]
delimiters = fields[1::2] + ['']
print(values)
print(delimiters)

print('*'*50)

print(''.join(v+d for v, d in zip(values, delimiters)))

print(re.split(r'(?:,|;|\s)\s*', line))