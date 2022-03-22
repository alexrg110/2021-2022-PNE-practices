import socket

IP = "Localhost"
PORT = 8081

while True:
    msg = input(">> ")

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((IP, PORT))

    msg_bytes = str.encode(msg)
    client_socket.send(msg_bytes)

    client_socket.close()
