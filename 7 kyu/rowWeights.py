def row_weights(array):
    return (sum(array[::2]), sum(array[1::2]))

print(row_weights([1, 2, 3, 4]))