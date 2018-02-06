import sys
lw = {}
wierzcholki = []
graf = []
wierzch = " "
il_sas = 0
V = int(input("Podaj liczbe wierzcholkow: "))
lwierzch = 0
sasiad = 0
lista1 = []
lista2 = []
stop = 0
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
        while lwierzch+1 < V:
            lwierzch += 1
            wierzch = input("Podaj wierzcholek: ")
            il_sas = int(input("Podaj liczbe sasiadow tego wierzcholka: "))
            il_sas = il_sas - len(VE[wierzch])
            if il_sas > len(VE)-1:
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
        print("Podales dane niepasujace do grafu")
def stopnie():
    maks = 0
    for aa, bb in VE.items():
        print ("Wierzcholek {} ma stopien: ".format(aa), len(bb))
        if maks < len(bb):
            maks = len(bb)
    print("Stopien grafu: {}".format(maks))

def sciezka(VE, start, koniec):
    global droga
    droga = []
    robi = [[start, [start]]]
    while 0 < len(robi):
        (krok, path) = robi.pop(0)
        for nast_krok in VE[krok]:
            if nast_krok in path:
                continue
            elif nast_krok == koniec:
                yield path + [nast_krok]
            else:
                robi.append([nast_krok, path + [nast_krok]])


def euler():
    eu = 0
    droga = 0
    while droga < len(graf):
        global path
        for path in sciezka(VE, graf[0], graf[droga]):
            print(path)
            if len(path) %2 ==0:
                if graf[droga] in lista1 and graf[droga] in lista2:
                    lista2.remove(graf[droga])
                else:
                    if graf[droga] not in lista1:
                        lista1.append(graf[droga])
            else:
                if graf[droga] in lista2 and graf[droga] in lista1:
                    lista1.remove(graf[droga])
                else:
                    if graf[droga] not in lista2:
                        lista2.append(graf[droga])
            print(lista1,lista2)
        droga +=1
    if lista2 == []:
        lista1.append(graf[0])
    else:
        lista2.append(graf[0])
    if len(path) == len(graf):
        for k in VE.keys():
            if len(VE[k]) % 2 == 0 and len(VE[k]) != 0:
                eu += 1
            else:
                global stop
                stop = 1
                global wynik2
                wynik2=("Graf nie jest eulerowski, ale jest spojny")
    if len(VE) == eu:
        wynik2=("Graf jest eulerowski i spojny")
    else:
        wynik2=("Graf nie jest ani eulerowski ani spojny")
    print(wynik2)
def dwud():
    spr = 0
    if len(lista1) < 1:
        print("Graf nie jest dwudzielny")
        sys.exit(0)
    elif len(lista2) < 2:
        print("Graf nie jest dwudzielny")
        sys.exit(0)
    while spr < len(lista1):
        if lista1 is not []:
            dwudzielnosc = ""
            for e in VE[lista1[spr]]:
                if e not in lista1:
                    dwudzielnosc = "Graf jest dwudzielny: {}, {}".format(lista1,lista2)
                    spr = 100
                else:
                    dwudzielnosc = "Graf nie jest dwudzielny"
            print(dwudzielnosc)
        spr+=1




sasiedzi()
stopnie()
euler()
dwud()
'''graph ={ '1': ['2','4'],
         '2': ['1', '3', '5'],
         '3': ['2','4'],
         '4': ['1','3'],
         '5': ['2']}'''