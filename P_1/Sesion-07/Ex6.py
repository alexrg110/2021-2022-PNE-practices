from seq1 import Seq

print("-----| Exercise 6 |-----")
seqs_list = [Seq(), Seq("ACTGA"), Seq("Invalid sequence")]
for index, seq in enumerate(seqs_list):
    print(f"Sequence {index}: (Lenght: {seq.len()}) {seq}")
    print(f"\tBases: {seq.count()}")



