def nb_year(p0, percent, aug, p):
    count = 0
    while p0 < p:
        p0 = p0 * (1 + percent/100) + aug
        count += 1
    return count

def nb_year(p0, percent, aug, p):
    return (1 + nb_year(int(p0*(1+percent/100))+aug, percent, aug, p)) if (p0 < p) else 0