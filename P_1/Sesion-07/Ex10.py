from seq1 import Seq

PRACTICE = 1
EXERCISE = 10
print(f"-----| Prcatice {PRACTICE}, Exercise {EXERCISE} |-----")
FOLDER = "../Genes/"
GENES = ["RNU6_269P", "FRAT1", "U5", "ADA", "FXN"]

for gene in GENES:
    file_name = FOLDER + gene + ".txt"
    try:
        seq = Seq()
        seq.read_fasta(file_name)
        bases_appearances = seq.count()
        most_frequent = None
        for base, count in bases_appearances.items():
            if most_frequent:
                if count > most_frequent[1]:
                    most_frequent = (base, count)
            else:
                most_frequent = (base, count)
        print(f"Gene {gene}: {most_frequent[0]}")
    except FileNotFoundError:
        print(f"[ERROR]: file '{file_name}' not found")