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
    droga = 1
    eu = 0
    while droga < len(graf):

        for path in sciezka(VE, graf[0], graf[droga]):
            continue
        droga +=1
#    sprawdzenie = set(path) & set(graf)
    if len(path) == len(graf):
        for k in VE.keys():
            if len(VE[k]) % 2 == 0 & len(VE[k]) != 0:
                eu += 1
            else:
                print("Graf nie jest eulerowski, ale jest spojny")
                sys.exit(0)
        if len(VE) == eu:
            print("Graf jest eulerowski i spojny")
    else:
        print("Graf nie jest spojny ani eulerowski")



sasiedzi()
stopnie()
euler()
'''graph ={ '1': ['2', '5'],
         '2': ['1', '3', '5'],
         '3': ['2','4'],
         '4': ['3','5','6'],
         '5': ['1','4','2'],
         '6': ['4']}'''