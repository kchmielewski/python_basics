'''Dana jest lista: l = [1, 5, 9, 4, 2, 7, 2, 4, 4, 0]

Wyświetl na ekran liczbę elementów listy.
Wyświetl na ekran ostatni element listy.
Odwróć kolejność elementów listy.
Wyświetl na ekran elementy od trzeciego do ostatniego.
Wyświetl na ekran co drugi element.
Wyświetl na ekran co drugi element zaczynając od końca.
Posortuj elementy listy.
Wczytaj trzy dowolne liczby i dołącz je do listy.
Zamień co drugi element listy na zera.
Zamień elementy list na napisy, a następnie stwórz napis, który będzie składał się z elementów listy oddzielonych przecinkami.'''

l = [1, 5, 9, 4, 2, 7, 2, 4, 4, 0]

print(len(l))
print(l[-1])
print(l[::-1])
print(l[3:10])
print(l[::-2])
print(l[::2])
print(sorted(l))
l.append(12)
l.append(13)
l.append(14)
for x in range(0,len(l),2):
    l[x]=0
print(l)
for y in range(0,len(l)):
    l[y]=str(l[y])



string=",".join(l)
print(string)