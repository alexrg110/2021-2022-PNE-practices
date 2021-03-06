from seq0 import*
FOLDER = "../Sesion-04/"
list_genes = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
list_bases = ["A", "C", "T", "G"]
for i in list_genes:
    filename = i + ".txt"
    sequence = seq_read_fasta(FOLDER + filename)
    print(f"Gene {i}: ")
    for base in list_bases:
        print(f"{base}: {seq_count_base(sequence, base)}")