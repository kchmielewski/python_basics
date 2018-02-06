'''
Poniższy kod generuje listę l 4 unikalnych losowych liczb całkowitych z przedziału <0, 5).

import random
l = random.sample(range(5), 4)
Napisz jednolinijkowy kod, za pomocą którego wyświetlisz na ekran napis “big number” jeżeli suma liczb w liście jest większa niż 6,
w przeciwnym razie wyświetl na ekran napis “small number”.
Skorzystaj z operatora trójargumentowego.'''

import random
l = random.sample(range(5), 4)
print(l)
print("big number" if sum(l)>6 else "small number")

