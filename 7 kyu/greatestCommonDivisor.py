def mygcd(x, y):
    return (mygcd(y, x%y) if x%y != 0 else y) if y else (x if x else 0)

print(mygcd(18, 15))