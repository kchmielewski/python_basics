import sys
V = int(input("Podaj liczbe wierzcholkow: "))
lwierzch = 0
lw = {}
wierzcholki = []
def blad():
    if sasiad == wierzch:
        sys.exit("Error: Podales bledne dane")
def za_duzo_sasiadow():
    if il_sas > V:
        sys.exit("Wpisales za duza liczbe sasiadow")
try:
    while lwierzch < V:
        lwierzch += 1
        wierzch = input("Podaj wierzcholek: ")
        il_sas = int(input("Podaj liczbe sasiadow tego wierzcholka: "))
        za_duzo_sasiadow()
        wierzcholki = []
        while il_sas > 0:
            il_sas -= 1
            sasiad = input("Podaj wierzcholek z ktorym sasiaduje: ")
            blad()
            wierzcholki.append(sasiad)
            lw[wierzch] = wierzcholki
    maks = 0
    for aa, bb in lw.items():
        print ("Wierzcholek {} ma stopien: ".format(aa), len(bb))
        if maks < len(bb):
            maks = len(bb)
    print("Stopien grafu: {}".format(maks))
except ValueError:
    print("Error: Lista wierzcholkow jest pusta, bo wprowadziles bledne dane")