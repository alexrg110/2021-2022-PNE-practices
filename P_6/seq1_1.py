class Seq:
    def valid_sequence(self):
        valid = True
        i = 0
        while i < len(self.strbases) and valid:
            c = self.strbases[i]
            if c != "A" and c != "C" and c != "G" and c != "T":
                valid = False
            i += 1
        return valid

    def __init__(self, strbases="NULL"):
        self.strbases = strbases
        if strbases == "NULL":
            print("NULL sequence created!")
        elif strbases == "ERROR":
            print("INCORRECT sequence detected!")
        else:
            print("New sequence created!")


    def __str__(self):
        return self.strbases

    def len(self):
        if self.strbases == "NULL" or self.strbases == "ERROR":
            return 0
        return len(self.strbases)

    def count_bases(self, base):
        if self.strbases == "NULL" or self.strbases == "ERROR":
            return 0
        return self.strbases.count(base)

    def count(self):
        gene_bases = ["A", "C", "T", "G"]
        dict_bases = {}
        for base in gene_bases:
            dict_bases[base] = self.count_bases(base)
        return dict_bases

    def reverse(self):
        if self.strbases == "NULL" or self.strbases == "ERROR":
            reverse_bases = self.strbases
            return reverse_bases
        else:
            reverse_bases = self.strbases[::-1]
            return reverse_bases

    def complement(self):
        base_complements = {"A": "T", "T": "A", "C": "G", "G": "C"}
        if self.strbases == "NULL" or self.strbases == "ERROR":
            complement = self.strbases
            return complement
        else:
            complement = ""
            for base in self.strbases:
                complement += base_complements[base]
            return complement

    def read_fasta(self, file_name):
        from pathlib import Path

        file_contents = Path(file_name).read_text()
        lines = file_contents.splitlines()
        body = lines[1:]
        self.strbases = ""
        for line in body:
            self.strbases += line

    def percentages(self):
        bases = self.count()

        for k in bases:
            bases[k] = round((bases[k] / self.len())*100, 2)

        return bases


    def common(self):
        bases = self.count()
        max_key = max(bases, key=bases.get)
        return max_key






