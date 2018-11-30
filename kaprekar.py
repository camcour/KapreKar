
def isKaprekar(nombre):
    ok = False
    sqr = str(x**2) #decimal representation
    for pos in range (1, len(sqr) - 1):
        part1 = int(sqr[:pos])
        part2 = int(sqr[pos:])
        if part1 + part2 == nombre:
            ok= True
    return ok
