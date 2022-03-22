from seq1 import Seq

PRACTICE = 1
EXERCISE = 5
print(f"-----| Prcatice {PRACTICE}, Exercise {EXERCISE} |-----")
seqs_list = [Seq(), Seq("ACTGA"), Seq("Invalid sequence")]
for index, seq in enumerate(seqs_list):
    print(f"Sequence {index}: (Lenght: {seq.len()}) {seq}")
    for base in Seq.BASES_ALLOWED:
        print(f"{base}: {seq.count_bases(base)}", end=" ")
    print()