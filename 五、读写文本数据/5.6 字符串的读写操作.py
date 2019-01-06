import io


s = io.StringIO()

print(s.write('Hello World\n'))

print('This is a test', file=s)

print(s.getvalue())

s = io.StringIO('Hello\nWorld\n')

print(s.read(4))
print(s.read())
