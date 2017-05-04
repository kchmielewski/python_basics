a = {"baton": 2, "czipsy": 3, "sok": 2.50}
portfel = 100

def zakupy(l, p, *x):
    s = 0
    for k in x:
        s +=l[k]
        print (k)
        print(s)
    return (s, p-s)

print (zakupy(a, portfel, 'baton','sok','czipsy','baton','czipsy'))
'''b = ["baton","czipsy","sok"]
d = ["2zl", "3zl", "2,50zl"]
lista = []
c = {key: [] for key in b}
print(c)'''
