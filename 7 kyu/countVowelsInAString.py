def count_vowels(s = ''):
    return sum(x in 'aeiouAEIOU' for x in s) if type(s) == str else None
