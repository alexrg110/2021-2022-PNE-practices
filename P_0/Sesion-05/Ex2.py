import seq0

FOLDER = "../Sesion-04/"

filename = input("Enter file's name: ")

print(f"Dna file: {filename}")
sequence = seq0.seq_read_fasta(FOLDER + filename)
print("The first 20 bases are: ")
print(sequence[:20])