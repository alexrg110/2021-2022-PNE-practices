def seq_ping():
    print("Ok")

def get_filename():
    exit = False
    while not exit:
        seq_name = input("Choose a file: ")
        folder = "../Sesion-04/"
        f = folder + seq_name
        try:
            filename = open(f, "r")
            exit = True
            return filename
        except FileNotFoundError:
            print("The filename does not exist.")

def seq_read_fasta(filename):
    seq = open(filename, "r").read()
    seq = seq[seq.find("\n"):].replace("\n", "")
    return seq

def seq_count_base(seq):
    count_a = 0
    count_c = 0
    count_g = 0
    count_t = 0
    for i in seq:
        if i == "A":
            count_a += 1
        elif i == "C":
            count_c += 1
        elif i == "G":
            count_g += 1
        elif i == "T":
            count_t += 1
    return count_a, count_c, count_g, count_t


def seq_count(seq):
    d = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
    for i in seq:
        d[i] += 1
    return d
