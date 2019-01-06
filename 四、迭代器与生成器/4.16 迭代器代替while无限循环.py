CHUNKSIZE = 8192


def reader(s):
    while True:
        data = s.recv(CHUNKSIZE)
        if data == b'':
            break


def reader2(s):
    for chunk in iter(lambda: s.recv(CHUNKSIZE), b''):
        print(chunk)