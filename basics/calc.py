
class Calculator():

    def __init__(self):
        self.ostatni_wynik = 0

    def __del__(self):
        print("del")

    def __str__(self):
        return "Hello"

    def __int__(self):
        return 10

    def __len__(self):
        return 5

    def __bool__(self):
        return True

    def dodaj(self, a, b):
        wynik = a + b
        self.ostatni_wynik = wynik
        print(wynik)

    def odejmij(self, a, b):
        wynik = a - b
        selg.ostatni_wynik = wynik
        print(wynik)

calc = Calculator()

calc.dodaj(5,3)
calc.dodaj(7,3)
calc.dodaj(8,3)

calc2 = Calculator()

calc2.dodaj(5,5)
calc2.dodaj(7,2)
calc2.dodaj(8,8)

print("Ostatni wynik Twoich obliczeń: {}".format(calc.ostatni_wynik))
print("Ostatni wynik Twoich obliczeń: {}".format(calc2.ostatni_wynik))