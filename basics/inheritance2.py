class Person():
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

class Employee(Person):
    def __init__(self, position):
        super().__init__("Tomek", "Chrzanowski", 56)
        self.position = position
        self.specialization = "drinks"

class Client(Person):
    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)
        self.ordered = "mojito"

pracownik = Employee("barman")

print(pracownik.name)
print(pracownik.position)

pracownik = Employee("deathbringer")

print(pracownik.name)
print(pracownik.position)

klient = Client("Jacek", "Gollob", 54)
print(klient.name)
print(klient.ordered)