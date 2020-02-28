def powers(n):
    order = 0
    result = []
    while n > 0:
        if n % 2 == 1:
            result.append(2**order)
        n = n // 2
        order += 1
    return result

print(powers(10))