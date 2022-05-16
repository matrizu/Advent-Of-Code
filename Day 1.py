def readFile(chemin):
    f = open(chemin, "r")
    data = f.read().splitlines()
    data = [ int(x) for x in data ]
    return data

def count(tab):
    previous = tab[0]
    nb = 0
    for k in range (1, len(tab)):
        if tab[k] > previous:
            nb += 1
            previous = tab[k]
        else:
            previous = tab[k]
    return nb
