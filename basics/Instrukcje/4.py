'''Wczytaj napis, a następnie wyświetl na ekranie napis “short” jeżeli napis ma mniej niż 5 znaków,
 “medium” jeżeli ma od 5 do 10 znaków, “long” jeżeli ma więcej niż 10 znaków.
W rozwiązaniu tego zadania nie używaj operatora or.'''

napis = input("Podaj napis: ")

if len(napis)<5:
    print("short")
elif len(napis) >= 5 and len(napis) < 10:
    print("medium")
else:
    print("long")