class Seq:

    BASES_ALLOWED = ["A", "C", "G", "T"] #propiedad o atributo de clase

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

    def __init__(self, bases):
        if Seq.valid_sequence(bases):
            self.bases = bases
            print("New sequence created!")
        else:
            self.bases = "ERROR"
            print("INCORRECT sequence detected!")

    def __str__(self):
        return self.bases

    def len(self):
        return len(self.bases)

class Gene(Seq):
    def __init__(self, bases, name="Null"):
        super().__init__(bases)
        self.name = name
        print("New gene created")

    def __str__(self):
        return  self.name + "-" + self.bases



