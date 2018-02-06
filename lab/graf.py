V = int(input("Podaj liczbe wierzcholkow: "))
lwierzch = 0
lw = {}
wierzcholki = []
while lwierzch < V:
    lwierzch += 1
    wierzch = int(input("Podaj wierzcholek: "))
    il_sas = int(input("Podaj liczbe sasiadow tego wierzcholka: "))
    wierzcholki = []
    while il_sas > 0:
        il_sas -= 1
        sasiad = input("Podaj wierzcholek z ktorym sasiaduje: ")
        wierzcholki.append(sasiad)
        lw[wierzch] = wierzcholki

print (lw)
print len(max(list(lw.values())))