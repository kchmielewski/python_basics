from math import factorial
def silnia(liczba):
#liczba = input("Podaj liczbe")
#liczba = int(liczba)
    a = 0
    wynik = factorial(liczba)
    razem = 0
    while wynik > 1:
        a += a
        koncowka = wynik % 10
        wynik = wynik / 10
        koncowka = int(koncowka)
        razem = format(koncowka) + " "
    print(razem)
silnia(4)