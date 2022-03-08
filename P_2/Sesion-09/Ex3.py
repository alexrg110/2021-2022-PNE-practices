from Client0 import Client

PRACTICE = 2
EXERCISE = 3

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

SERVER_IP = "localhost"
SERVER_PORT = 8080

c = Client(SERVER_IP, SERVER_PORT)

print("Sending a message to the server...")
response = Client.talk("Testing!!!")
print(f"Response: {response}")