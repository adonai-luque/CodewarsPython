def is_isogram(string):
    result = True
    string = string.lower()
    for c in string:
        if string.count(c) > 1:
            result = False
            break
    return result

print(is_isogram(""))