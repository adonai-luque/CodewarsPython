"""def comp(array1, array2):
    if array1 == None or array2 == None:
        return False
    else:
        for n in array1:
            if (n*n) in array2:
                array2.remove(n*n)
        return len(array2) == 0"""

def comp(array1, array2):
    try:
        return sorted([n*n for n in array1]) == sorted(array2)
    except:
        return False

a = [-161, -144, -144, -121, -11, 19, 19, 19]
b = [121, 361, 361, 361, 14641, 20736, 20736, 25921]

print(comp(a, b))