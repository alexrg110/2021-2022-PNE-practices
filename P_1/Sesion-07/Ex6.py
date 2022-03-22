from seq1 import Seq

PRACTICE = 1
EXERCISE = 6
print(f"-----| Prcatice {PRACTICE}, Exercise {EXERCISE} |-----")
seqs_list = [Seq(), Seq("ACTGA"), Seq("Invalid sequence")]
for index, seq in enumerate(seqs_list):
    print(f"Sequence {index}: (Lenght: {seq.len()}) {seq}")
    print(f"\tBases: {seq.count()}")



