class Seq:

    BASES = ["A", "C", "G", "T"]
    COMPLEMENTS = {"A": "T", "T": "A", "C": "G", "G": "C"}

    @staticmethod
    def validate_sequence(bases):
        valid = len(bases) != 0
        i = 0
        while valid and i < len(bases):
            if bases[i] in Seq.BASES:
                 i += 1
            else:
                valid = False
        return valid

    def __init__(self, bases="NULL"):
        if bases == "NULL":
            self.bases = bases
            print("NULL sequence created!")
        elif Seq.validate_sequence(bases):
            self.bases = bases
            print("New sequence created!")
        else:
            self.bases = "ERROR"
            print("INCORRECT sequence detected!")

    def __str__(self):
        return self.bases

    def seq_read_fasta(self, file_name):
        from pathlib import Path

        file_cont = Path(file_name).read_text()
        lines = file_cont.splitlines()
        body = lines[1:]
        self.bases = ""
        for line in body:
            self.bases += line

    def seq_len(self):
        if self.bases == "NULL" or self.bases == "ERROR":
            return 0
        return len(self.bases)

    def count(self, base):
        if self.bases == "NULL" or self.bases == "ERROR":
            return 0
        return self.bases.count(base)

    def base_count(self):
        total = {}
        for b in Seq.BASES:
            total[b] = self.count(b)
        return total

    def base_info(self):
        total = f"Sequence: {self.bases}\n"
        total += f"Total length: {self.seq_len()}\n"

        d = self.base_count()
        for base, count in d.items():
            total += f"{base}: {count} ({round((count * 100) / self.seq_len(),2)}%)\n"
        return total

    def seq_reverse(self):
        if self.bases == "NULL" or self.bases == "ERROR":
            return self.bases

        return self.bases[::-1]

    def seq_complement(self):
        if self.bases == "NULL" or self.bases == "ERROR":
            return self.bases

        total = ""
        for base in self.bases:
            total += Seq.COMPLEMENTS[base]
        return total