#def calculate(s):
#    return str(sum(int(n) for n in s.replace("minus", "plus-").split("plus")))

def calculate(s):
    acum = 0
    s = 'plus' + s + 'x'
    operation = ''
    
    while len(s) > 1:
        number = ''
        if s[0:4] == 'plus':
            for i in range(4, len(s)+1):
                if s[i].isdigit():
                    number += s[i]
                else:
                    s = s.replace(s[0:i],'',1)
                    break
            acum += int(number)
        elif s[0:5] == 'minus':
            for i in range(5, len(s)+1):
                if s[i].isdigit():
                    number += s[i]
                else:
                    s = s.replace(s[0:i],'',1)
                    break
            acum -= int(number)
    
    return str(acum)

cadena = '3plus8minus4plus9plus2minus3'
print(calculate(cadena))
print(cadena)