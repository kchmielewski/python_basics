'''Dany jest słownik: d = {1: 'a', 2: 'b', 3: 'c'}

Wyświetl wszystkie klucze słownika.
Wyświetl wszystkie wartości słownika.
Wyświetl wszystkie pary (klucz, wartość) słownika.
Wczytaj liczbę jako klucz słownika i wyświetl odpowiadającą jej wartość, jeśli w słowniku nie ma takiego klucza wyświetl wartość 0.'''

d = {1: 'a', 2: 'b', 3: 'c'}
print(d.keys())
print(d.values())
print(d.items())
for x in range(1,5):
    try:

        print(d[x])
    except:
        print(0)