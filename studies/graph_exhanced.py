import sys
lw = {}
wierzcholki = []
graf = []
wierzch = " "
il_sas = 0
V = int(input("Podaj liczbe wierzcholkow: "))
lwierzch = 0
sasiad = 0
while lwierzch < V:
    lwierzch += 1
    wierzch = input("Podaj nazwe wierzcholka : ")
    graf.append(wierzch)
VE = {key: [] for key in graf}

def za_duzo_sasiadow():
    if il_sas > V:
        sys.exit("Wpisales za duza liczbe sasiadow")
def blad():
    if sasiad == wierzch:
        sys.exit("Error: Podales bledne dane")
def sasiedzi():
    try:
        lwierzch = 0
        while lwierzch < V:
            lwierzch += 1
            wierzch = input("Podaj wierzcholek: ")
            il_sas = int(input("Podaj liczbe sasiadow tego wierzcholka: "))
            il_sas = il_sas - len(VE[wierzch])
            if il_sas > len(VE):
                sys.exit("Wpisales za duza liczbe sasiadow")
            while il_sas > 0:
                sasiad = input("Podaj wierzcholek z ktorym sasiaduje: ")
                il_sas -= 1
                if sasiad == wierzch:
                    sys.exit("Error: Podales bledne dane")
                if sasiad in VE[wierzch]:
                    continue
                else:
                    VE[wierzch].append(sasiad)
                if wierzch in VE[sasiad]:
                    continue
                else:
                    VE[sasiad].append(wierzch)
            print(VE)
    except KeyError:
        print("Podales dane nie pasujace do grafu")
def stopnie():
    maks = 0
    for aa, bb in VE.items():
        print ("Wierzcholek {} ma stopien: ".format(aa), len(bb))
        if maks < len(bb):
            maks = len(bb)
    print("Stopien grafu: {}".format(maks))

print(sasiedzi())
print(stopnie())