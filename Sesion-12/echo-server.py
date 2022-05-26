import socket
import termcolor


# -- Server network parameters
IP = "Localhost"
PORT = 24500


def process_client(s):
    # -- Receive the request message
    req_raw = s.recv(2000)
    req = req_raw.decode()

    print("Message FROM CLIENT:")
    termcolor.cprint(req, "green")


# -------------- MAIN PROGRAM
# ------ Configure the server
# -- Listening socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# -- Setup up the socket's IP and PORT
ls.bind((IP, PORT))

# -- Become a listening socket
ls.listen()

print("SEQ Server configured!")

# --- MAIN LOOP
try:

    while True:
        print("Waiting for clients....")
        (cs, client_adress) = ls.accept()
        process_client(cs)

        cs.close()
except KeyboardInterrupt:
            print("Server Stopped!")
            ls.close()




