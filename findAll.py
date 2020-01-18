def find_all(array, n):
    findings = []
    for i in range(0, len(array)):
        if array[i] == n:
            findings.append(i)
    return findings

print(find_all([6, 9, 3, 4, 3, 82, 11], 3))
