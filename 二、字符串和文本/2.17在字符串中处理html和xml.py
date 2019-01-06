s = 'Elements are written as "<tag>text</tag>".'
import html
print(s)
print(html.escape(s))
print(html.escape(s, quote=False))

print('html'.center(50, '='))

s = 'Spicy Jalapeño'
print(s.encode('ascii', errors='xmlcharrefreplace'))

s = 'Spicy &quot;Jalape&#241;o&quot.'

from html.parser import HTMLParser

p = HTMLParser()
print(html.unescape(s))

from xml.sax.saxutils import unescape

t = 'The prompt is &gt;&gt;&gt;'
print(unescape(t))