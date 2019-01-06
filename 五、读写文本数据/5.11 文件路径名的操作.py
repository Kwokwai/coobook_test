import os

path = '/Users/beazley/Data/data.csv'

os.path.basename(path)

os.path.dirname(path)

os.path.join('tmp', 'data', os.path.basename(path))

path = '~/Data/data.csv'

os.path.expanduser(path)

os.path.splitext(path)
