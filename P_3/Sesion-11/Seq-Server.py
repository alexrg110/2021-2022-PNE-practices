import socket
import termcolor
import os
from sequence import *


PORT = 23400
IP = "127.0.0.1"
GEN_1 = "ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA"
GEN_2 = "AAAAACATTAATCTGTGGCCTTTCTTTGCCATTTCCAACTCTGCCACCTCCATCGAACGA"
GEN_3 = "CAAGGTCCCCTTCTTCCTTTCCATTCCCGTCAGCTTCATTTCCCTAATCTCCGTACAAAT"
GEN_4 = "CCCTAGCCTGACTCCCTTTCCTTTCCATCCTCACCAGACGCCCGCATGCCGGACCTCAAA"
GEN_5 = "AGCGCAAACGCTAAAAACCGGTTGAGTTGACGCACGGAGAGAAGGGGTGTGTGGGTGGGT"
GENES = [GEN_1, GEN_2, GEN_3, GEN_4, GEN_5]

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
try:
    server_socket.bind((IP, PORT))
    server_socket.listen()


    print("Seq-Server configured")
    while True:
            try:
                print(f"Waiting for client....")
                (client_socket, address) = server_socket.accept()

                request = client_socket.recv(2048).decode("utf-8")
                slices = request.split(" ")
                command = slices[0]
                termcolor.cprint(f"{command} command:", "green")
                response = " "
                if command == "PING":
                    response = f"OK!\n"
                    client_socket.send(response.encode())
                    print(response)

                elif command == "GET":
                    sequence_number = int(slices[1])
                    gene = GENES[sequence_number]

                    response = f"{gene}\n"
                    client_socket.send(response.encode())
                    print(response)

                elif command == "INFO":
                    bases = slices[1]
                    seq = Seq(bases)

                    response = f"{seq.info()}"
                    client_socket.send(response.encode())

                elif command == "COMP":
                    seq = slices[1]
                    s = Seq(seq)

                    response = f"{s.complement()}\n"
                    client_socket.send(response.encode())
                    print(response)

                elif command == "REV":
                    seq = slices[1]
                    s = Seq(seq)

                    response = f"{s.reverse()}\n"
                    client_socket.send(response.encode())
                    print(response)

                elif command == "GENE":
                    gene = slices[1]
                    seq = Seq()
                    file_name = os.path.join(".", "Genes", f"{gene}.txt")
                    seq.read_fasta(file_name)

                    response = f"{seq}\n"
                    client_socket.send(response.encode())
                    print(response)

                else:
                    response = "Invalid command"

            except Exception:
                response = f"ERROR: {command}\n"
                client_socket.send(response.encode())
                print(response)
                client_socket.close()
except socket.error:
        print(f"Problems using port {PORT}. Do you have permission?")

except KeyboardInterrupt:
        print("Server stopped by the admin")
        server_socket.close()

