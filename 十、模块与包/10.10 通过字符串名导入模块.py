import importlib

math = importlib.import_module('math')
math.sin(2)

mod = importlib.import_module('urllib.request')
u = mod.urlopen("http://www.python.org")

