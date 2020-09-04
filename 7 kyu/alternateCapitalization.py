def capitalize(s):
    return [''.join(s[i] if i%2 == 1 else s[i].upper() for i in range(len(s))), ''.join(s[i] if i%2 == 0 else s[i].upper() for i in range(len(s)))]

s = 'abracadabra'
print(capitalize(s))