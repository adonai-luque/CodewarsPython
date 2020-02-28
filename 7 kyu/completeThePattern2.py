def pattern(n):
    return '\n'.join(''.join(str(i) for i in range(n,i-1, -1)) for i in range(1, n+1))

print(pattern(4))