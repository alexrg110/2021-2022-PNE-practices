from Client0 import Client
from seq1 import Seq

PRACTICE = 2
EXERCISE = 4

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

SERVER_IP = "localhost"
SERVER_PORT = 8081
FOLDER = "./Genes/"

c = Client(SERVER_IP, SERVER_PORT)
genes_list = ["U5", "FRAT1", "ADA"]
for gen in genes_list:
    s = Seq()
    s.read_fasta(FOLDER + f"{gen}.txt")
    c.debug_talk(f"Sending {gen} Gene to the server...")
    c.debug_talk(str(s))

