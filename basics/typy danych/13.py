'''Wyświetl potęgi liczby 2 o wykładnikach od 2 do 5 korzystając z operatora przesunięcia bitowego.'''
'''Dane są dwa zbiory: s1 = {1, 2, 3, 4, 5}, s2 = {3, 4, 5, 6, 7}

Wyświetl sumę zbiorów.
Wyświetl różnicę zbiorów.
Wyświetl przecięcie zbiorów.
Dodaj do zbioru s1 liczbę 0.
Usuń ze zbioru s2 liczbę 3.'''

s1 = {1, 2, 3, 4, 5}
s2 = {3, 4, 5, 6, 7}

print(s1 | s2)
print(s1 & s2)
print(s1 ^ s2)

print(bin(0b1011 & 0b1010))