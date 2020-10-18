a = ['abc', 'abc abc']

def word_values(a):

    def word_value(s):
        return sum(ord(c)-96 for c in s.replace(' ', ''))
    
    return [word_value(a[i])*(i+1) for i in range(len(a))]

print(word_values(a))
