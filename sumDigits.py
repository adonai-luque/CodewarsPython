def sum_digits(number):
    digits = [int(n) for n in str(number) if n.isdigit()]
    return sum(digits)

print(sum(234))