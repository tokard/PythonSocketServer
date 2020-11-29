import socket


def interaction(message, sock):
    sock.send(message.encode('utf-8'))
    response = sock.recv(2048).decode('utf-8')
    if response == 'EXIT':
        sock.close()
        return 0
    else:
        print(response)
        return 1


def client_conn():
    sock = socket.socket()
    sock.connect(('localhost', 8080))
    while True:
        if not interaction(input(), sock):
            break

client_conn()
