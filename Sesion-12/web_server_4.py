import socket
import termcolor
from pathlib import Path


# -- Server network parameters
IP = "localhost"
PORT = 22000


def process_client(s):
    # -- Receive the request message
    req_raw = s.recv(2000)
    req = req_raw.decode()

    print("Message FROM CLIENT: ")

    # -- Split the request messages into lines
    lines = req.splitlines()

    # -- The request line is the first
    req_line = lines[0]
    slices = req_line.split(" ")
    method = slices[0]
    path = slices[1]
    version = slices[2]

    print("Request line: ", end="")
    termcolor.cprint(req_line, "green")

    #HTTP response
    body = Path("index.html").read_text()
    status_line = "HTTP/1.1 200 OK\n"
    header = "Content_Type: text/html\n"
    header += f"Content_Lenght: {len(body)}\n"
    response = status_line + header + "\n" + body
    response_bytes = response.encode()
    cs.send(response_bytes)


ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

ls.bind((IP, PORT))
ls.listen()

print("SEQ Server configured!")

# --- MAIN LOOP
try:
    while True:
        print("Waiting for clients...")
        (cs, client_address) = ls.accept()
        process_client(cs)
        cs.close()
except KeyboardInterrupt:
    print("Server Stopped!")
    ls.close()
