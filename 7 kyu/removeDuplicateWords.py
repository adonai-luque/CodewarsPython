def remove_duplicate_words(s):
    newWordList = []
    for word in s.split(' '):
        if word not in newWordList:
            newWordList.append(word)
    return ' '.join(newWordList)


s = 'alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta'
print(remove_duplicate_words(s))