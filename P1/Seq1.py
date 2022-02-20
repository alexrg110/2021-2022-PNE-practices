class Seq:
    """ A class for representing sequences"""

    def __init__(self, strbases):
        #Initialize the sequence with the value
        # passed as argument when creating
        self.strbases = strbases
        if not self.valid_sequences():
            self.strbases = "ERROR"
            print("ERROR!!")
        else:
            print("New sequence created!")
