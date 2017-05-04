w1 = (1, 2, 3)
w2 = (4, 5, 6)

print ([w1[i] for i in range(len(w1))])
print ([w1[i] + w2[i] for i in range(len(w1))])

def skalar(a, b):
    s = 0
    for i in range(0, len(a)):
        s += a[i]*b[i]
    return s

print (skalar(w1, w2))