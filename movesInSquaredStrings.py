def vert_mirror(strng):
    list = [s[len(s)::-1] for s in strng.split('\n')]
    return '\n'.join(list)
    
def hor_mirror(strng):
    list = strng.split('\n')
    list.reverse()
    return '\n'.join(list)
    

def oper(fct, s):
    return fct(s)
    

print(oper(vert_mirror, "ab\ncd\nde"))
print(hor_mirror("ab\ncd\nde"))