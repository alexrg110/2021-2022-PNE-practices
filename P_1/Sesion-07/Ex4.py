from seq1 import Seq

PRACTICE = 1
EXERCISE = 4
print(f"-----| Prcatice {PRACTICE}, Exercise {EXERCISE} |-----")
s1 = Seq()
s2 = Seq("ACTGA")
s3 = Seq("Invalid sequence")
print(f"Sequence 1: (Lenght: {s1.len()}) {s1}")
print(f"Sequence 2:  (Lenght: {s2.len()}) {s2}")
print(f"Sequence 2: (Lenght: {s3.len()}) {s3}")