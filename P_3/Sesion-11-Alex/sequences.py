class Seq:

    BASES_ALLOWED = ["A", "C", "G", "T"]
    BASES_COMPLEMENTS = {"A": "T", "T": "A", "C": "G", "G": "C"}

    @staticmethod #funcion o metodo que corresponde a toda la clase en general
    def valid_sequence(bases):
        valid = len(bases) != 0
        i = 0
        while valid and i < len(bases):
            if bases[i] in Seq.BASES_ALLOWED:
                 i += 1
            else:
                valid = False
        return valid

    def __init__(self, bases="NULL"):
        if bases == "NULL":
            self.bases = bases
            print("NULL sequence created!")
        elif Seq.valid_sequence(bases):
            self.bases = bases
            print("New sequence created!")
        else:
            self.bases = "ERROR"
            print("INCORRECT sequence detected!")

    def __str__(self):
        return self.bases

    def len(self):
        if self.bases == "NULL" or self.bases == "ERROR":
            return 0
        else:
            return len(self.bases)

    def count_bases(self, base):
        if self.bases == "NULL" or self.bases == "ERROR":
            return 0
        return self.bases.count(base)

    def count(self):
        result = {}
        for base in Seq.BASES_ALLOWED:
            result[base] = self.count_bases(base)
        return result

    def reverse(self):
        if self.bases == "NULL" or self.bases == "ERROR":
            return self.bases

        return self.bases[::-1]

    def complement(self):
        if self.bases == "NULL" or self.bases == "ERROR":
            return self.bases

        result = ""
        for base in self.bases:
            result += Seq.BASES_COMPLEMENTS[base]
        return result

    def read_fasta(self, file_name):
        from pathlib import Path

        file_contents = Path(file_name).read_text()
        lines = file_contents.splitlines()
        body = lines[1:]
        self.bases = ""
        for line in body:
            self.bases += line

    def info(self):
        result = f"Sequence: {self.bases}\n"
        result += f"Total lenght: {self.len()}\n"

        d = self.count()
        for base, count in d.items():
            result += f"{base}: {count} ({round((count * 100) / self.len(),2)}%)\n"
        return result

