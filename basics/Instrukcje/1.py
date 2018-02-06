'''Napisz skrypt w którym zdefiniujesz listę składającą się z liczb całkowitych i wyświetlisz pierwszy indeks równowagi.
 Jeśli lista nie ma indeksu równowagi, wyświetl stosowny komunikat.'''

A = [2,7,-4,5,3,-6,2,1]


x=0
y = 0
try:
    while y != ((sum(A))/2):
        y+= A[x]
        x+=1

    if y == ((sum(A))/2):
        print("Indeksem równowagi jest P = {}".format(x))
except IndexError:
    print("Nie ma indeksu równowagi")