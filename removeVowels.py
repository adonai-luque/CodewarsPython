"""
def remove_vowels(strng):
    vocals = 'aeiou'
    for v in vocals:
        strng = strng.replace(v, '')
    return strng
"""

def remove_vowels(strng):
    return strng.translate({ord('a'):None ,ord('e'):None, ord('i'):None, ord('o'):None, ord('u'):None})

print(remove_vowels('Drake'))