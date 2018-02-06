osoby = [{'nazwisko': 'Nowak', 'waga': 70,
          'ulubione_dania': ['schabowy', 'pomidorowa']},
         {'nazwisko': 'Kos',   'waga': 30,
          'ulubione_dania': ['lody', 'ciastka']},
         {'nazwisko': 'Szpak', 'waga': 40,
          'ulubione_dania': ['ryz', 'ogorkowa']},
         {'nazwisko': 'Kowalski', 'waga': 70,
          'ulubione_dania': ['schabowy', 'pomidorowa']},
         {'nazwisko': 'Konstantynopolitanczykiewicz', 'waga': 80,
          'ulubione_dania': ['frytki', 'ryba']},]
osobki = []
dania = []
k = 0
while k < len(osoby):
    osobki.append(osoby[k]['nazwisko'])
    dania.append(osoby[k]['ulubione_dania'][0])
    k += 1  
print sorted(osobki, reverse = True)
print sorted(osobki)
print sorted(osoby, reverse=True)
print sorted(osoby, reverse=False)
