'''Poniższy kod generuje listę 10 losowych liczb całkowitych z przedziału <0, 10).

from random import randint
l = [randint(0, 10) for x in range(10)]
Napisz pętlę, w której zostaną zliczone wystąpienia wszystkich liczb z listy, a następnie wyświetl na ekran pary: (liczba, liczebność).
'''
from random import randint
l = [randint(0, 10) for x in range(10)]
print(l)

for x in l:
    print("{}: {}".format(x,l.count(x)))