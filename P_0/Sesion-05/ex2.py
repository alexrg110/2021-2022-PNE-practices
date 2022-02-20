from P_0.sequences import seq0

filename = seq0.get_filename()
sequence = seq0.seq_read_fasta(filename)
print(sequence[:20])