def solve(a):
    a.sort()
    n = len(a)
    m = sum(a) + 1
    b = [0]
    for i in range(n):
        b = b + [(n + a[i]) for n in b]
        b = list(set(b))
    for i in range(m):
        if i != b[i]:
            return i
    return (b[-1] + 1)