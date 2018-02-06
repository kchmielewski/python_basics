VE = {'1': ['2', '5'],
      '2': ['1', '3', '5'],
      '3': ['2','4'],
      '4': ['6'],
      '5': ['1','4','2'],
      '6': ['4']}
euler = 0
for k in VE.keys():
    if len(VE[k]) % 2 == 0 & len(VE[k]) != 0:
        euler += 1
        continue
if euler == len(VE):
    print("Graj jest Eulerowski")
else:
    print("Graf nie jest Eulerowski")


'''graph = {'A': ['B', 'C'],
         'B': ['C', 'D'],
         'C': ['D'],
         'D': ['C'],
         'E': ['F'],
         'F': ['C']}
def paths(graph, start, end):
    todo = [[start, [start]]]
    while 0 < len(todo):
        (node, path) = todo.pop(0)
        for next_node in graph[node]:
            if next_node in path:
                continue
            elif next_node == end:
                yield path + [next_node]
            else:
                todo.append([next_node, path + [next_node]])
for path in paths(graph, 'A', 'D'):
    print (path)'''









'''
graf = [1,2,3,4,5]
a = {key: [] for key in graf}
nrwierzch = 0
while nrwierzch < len(graf):
    sas = input("Podaj liczbe sasiadow wierzcholka")
    sas = int(sas)
    wierzcholek = []
    while sas > 0:
        sas -= 1
        wierzcholek = input("Podaj sasiada dla wierzcholka {}: ".format(graf[nrwierzch]))
        print(a[nrwierzch])
    nrwierzch+=1


for aa, bb in lw.items():
    bb.append(2)
    grr.update(bb)
a = "3"
kw = {}
for aa in lw.keys():
    if aa != a:
       kw = {a:aa}
       lw.update(kw)
    print ("Value : %s" % dict)'''
lista1=[]
lista2=[]
krok=0
if krok%2 == 0:
    lista1.append(krok)
    krok+=1
else:
    lista2.appent(krok)
    krok+=1