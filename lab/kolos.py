print [] and {} or 3
print [1] and None or []
print not (0 and None or 3)


miesiace={'luty':28,'maj':31,'lipiec':31,'wrzesien':55,'listopad':20}
print [reduce(lambda x, y: x+y, miesiace.values())]
print miesiace.values()
miesiace['luty'] = 29
miesiace.pop('maj')

a = 1
while a < len(miesiace.keys()):
    for k in miesiace.keys():
        miesiace[k] = a
        a+=1
print miesiace

licz = [1, [2, 3], (4, 5)]
print licz[-2:]

a = [1]
b = [a]

b[0].append(2)
print a
print b


a = b = [1,2]
def f(x):
    a=x
    return a+b
def g(y):
    b=f(y)
    return a+b
print g(f(a))

print map(lambda x, y: x + y, range(7), range(7))
