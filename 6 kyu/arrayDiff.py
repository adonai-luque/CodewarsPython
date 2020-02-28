def array_diff(a, b):
    #Searching for elements of b also in a
    for i in b:
        #Repeating removal of repeated elements
        for k in range(0, a.count(i)):
            a.remove(i)
    return a