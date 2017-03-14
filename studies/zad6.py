data1 = [20, 11, 1993]
data2 = [20, 11, 1993]

pierwsza_data = data1[0]+data1[1]+data1[2]
druga_data = data2[0]+data2[1]+data2[2]

if data1 == data2:
    print("Daty są równe")
elif data1[2] > data2[2]:
    print("Pierwsza data jest większa od drugiej")
elif data1[2] < data2[2]:
    print("Druga data jest większa od pierwszej")
elif data1[2] > data2[1]:
    print("Pierwsza data jest większa od drugiej")
elif data1[0] > data2[0]:
    print("Pierwsza data jest większa od drugiej")
else:
    print("Druga data jest większa od pierwszej")