'''Mirek ma n słoików na cukierki.
 Przez pewien czas Mirek wkładał do wybranych słoików cukierki.
  Każdą operację dodawania cukierków do słoików można opisać trzema liczbami całkowitymi: a, b, k,
   gdzie a i b to indeksy słoików, a k to liczba cukierków jaka została dodana do każdego słoika o indeksach z zakresu <a, b>.

Dana jest lista trójelementowych krotek (a, b, k) opisujących operacje dodawania cukierków do słoików:

l = [(1, 2, 100), (2, 5, 100), (3, 4, 100)]
oraz liczba słoików:

n = 5
Napisz kod, króry dla zadanej listy operacji l i liczby słoików n obliczy średnią liczbę cukierków dla n słoików po wykonaniu operacji z listy l.
 Wartość średniej zaokrąglij w dół do najbliższej liczby całkowitej.

Dla danych z zadania liczebność cukierków w słoikach będzie zmieniać się w następujący sposób:

  0   0   0   0   0
100 100   0   0   0
100 200 100 100 100
100 200 200 200 100
Po wykonaniu ostatniej operacji w słoikach będzie w sumie 800 cukierków. Średnio w jednym słoiku znajduje się 800/5 = 160 cukierków.
'''
sloiki = [1,2,3,4,5]
liczba = [0,0,0,0,0]
liczbas = dict(zip(sloiki,liczba))

l = [(1, 2, 100), (2, 5, 100), (3, 4, 100)]

for y in l:
    for x in range(y[0],y[1]+1):
        liczbas[x]+= y[2]
    print(liczbas)
    print(sum(liczbas.values())/len(sloiki))