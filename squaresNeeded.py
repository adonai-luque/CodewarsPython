import math

def squares_needed(grains):
    return math.ceil(math.log(grains+1, 2))

print(squares_needed(8))