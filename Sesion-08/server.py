import socket
from colorama import Fore


PORT = 6123
IP = "localhost"
MAX_OPEN_REQUESTS = 5
number_con = 0
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    server_socket.bind((IP, PORT))

    server_socket.listen(MAX_OPEN_REQUESTS)

    while True:
        print(f"Waiting for connections at {IP}, {PORT} ")
        (client_socket, address) = server_socket.accept()

        number_con += 1

        print("CONNECTION: {}. From the IP: {}".format(number_con, address))


        msg = client_socket.recv(2048).decode("utf-8")
        print("Message from client: {}".format(Fore.LIGHTYELLOW_EX + msg))

        message = "Hello from the teacher's server"
        send_bytes = str.encode(Fore.LIGHTGREEN_EX + message)

        client_socket.send(send_bytes)
        client_socket.close()

except socket.error:
    print("Problems using port {}. Do you have permission?".format(PORT))

except KeyboardInterrupt:
    print("Server stopped by the user")
    server_socket.close()