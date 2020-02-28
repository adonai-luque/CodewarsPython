def polydivisible(x):
    return sum(int(str(x)[:i+1])%(i+1)==0 for i in range(len(str(x)))) == len(str(x))

print(polydivisible(153))
