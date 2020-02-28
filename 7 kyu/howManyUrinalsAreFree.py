def uncomfortableClose(s):
    if '11' in s:
        return True
    return False

def insertOne(s, i):
    return s[:i] + '1' + s[i+1:]

def get_free_urinals(urinals):
    initialCount = urinals.count('1')
    if uncomfortableClose(urinals):
        return -1
    else:
        for i in range(len(urinals)):
            if not uncomfortableClose(insertOne(urinals, i)):
                urinals = insertOne(urinals, i)
        return urinals.count('1') - initialCount



a = '1'
print(get_free_urinals(a))
