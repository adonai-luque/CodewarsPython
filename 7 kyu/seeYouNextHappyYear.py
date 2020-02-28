def happy_year(year):
    return len(set(str(year))) == len(str(year))

def next_happy_year(year):
    return year+1 if happy_year(year+1) else next_happy_year(year+1)