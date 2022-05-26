import socket
import termcolor
import os
from seq1 import *

PORT = 20500
IP = "127.0.0.1"
g_1 = "ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA"
g_2 = "AAAAACATTAATCTGTGGCCTTTCTTTGCCATTTCCAACTCTGCCACCTCCATCGAACGA"
g_3 = "CAAGGTCCCCTTCTTCCTTTCCATTCCCGTCAGCTTCATTTCCCTAATCTCCGTACAAAT"
g_4 = "CCCTAGCCTGACTCCCTTTCCTTTCCATCCTCACCAGACGCCCGCATGCCGGACCTCAAA"
g_5 = "AGCGCAAACGCTAAAAACCGGTTGAGTTGACGCACGGAGAGAAGGGGTGTGTGGGTGGGT"
g_list = [g_1, g_2, g_3, g_4, g_5]

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
try:
    server_socket.bind((IP, PORT))
    server_socket.listen()


    print("Server configured")
    while True:
            try:
                print(f"Waiting for client....")
                (client_socket, address) = server_socket.accept()

                request = client_socket.recv(2048).decode("utf-8")
                slices = request.split(" ")
                function = slices[0]
                termcolor.cprint(f"{function} command:", "yellow")
                response = " "
                if function == "PING":
                    response = f"OK!\n"
                    client_socket.send(response.encode())
                    print(response)

                elif function == "GET":
                    sequence_number = int(slices[1])
                    gene = g_list[sequence_number]

                    response = f"{gene}\n"
                    client_socket.send(response.encode())
                    print(response)

                elif function == "INFO":
                    bases = slices[1]
                    seq = Seq(bases)

                    response = f"{seq.base_info()}"
                    client_socket.send(response.encode())
                    print(response)

                elif function == "COMP":
                    seq = slices[1]
                    s = Seq(seq)

                    response = f"{s.seq_complement()}\n"
                    client_socket.send(response.encode())
                    print(response)

                elif function == "REV":
                    seq = slices[1]
                    s = Seq(seq)

                    response = f"{s.seq_reverse()}\n"
                    client_socket.send(response.encode())
                    print(response)

                elif function == "GENE":
                    gen = slices[1]
                    seq = Seq()
                    filename = os.path.join(".", "Genes", f"{gen}.txt")
                    seq.seq_read_fasta(filename)

                    response = f"{seq}\n"
                    client_socket.send(response.encode())
                    print(response)

                else:
                    response = "Invalid command"

            except Exception:
                response = f"ERROR: {function}\n"
                client_socket.send(response.encode())
                print(response)
                client_socket.close()
except socket.error:
        print(f"Problems using port {PORT}. Do you have permission?")

except KeyboardInterrupt:
        print("Server stopped by the admin")
        server_socket.close()