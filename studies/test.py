import sys
graf = ['1','2','3','4','5','6','7']
VE = {   '1': ['6'],
         '2': ['5', '7'],
         '3': ['5','6'],
         '4': ['6','7'],
         '5': ['2','3'],
         '6': ['1','3', '4'],
         '7': ['2','4']}
lista1=[]
lista2=[]
def sciezka(VE, start, koniec):
    eu = 0
    robi = [[start, [start]]]
    while 0 < len(robi):
        (krok, path) = robi.pop(0)
        for nast_krok in VE[krok]:

            if nast_krok in path:
                if len(path) == len(graf):
                    while skok != len(path):
                        if skok % 2 == 0:
                            lista1.append(path[skok])
                        else:
                            lista2.append(path[skok])
                    skok += 1
                    print(lista1,lista2)
                    for k in VE.keys():
                        if len(VE[k]) % 2 == 0 & len(VE[k]) != 0:
                            eu += 1
                        else:
                            sys.exit("Graf nie jest eulerowski, ale jest spojny")
                    if len(VE) == eu:
                        sys.exit("Graf jest eulerowski i spojny")
                continue
            elif nast_krok == koniec:
                yield path + [nast_krok]
            else:
                robi.append([nast_krok, path + [nast_krok]])
droga = 0
while droga < len(graf):
    for path in sciezka(VE, graf[0], graf[droga]):
        continue
    droga +=1
kolor=[]

'''kolor.extend(VE.keys())
huh = 0
while huh < len(graf):
    #if VE[graf[huh]]
    kolor.remove(graf[huh])
    print(kolor)
    huh+=1
'''