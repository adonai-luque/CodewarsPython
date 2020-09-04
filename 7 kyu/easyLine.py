def easyline(n):
    
    def listOfPairsAdded(l):
        return [(l[i] + l[i+1]) for i in range(0, len(l)-1)]

    def pascalLine(n):
        if n == 0:
            return [1]
        else:
            return [1] + listOfPairsAdded(pascalLine(n-1)) + [1]

    return sum(i**2 for i in pascalLine(n))


print(easyline(25))
