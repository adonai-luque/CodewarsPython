def binary_gcd(x, y):
    return (binary_gcd(y, x%y) if x%y != 0 else str(bin(y)).count('1')) if y else (str(bin(x)).count('1') if x else 0)