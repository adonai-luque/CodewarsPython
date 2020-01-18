def get_sum(a,b):
    acum = 0
    men = min(a,b)
    may = max(a,b)
    while True:
        acum += men
        men += 1
        if men > may:
            break
    return acum

print(get_sum(-1, 2))

"""
def get_sum(a,b):
    return sum(range(min(a, b), max(a, b) + 1))
"""