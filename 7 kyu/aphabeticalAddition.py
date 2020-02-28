def add_letters(*letters):
    #Define a position for each letter in the alphabet
    ord_letters = [(ord(i) - 96) for i in letters]
    #Translate the sum of the positions into a number between 1 and 26 and then convert it into a letter
    return(chr(96 + (1 + (25 + sum(ord_letters)) % 26)))

print(add_letters('a', 'b', 'c'))