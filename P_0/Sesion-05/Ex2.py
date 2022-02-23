import seq0

FOLDER = "../Sesion-04/"


print(f"Dna file: {filename}")
sequence = seq0.seq_read_fasta(FOLDER + filename)
print("The first 20 bases are: ")
print(sequence[:20])