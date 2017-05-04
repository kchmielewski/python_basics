lista = ['karol','lol','stasiek','wymiatacz','lololololol']
k = 0
max = 0
while k < len(lista):
    if max < len(lista[k]):
        max = len(lista[k])
        arg = lista[k]
    k += 1
print(arg)
print(max)

