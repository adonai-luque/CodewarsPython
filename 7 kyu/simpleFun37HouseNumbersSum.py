def house_numbers_sum(inp):
    acum = 0
    for n in inp:
        if n == 0:
            break
        else:
            acum += n
    return acum
        
print(house_numbers_sum([1, 2, 3, 4, 0, 5, 6, 0, 7, 8, 0]))