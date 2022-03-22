BASES = ["A", "C", "T", "G"]
COMPLEMEMTS = {"A": "T", "T": "A", "C": "G", "G": "C"}
def seq_ping():
    print("Ok")

def seq_read_fasta(filename):
    seq = open(filename, "r").read()
    seq = seq[seq.find("\n"):].replace("\n", "")
    return seq

def seq_len(seq):
    return len(seq)

def seq_count_base(seq: str, base):
    return seq.count(base)

def seq_count(seq):
    d = {}
    for base in BASES:
        d[base] = seq_count_base(seq, base)
    return d

def seq_reverse(seq):
    return seq[::-1]#para dar la vuelta a una cadena de caracteres

def seq_complement(seq): # seq = "ATTCG"
    result = ""
    for base in seq:  # base = "A"
        result += COMPLEMEMTS[base]
    return result

def most_frequent_base(seq):
    d = seq_count(seq)
    max_base = None
    max_count = 0
    for base, count in d.items():
        if count >= max_count:
            max_base = base
            max_count = count
    return max_base


