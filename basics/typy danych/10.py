'''Stwórz napis s = 'Dzień numer: ...'. W miejsce ... wstaw parametr, pod który zostanie podstawiona liczba całkowita.
 Jeżeli liczba składa się z mniej niż 3 cyfr uzupełnij brakujące miejsca zerami.'''
x = 10

if x<10:
    x = x*100
elif x<100:
    x = x*10

s = 'dzien numer: {}'.format(x)

print(s)