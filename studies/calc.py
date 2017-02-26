from math import sqrt
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


print("Ostatni wynik Twoich obliczeń: {}".format(calc.ostatni_wynik))