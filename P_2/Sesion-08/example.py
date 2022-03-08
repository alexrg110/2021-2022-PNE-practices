import socket

# Configure the Server's IP and PORT
PORT = 8081
IP = "Localhost"
MAX_OPEN_REQUESTS = 5

# Counting the number of connections
number_con = 0

# create an INET, STREAMing socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    server_socket.bind((IP, PORT))
    # become a server socket
    # MAX_OPEN_REQUESTS connect requests before refusing outside connections
    server_socket.listen(MAX_OPEN_REQUESTS)

    while True:
        # accept connections from outside
        print(f"Waiting for connections at ({IP}, {PORT}) .... ")
        (client_socket, address) = server_socket.accept()

        # Another connection!e
        number_con += 1

        # Print the conection number
        print(f"CONNECTION: {number_con} from ({address})")

        # Read the message from the client, if any
        msg = client_socket.recv(2048).decode("utf-8")
        print(f"Message from client: {msg}")

        # Send the message
        message = "Hello from the teacher's server"
        send_bytes = str.encode(message)
        # We must write bytes, not a string
        client_socket.send(send_bytes)
        client_socket.close()

except socket.error:
    print(f"Problems using port {PORT}. Do you have permission?")

except KeyboardInterrupt:
    print("Server stopped by the admin")
    server_socket.close()