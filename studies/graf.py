import sys
graf = ['1','2','3','4','5','6','7']
VE = {   '1': ['4'],
         '2': ['3','5'],
         '3': ['2','6'],
         '4': ['1','5','7'],
         '5': ['2','4'],
         '6': ['3','7'],
         '7': ['4','6']}
stop = 0
lista1=[]
lista2=[]
def sciezka(VE, start, koniec):
    eu = 0
    robi = [[start, [start]]]
    while 0 < len(robi):
        (krok, path) = robi.pop(0)
        for nast_krok in VE[krok]:
            global wynik2
            if nast_krok in path:
                if len(path) == len(graf):
                    for k in VE.keys():
                        if len(VE[k]) % 2 == 0 & len(VE[k]) != 0:
                            eu += 1
                        else:
                            global stop
                            stop = 1
                            wynik2=("Graf nie jest eulerowski, ale jest spojny")
                    if len(VE) == eu:
                        wynik2=("Graf jest eulerowski i spojny")

                else:
                    if stop == 1:
                        continue
                    else:
                        wynik2=("Graf nie jest ani eulerowski ani spojny")
            elif nast_krok == koniec:
                yield path + [nast_krok]
            else:
                robi.append([nast_krok, path + [nast_krok]])

skok = 0
droga = 0
while droga < len(graf):
    for path in sciezka(VE, graf[0], graf[droga]):

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

    droga +=1

if lista2 == []:
    lista1.append(graf[0])
else:
    lista2.append(graf[0])
spr = 0
while spr < len(lista1):
    for e in VE[lista1[spr]]:
        if e in lista1:
            dwudzielnosc = ("Graf nie jest dwudzielny")
            spr = 100
        else:
            dwudzielnosc = "Graf jest dwudzielny: {}, {}".format(lista1,lista2)
    spr+=1
#print(dwudzielnosc)
print(wynik2)
print(dwudzielnosc)