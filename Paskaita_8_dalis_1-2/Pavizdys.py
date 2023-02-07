# objektinis
# Užduotis 1

# class Kate:
#     def __init__(self, spalva, kojos):
#         self.spalva = spalva
#         self.kojos = kojos

# kate1 = Kate("pilka", 4)
# kate2 = Kate("juoda", 3)

# # print(kate1.spalva)
# # print(kate2.kojos)

# kate2.kojos = 4
# print(kate1.kojos)
# print(kate2.kojos)


# class Kate:
#     def __init__(self, spalva, kojos):
#         self.spalva = spalva
#         self.kojos = kojos


#     def miaukseti(self):
#         print("Miau")
# kate1 = Kate("pilka", 4)
# kate1.miaukseti()

# class Zmogus:
#     def __init__(self,Vardas,Pavardė):
#         self.Vardas = Vardas
#         self.Pavardė = Pavardė

# zmogus1 = Zmogus("Jonas","Jonaitis")
# zmogus2 = Zmogus("Juozas","Juozaitis")
# print(zmogus1.Vardas,zmogus2.Pavardė)
# print(zmogus2.Vardas,zmogus1.Pavardė)

# class Kate:
#     def __init__(self, spalva, kojos):
#         self.spalva = spalva
#         self.kojos = kojos

#     def judinti_kojas(self):
#         pass

#     def ziureti_kur_begi(self) -> None:
#         None

#     def begti(self):
#         self.judinti_kojas()
#         self.ziureti_kur_begi()
#         print("Bėgu")
# muza = Kate("pilka", 4)
# muza.begti()

# class Kate:
#     def __init__(self, spalva = "juoda", kojos = 4):
#         self.spalva = spalva
#         self.kojos = kojos
# kate3 = Kate("pilka", 4)
# print(kate3.spalva, kate3.kojos)

# class Kate:
#     def __init__(self, spalva, kojos):
#         self.spalva = spalva
#         self.kojos = kojos

#     def miaukseti(self, zinute = "Miau", kiekis = 1):
#         return(zinute * kiekis)
# kate5 = Kate("Juoda", 4)

# print(kate5.miaukseti())

# print(kate5.miaukseti("Murrrr", 5))

# pasisveikinimas = "Sveikas, Pasauli"

# print(type(pasisveikinimas))
# print(id(pasisveikinimas))
# print(pasisveikinimas)
# print(pasisveikinimas.split())
# print(pasisveikinimas.upper())
# print(pasisveikinimas.lower())

# class Kate:
#     def __init__(self, spalva, kojos):
#         self.spalva = spalva
#         self.kojos = kojos


# kates = []

# kate1 = Kate("Juoda", 4)
# kate2 = Kate("Balta", 4)
# kate3 = Kate("Pilka", 4)

# kates.append(kate1)
# kates.append(kate2)
# kates.append(kate3)

# for kate in kates:
#     print(kate.spalva, kate.kojos)

class Kate:
    def __init__(self, vardas, amzius, spalva="juoda"):
        # Savybės:
        self.vardas = vardas
        self.amzius = amzius
        self.spalva = spalva

    # Metodas:
    def miaukseti(self, miauksejimas="Miau", kartai=1):
        print(miauksejimas * kartai)

    def __str__(self):
        return f"Katė vardu {self.vardas,}{self.amzius}{self.spalva}"

    def __repr__(self):
        return f"Katė vardu {self.vardas}{self.amzius}{self.spalva}"


kates = []

while True:
    pasirinkimas = int(input("Pasirinkite:\n1 - įvesti katę\n2 - peržiūrėti visas kates\n3 - išeiti iš programos\n"))
    if pasirinkimas == 1:
        vardas = input("Įveskite katės vardą")
        amzius = int(input("Įveskite katės amžių"))
        spalva = input("Įveskite katės spalvą")
        kate = Kate(vardas, amzius, spalva)
        kates.append(kate)
    if pasirinkimas == 2:
        for kate in kates:
            print(kate)
    if pasirinkimas == 3:
        print("Viso gero")
        break

    # In Python, __repr__ is a special method used to represent a 
    # class's objects as a string. __repr__ is called by the repr()
    # built-in function. You can define your own string representation
    # of your class objects using the __repr__ method. Special methods
    # are a set of predefined methods used to enrich your classes.