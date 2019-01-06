

def bad_filename(filename):
    return repr(filename)[1:-1]


filename = ''
try:
    print(filename)
except UnicodeEncodeError:
    print(bad_filename(filename))


import os
files = os.listdir('.')

print(files)


