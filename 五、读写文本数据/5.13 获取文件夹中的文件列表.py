import os

names = os.listdir('somedir')


import os.path

names = [name for name in os.listdir('somedir') if os.path.isfile(os.path.join('simedir', name))]

dirnames = [name for name in os.listdir('simedir') if os.path.isdir(os.path.join('somedir', name))]

pyfiles = [name for name in os.listdir('somedir') if name.endswith('.py')]


import glob

pyfiles = glob.glob('simedir/*.py')

from fnmatch import fnmatch


pyfiles = [name for name in os.listdir('somedir') if fnmatch(name, '*.py')]


import os
import os.path

import glob

name_sz_date = [(name, os.path.getsize(name), os.path.getmtime(name)) for name in pyfiles]

