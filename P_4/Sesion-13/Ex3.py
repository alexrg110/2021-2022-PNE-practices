import socket
import termcolor
from pathlib import Path


IP = "localhost"
PORT = 22000


def process_client(client_socket):
    # HTTP Request
    request_bytes = client_socket.recv(2048)
    request = request_bytes.decode()

    print("Message FROM CLIENT:")

    lines = request.splitlines()
    request_line = lines[0]  # "GET /directory/other/file.html HTTP/1.0"
    slices = request_line.split(" ")  # slices = ["GET", "/directory/other/file.html", "HTTP/1.0"]
    method = slices[0]  # "GET"
    path = slices[1]  # "/directory/other/file.html"
    version = slices[2]  # "HTTP/1.0"
    print("Request line: ", end="")
    termcolor.cprint(request_line, 'green')

    body = ""
    if path == "/info/A":
            body = Path("P_4/Sesion-13/A.html").read_text()
    elif path == "/info/C":
            body = Path("P_4/Sesion-13/C.html").read_text()
    elif path == "/info/G":
            body = Path("P_4/Sesion-13/G.html").read_text()
    elif path == "/info/T":
            body = Path("P_4/Sesion-13/T.html").read_text()
    elif path == "/":
            body = Path("P_5/Sesion-15/index.html").read_text()
            status_line = "HTTP/1.1 200 OK\n"
    elif path.startswith("/info/"):  # path: /info/
        slices = path.split("/")  # slices: ["", "info", ""]
        resource = slices[2]
        try:
            body = Path(f"{resource}.html").read_text()
            status_line = "HTTP/1.1 200 OK\n"
        except FileNotFoundError:
            body = Path("P_5/Sesion-15/Error.html").read_text()
            status_line = "HTTP/1.1 404 NOT_FOUND\n"
    else:
        body = Path("P_5/Sesion-15/Error.html").read_text()
        status_line = "HTTP/1.1 404 NOT_FOUND\n"
    headers = "Content-Type: text/html\n"
    headers += f"Content-Length: {len(body)}\n"
    response = status_line + headers + "\n" + body
    response_bytes = response.encode()
    client_socket.send(response_bytes)


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind((IP, PORT))
server_socket.listen()

try:
    while True:
        print("Waiting for clients...")
        (client_socket, client_address) = server_socket.accept()
        process_client(client_socket)
        client_socket.close()
except KeyboardInterrupt:
    print("Server Stopped!")
    server_socket.close()

