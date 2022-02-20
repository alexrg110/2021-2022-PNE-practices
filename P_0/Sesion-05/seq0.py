def seq_ping():
    print("Ok")

def get_filename():
    exit = False
    while not exit:
        filename = input("Enter filename: ")
        try:
            seq = open(filename, "r")
            exit = True
            return filename
        except FileNotFoundError:
            print("File does not exit. Provide another file.")

def seq_read_fasta(filename):
    seq = open(filename, "r").read()
    seq = seq[seq.find("\n"):].replace("\n", "")
    return seq

def seq_count_base():
    list_letters = ["A", "C", "T", "G"]
    count_a = 0
    count_g = 0
    count_t = 0
    count_c = 0
    for i in seq:
        if i == list_letters[0]:
            count_a += 1
        elif i == list_letters[1]:
            count_c += 1
        elif i == list_letters[2]:
            count_t += 1
        elif i == list_letters[3]:
            count_g += 1
    return count_a, count_c, count_t, count_g

def seq_count():
    d = {'A': 0, 'T': 0, 'C': 0, 'G': 0}




