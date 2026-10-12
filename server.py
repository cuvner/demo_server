import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_address = ('localhost', 10000)
print('starting up on %s port %s' % server_address)
sock.bind(server_address)

sock.listen(1)

while True:
    print('Waiting for connection')
    connection, client_address = sock.accept()

    try:
        print('connection from', client_address)
        while True:
            data = connection.recv(1600)
            if data:
                msg = data.decode('utf-8')
                print('received "%s"' % msg)
                print("Sending data back to client")
                msg = msg + ' Plus extra from the server'
                connection.sendall(msg.encode('utf-8'))
            else:
                print('No more data from', client_address)
                break

    finally:
        connection.close()