map = '01000000X000X011X0X'
def pandemia(map):
    continents = map.split('X')
    for i in range(len(continents)):
        if '1' in continents[i]:
            continents[i] = continents[i].replace('0', '1')
    return 'X'.join(continents)
  
def percentage(map):
    return (100*map.count('1')/(map.count('0') + map.count('1'))) if (map.count('0') + map.count('1')) > 0 else 0

print(percentage(pandemia(map)))