import sys
import Tkinter
import tkFont
import random

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

class Canvas(Tkinter.Tk):
    def __init__(self):
        Tkinter.Tk.__init__(self)
        self.rysuj()
    def rysuj(self):
        self.cnvs = Tkinter.Canvas(self, width=500, height=500)#plotno na ktorym beda rysowane obrazki, musi byc rysowane w glownej petli
        self.cnvs.pack()#inicjuje rysowanie w.w.
    def line(self, x1, y1, x2, y2):
        self.cnvs.create_line(x1+22, y1+22, x2+22, y2+22)#robimy linie polaczen z punktu xy1 do xy2, od i do srodkow okregu
    def oval(self, x, y, color, num):#rysowanie okregow
        self.cnvs.create_oval(x, y, x+50, y+50, fill=color, width=0)#tutaj rysujemy kolko o wielosci 50, zasada rysowania podobna jak przy liniach
        self.cnvs.create_text(x+22, y+22, text=num, font=tkFont.Font(size=15, weight="bold"))#tutaj w kolku teskt, czy numer, obojetnie jak nazywa sie nasz wierzcholek w tablicy z lekkim przesunieciem, aby byl w srodku okregu
colors = ['red', 'green', 'yellow', 'blue', 'purple', 'grey', 'white', 'cyan']

def drawGraph(instance, w, k):
    #ustalam poczatkowe kordynaty
    x = 0
    y = 75
    crd = {}
    usdcls = {}#(usEdcOlORs) = uzyte kolory
    connections = {}
    #tutaj sprawdzamy wszystkie polaczenia miedzy wierzcholkami
    for pts, cons in k.items():
        for p in cons:
            if p not in connections:
                connections[p] = []
            connections[p].append(pts)
    #petla w ktorej sortujemy nowo utworzona tablice (tylko do ustalania kordynatow) oraz przypisujemy kolory do wierzcholkow
    for obj in sorted(connections, key=lambda v:len(connections[v]), reverse=True):#tutaj sorted z argumentem key, sortuje tablice z poleczeniami wg wielkosci podstablic, reverse odwraca, zeby byly ulozone malejaco
        x = x+100#przesuwamy sie do prawej
        if(x > 350): # zeby nam nie ucieklo w prawo poza ekran, ustalamy kiedy sie obnizamyna osi Y
            y = y + 100#obnizamy pozycje rysowania
            x = 100#wracamy do pozycji 'startowej' (w lewo), ale bedzie juz narysowana nizej
        bl = [] #blacklista kolorow, czyszczona co wierzcholek zeby dzialalo wg opisu 'Algorytm zachlanny' http://eduinf.waw.pl/inf/alg/001_search/0142.php
        for neigh in connections[obj]:#lecimy po polaczeniach w tablicy polaczen
            if neigh in usdcls:#jesli sasiad znajduje sie w liscie uzytych kolorow
                bl.append(usdcls[neigh])#dodajemy go na blackliste
        for c in colors:#spradzamy kazdy kolor
            if c not in bl:#gdy znalazl wolny kolor
                usdcls[obj] = c#przypisuje go co tablicy z zajetymi kolorami
                break#nie ma sensu dalej sprawdzac, bo juz mamy pierwszy wolny kolor
        crd[obj] = {'x':x+random.randrange(0,50), 'y':y+random.randrange(0,50)}#przypisujemy koordynady x,y + troche szumu aby pozbawic symetrii, dzieki czemu bedzie widac wszystkie linie
    for obj, pnts in k.items():#tutaj rysowanie linii, mamy tablice koordynatow wiec kolejnosc w tablicy nie ma znaczenia
        for p in pnts:
            instance.line(crd[obj]['x'], crd[obj]['y'], crd[p]['x'], crd[p]['y'])
    for obj in k:#tutaj rysowanie okregow i tesktu w nim, mamy tablice koordynatow wiec kolejnosc w tablicy nie ma znaczenia
        instance.oval(crd[obj]['x'], crd[obj]['y'], usdcls[obj], obj)
    print usdcls
    print colors
sasiedzi()
gui = Canvas()
gui.geometry("450x450")
gui.resizable(0,0)
drawGraph(gui, graf, VE) #zanim zaczniemy nieskonczona petle gui, odpalmay nasz generator grafow, zeby nam narysowal wszystkie potrzebne elementy
gui.mainloop()
