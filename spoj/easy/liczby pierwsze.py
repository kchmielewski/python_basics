'''Sprawdź, które spośród danych liczb są liczbami pierwszymi
Input
n - liczba testów n<100000, w kolejnych liniach n liczb z przedziału [1..10000]
Output
Dla każdej liczby słowo TAK, jeśli liczba ta jest pierwsza, słowo: NIE, w przeciwnym wypadku.
Example
Input:
3
11
1
4
Output:
TAK
NIE
NIE'''
n = 1
while n < 100000:
    if (n%1==0 and n%n==0 and (n%2!=0 and n%3!=0)):
        print("TAK")
    else:
        print("NIE")
    n += 1