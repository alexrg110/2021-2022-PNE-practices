import socket
import termcolor


PORT = 8080
IP = "localhost"
CONNECTIONS = 5

n = 0
clients = []

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
try:
    server_socket.bind((IP, PORT))
    server_socket.listen()

    while n != CONNECTIONS:
        print(f"Waiting for connections at ({IP}, {PORT}) .... ")
        (client_socket, address) = server_socket.accept()

        n += 1
        clients.append(address)

        print(f"CONNECTION: {n} from ({address})")

        request = client_socket.recv(2048).decode("utf-8")
        print(f"Message from client: ", end="")
        termcolor.cprint(request, "green")

        msg = f"ECHO: {request}\n"
        response_bytes = str.encode(msg)
        client_socket.send(response_bytes)

        client_socket.close()

    server_socket.close()

    print("The following clients has connected to the server:")
    for index, client in enumerate(clients):
        print(f"Client {index}: {client}")

except socket.error:
    print(f"Problems using port {PORT}. Do you have permission?")

except KeyboardInterrupt:
    print("Server stopped by the admin")
    server_socket.close()

