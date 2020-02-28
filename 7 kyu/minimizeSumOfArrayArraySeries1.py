def min_sum(arr):
    acum = 0
    while len(arr) > 0:
        acum += max(arr)*min(arr)
        arr.remove(max(arr))
        arr.remove(min(arr))
    return acum

print(min_sum([12, 6, 10, 26, 3, 24]))