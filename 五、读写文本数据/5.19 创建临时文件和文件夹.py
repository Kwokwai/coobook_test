from tempfile import TemporaryFile


with TemporaryFile('w+t') as f:
    f.write('Hello World\n')
    f.write('Testing\n')

    f.seek(0)
    data = f.read()

    