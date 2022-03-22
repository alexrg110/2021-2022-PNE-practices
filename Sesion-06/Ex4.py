import termcolor
from seq1 import Seq

def print_seqs(seq_list, color):
    for index, seq in enumerate(seq_list):
        termcolor.cprint(f"Sequence {index}: (Lenght: {seq.len()}) {seq}", color)

def generate_seqs(pattern, number):
    seq_list = []
    for n in range(1, number + 1):
        seq_list.append(Seq(pattern * n))
    return seq_list

seq_list1 = generate_seqs("A", 3)
seq_list2 = generate_seqs("AC", 5)

termcolor.cprint("List 1:", "blue")
print_seqs(seq_list1, "blue")

print()
termcolor.cprint("List 2:", "green")
print_seqs(seq_list2, "green")