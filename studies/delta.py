from math import sqrt
a = input("Podaj a potrzebną do obliczenia funkcji kwadratowej: ")
b = input("Podaj b potrzebne do obliczenia funkcji kwadratowej: ")
c = input("Podaj c potrzebne do obliczenia funkcji kwadratowej: ")
a1 = int(a)
b1 = int(b)
c1 = int(c)
d = b1 * b1 + 4 * a1 * c1
if d > 0:
    x1 = (-b1 - sqrt(d))/(2*a1)
    x2 = (b1 - sqrt(d))/(2*a1)
    print("Funkcja kwadratowa ma dwa rozwiązania: {} i {}".format(x1, x2))
elif d == 0:
    x = (-sqrt(d)/(2*a1))
    print("Funkcja kwadratowa ma jedno rozwiązanie: {}".format(x))
else:
    print("Funkcja kwadratowa nie ma rozwiązań")