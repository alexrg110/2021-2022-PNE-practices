from Client1 import Client
PRACTICE = 3
EXERCISE = 7
GENES = ["ADA", "FRAT1", "FXN", "RNU6_269P", "U5"]
BASES = "ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA"
COMMANDS = ["PING", "GET", "INFO", "COMP", "REV", "LEN", "GENE", "OPE"]
print(f"-----| {PRACTICE}, {EXERCISE} |-----")

CLIENT_IP = "127.0.0.1"
CLIENT_PORT = 23400

c = Client(CLIENT_IP, CLIENT_PORT)
print(c)
for gene in COMMANDS:
    print(f"* Testing {gene}...")
    if gene == "PING":
          c.debug_talk(gene)

    elif gene == "GET":
        for n in range(5):
            c.debug_talk(f"{gene} {str(n)}")

    elif gene == "INFO":
        c.debug_talk(f"{gene} {BASES}")

    elif gene == "COMP":
         c.debug_talk(f"{gene} {BASES}")

    elif gene == "REV":
        c.debug_talk(f"{gene} {BASES}")

    elif gene == "GENE":
        for file in GENES:
            c.debug_talk(f"{gene} {file}")

    elif gene == "OPE":
        c.debug_talk(f"{gene} {BASES}")