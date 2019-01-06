filename = 'spam.txt'
print(filename.endswith('.txt'))

print(filename.startswith('file:'))

url = 'http://www.python.org'
url.startswith('http:')


import os
filenames = os.listdir('.')
print(filenames)

print([name for name in filenames if name.endswith('.py')])
print(any(name.endswith('.py') for name in filenames))


from urllib.request import urlopen


def read_data(name):
    if name.startswith(('http:', 'https:', 'ftp:')):
        return urlopen(name).read()
    else:
        with open(name) as f:
            return f.read()

choices = ['htpp:', 'ftp:']

url = 'http://www.python.org'
print(url.startswith(tuple(choices)))


