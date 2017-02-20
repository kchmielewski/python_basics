
class Calculator():

    def __init__(self):
        print("init")

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
        print(wynik)

    def odejmij(self, a, b):
        wynik = a - b
        print(wynik)

calc = Calculator()
