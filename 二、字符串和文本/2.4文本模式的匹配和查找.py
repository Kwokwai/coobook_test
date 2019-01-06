text = 'year, but no, but year, but no, but year'

print(text == 'year')


print(text.startswith('year'))
print(text.endswith('no'))

print(text.find('no'))

text1 = '11/27/2012'
text2 = 'Nov 27, 2012'

import re

print('='*50)

if re.match(r'\d+/\d+/\d+', text1):
    print('yes')
else:
    print('no')

if re.match(r'\d+/\d+/\d+', text2):
    print('yes')
else:
    print('no')


datepat = re.compile(r'd\d+/\d+/\d+')
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
print(datepat.findall(text))

