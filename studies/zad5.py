a = 68
b = 36
while b:
    a, b = b, a % b
    print(a)