from seq1 import Seq

PRACTICE = 1
EXERCISE = 9
FOLDER = "../Genes/"
file_name = input("Introduce filename: ")
print(f"-----| Prcatice {PRACTICE}, Exercise {EXERCISE} |-----")
s = Seq()
s.read_fasta(FOLDER + file_name)
print(f"Sequence: (Lenght: {s.len()}) {s}")
print(f"\tBases: {s.count()}")
print(f"\tRev: {s.reverse()}")
print(f"\tComp: {s.complement()}")