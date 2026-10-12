import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 10000)
print('Connecting to %s port %s' % server_address)
sock.connect(server_address)

try:
    message = 'This is the message, please repeat.'
    data_out = message.encode('utf-8')
    print('sending "%s"' % message)
    sock.sendall(data_out)

    amount_received = 0
    amount_expected = len(data_out)
    while amount_received < amount_expected:
        data = sock.recv(1600)
        if not data:
            break  # server closed the connection
        amount_received += len(data)
        print('received "%s"' % data.decode('utf-8'))

finally:
    print("closing client")
    sock.close()
