from seq1 import Seq

print("-----| Exercise 5 |-----")
seqs_list = [Seq(), Seq("ACTGA"), Seq("Invalid sequence")]
for index, seq in enumerate(seqs_list):
    print(f"Sequence {index}: (Lenght: {seq.len()}) {seq}")
    for base in Seq.BASES_ALLOWED:
        print(f"{base}: {seq.count_bases(base)}", end=" ")
    print()