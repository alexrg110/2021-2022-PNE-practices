import socket
import termcolor
from pathlib import Path

IP = "localhost"
PORT = 22000


def process_client(s):
    req_raw = s.recv(2000)
    req = req_raw.decode()

    print("Message FROM CLIENT: ")
    lines = req.splitlines()
    req_line = lines[0]
    slices = req_line.split(" ")  # slices = ["GET", "/directory/other/file.html", "HTTP/1.0"]
    method = slices[0]  # "GET"
    path = slices[1]  # "/directory/other/file.html"
    version = slices[2]  # "HTTP/1.0"
    print("Request line: ", end="")
    termcolor.cprint(req_line, 'green')

    # HTTP Response
    if path == "/info/A":
        body = Path("P_4/Sesion-13/A.html").read_text()
        status_line = "HTTP/1.1 200 OK\n"
        header = "Content-Type: text/html\n"
        header += f"Content-Length: {len(body)}\n"
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

