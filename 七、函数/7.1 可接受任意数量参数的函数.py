

def avg(first, *rest):
    return (first + sum(rest) / (1 + len(rest)))


print(avg(1, 2))
print(avg(1, 2, 3, 4))


import html

def make_element(name, value, **attrs):
    keyvals = [' %s="%s' % item for item in attrs.items()]
    attr_str = ''.join(keyvals)
    elements = '<{name}{attrs}>{value}</{name}>'.format(
        name=name,
        attrs=attr_str,
        value=html.escape(value)
    )
    return elements


print(make_element('item', 'Albatross', size='large', quantity=6))
print(make_element('p', '<spam>'))