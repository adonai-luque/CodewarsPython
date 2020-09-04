def consecutive_ducks(n):
    for i in range(2, int((n+1)/2)+1):
        if (2*n/i - i - 1)%2 == 0:
            return True
    return False