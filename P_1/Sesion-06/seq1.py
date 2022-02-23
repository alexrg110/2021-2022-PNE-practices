class Seq:
    def __init__(self, bases):
        self.bases = bases
        print("New sequence created!")

    def __str__(self):
        return self.bases

    def len(self):
        return len(self.bases)

class Gene(Seq):
    def __init__(self, bases, name=""):
        super().__init__(bases)
        self.name = name
        print("New gene created")


s = Seq("AGTACACTGGT")
g = Gene("CGTAAC")
print(f"Sequence 1: {s}")
print(f"  Length: {s.len()}")
print(f"Sequence 2: {g}")
print(f"  Length: {g.len()}")