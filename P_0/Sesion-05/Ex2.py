from seq0 import *
FOLDER = "./Genes/"
try:
    name = input("Introduce filename: ")
    filename = name + ".txt"
    sequence = seq_read_fasta(FOLDER + filename)
    print(f"DNA file: {filename}")
    print(f"The first 20 bases are: {sequence[:20]}")
except FileNotFoundError:
    print(f"{filename} does not exist")
except IndexError:
    print(f"{filename} is empty")
