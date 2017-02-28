def zamiana():
    liczba = input("Podaj liczbę: ")
    liczba = int(liczba)
    slownie = ""
    a = {0 : "zero",
         1 : "jeden",
         2 : "dwa",
         3 : "trzy",
         4 : "cztery",
         5 : "piec",
         6 : "szesc",
         7 : "siedem",
         8 : "osiem",
         9 : "dziewiec"}

    while liczba > 1:
        koncowka = liczba%10
        liczba = liczba/10
        koncowka = int(koncowka)
        slownie = a[koncowka] + " " + slownie

    return(slownie)

print(zamiana())
