from seq0 import*
FOLDER = "../Sesion-04/"
list_genes = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]

for i in list_genes:
    filename = i + ".txt"
    sequence = seq_read_fasta(FOLDER + filename)
    print(f"Gene {i}:")
    frag = sequence[:20]
    print(f"Frag: {sequence[:20]}")
    print(f"Rev: {seq_reverse(frag)}")
