import socket

# SERVER IP, PORT
SERVER_IP = "Localhost"
SERVER_PORT = 8081


# First, create the socket
# We will always use this parameters: AF_INET y SOCK_STREAM
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# establish the connection to the Server (IP, PORT)
s.connect((SERVER_IP, SERVER_PORT))

# Send data. No strings can be send, only bytes
# It necesary to encode the string into bytes
s.send(str.encode("HELLO FROM THE CLIENT!!!"))

# Receive data from the server
msg = s.recv(2048)
message = msg.decode("utf-8")
print(f"MESSAGE FROM THE SERVER: {message}")


# Closing the socket
s.close()