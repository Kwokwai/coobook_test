import os

fd = os.open('somefile.txt', os.O_WRONLY | os.O_CREAT)

f = open(fd, 'wt')
f.write('hello world\n')
f.close()


from socket import socket, AF_INET, SOCK_STREAM


def echo_client(client_sock, addr):
    print('Got connection from', addr)

    client_in = open(client_sock.fileno(), 'rt', encoding='latin-1', closefd=False)

    client_out = open(client_sock.fileno(), 'wt', encoding='latin-1', closefd=False)

    for line in client_in:
        client_out.write(line)
        client_out.flush()

    client_sock.close()


def echo_server(address):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(address)
    socket.listen(1)
    while True:
        client, addr = sock.accept()
        echo_client(client, addr)


import sys
bstdout = open(sys.stdout.fileno(), 'wb', closed=False)
bstdout.write(b'Hello World\n')
bstdout.flush()