def euclides():
    a = 68
    b = 36
    while b:
        a, b = b, a % b
    return a
print(euclides())