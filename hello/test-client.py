from client0 import Client
PRACTICE = 3
EXERCISE = 7
Gen_txt = ["ADA", "FRAT1", "FXN", "RNU6_269P", "U5"]
Bases_seq = "ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA"
Commands = ["PING", "GET", "INFO", "COMP", "REV", "GENE"]
print(f"-----| {PRACTICE}, {EXERCISE} |-----")

CLIENT_IP = "127.0.0.1"
CLIENT_PORT = 20500

c = Client(CLIENT_IP, CLIENT_PORT)
print(c)
for function in Commands:
    print(f"* Testing {function}...")
    if function == "PING":
          c.debug_talk(function)

    elif function == "GET":
        for n in range(5):
            c.debug_talk(f"{function} {str(n)}")

    elif function == "INFO":
        c.debug_talk(f"{function} {Bases_seq}")

    elif function == "COMP":
         c.debug_talk(f"{function} {Bases_seq}")

    elif function == "REV":
        c.debug_talk(f"{function} {Bases_seq}")

    elif

    elif function == "GENE":
        for file in Gen_txt:
            c.debug_talk(f"{function} {file}")