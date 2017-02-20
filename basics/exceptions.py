try:
    plik = open("text.txt", "r")
    plik.write("Hello")
    plik.close()
except FileNotFoundError as e:
    print("Plik nie istnieje")
    print(e)

except Exception as e:
    print(e)
    print("Nieznany błąd")