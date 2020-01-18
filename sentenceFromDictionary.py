from itertools import permutations

dictio = ('a', 'b', 'ab')
s = 'abab'
listofdictios = list(permutations(dictio))

def extract(dictio, s):
    sentence = ''
    while s != '':
        for word in dictio:
            if s.find(word) == 0:
                sentence += ' ' + word
                s = s.replace(word, '', 1)
                break
    return sentence[1:]

sentences = []

for d in listofdictios:
    sentences.append(extract(d,s))

print(sentences)
