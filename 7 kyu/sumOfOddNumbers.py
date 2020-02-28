def row_sum_odd_numbers(n):
    return n**3

"""def row_sum_odd_numbers(n):
    row = [2*i-1 for i in range(int(0.5*n**2-0.5*n+1), int(0.5*n**2+0.5*n+1))]
    return sum(row)"""

print(row_sum_odd_numbers(8))
 