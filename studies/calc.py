from math import sqrt
from math import factorial
class Calculator():
    def __init__(self):
        self.ostatni_wynik = 0

    def dodaj(self, a, b):
        wynik = a + b
        self.ostatni_wynik = wynik
        print(wynik)

    def odejmij(self, a, b):
        wynik = a - b
        self.ostatni_wynik = wynik
        print(wynik)

    def pomnoz(self, a, b):
        wynik = a * b
        self.ostatni_wynik = wynik
        print(wynik)

    def podziel(self, a, b):
        wynik = a / b
        self.ostatni_wynik = wynik
        print(wynik)

    def silnia(self,a):
        print(factorial(a))
    def funkcja_kwadratowa(self, a, b, c):
        d = b * b + 4 * a * c
        if d > 0:
            x1 = (-b - sqrt(d))/(2*a)
            x2 = (b - sqrt(d))/(2*a)
            print("Funkcja kwadratowa ma dwa rozwiązania: {} i {}".format(x1, x2))
        elif d == 0:
            x = (-sqrt(d)/(2*a))
            print("Funkcja kwadratowa ma jedno rozwiązanie: {}".format(x))
        else:
            print("Funkcja kwadratowa nie ma rozwiązań")



calc = Calculator()
calc.silnia(3)
calc.funkcja_kwadratowa(1, -4, 5)
print("Ostatni wynik Twoich obliczeń: {}".format(calc.ostatni_wynik))
