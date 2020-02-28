def seven(m):
    steps = 0
    d = m
    while True:
        if d < 100:
            break
        d = m//10 - 2*(m%10)
        steps += 1
        m = d
    return [d, steps]

print(seven(0))