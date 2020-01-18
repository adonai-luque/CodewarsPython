def DNA_strand(dna):
    dna = dna.replace('A', 'B')
    dna = dna.replace('T', 'A')
    dna = dna.replace('B', 'T')
    dna = dna.replace('C', 'D')
    dna = dna.replace('G', 'C')
    dna = dna.replace('D', 'G')
    return dna

print(DNA_strand('TAACG'))

"""
pairs = {'A':'T','T':'A','C':'G','G':'C'}
def DNA_strand(dna):
    return ''.join([pairs[x] for x in dna])
"""