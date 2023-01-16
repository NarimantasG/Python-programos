# zodziai=["Labas","vakaras","Lietuva"]
# print(zodziai[0])
# print(zodziai[2])

# zodis='Laba diena'
# print=(zodis[5])

# visko_po_truputi = [5, 5.6, "Lietuva", [5, 6, 15], True]
# print(visko_po_truputi[3][1])

# sarasas=[5, 2, 6]
# sarasas.append(13)
# print(sarasas)

# sarasas = [5, 2, 6]
# sarasas[1] = 64
# print(sarasas)

# sarasas = [6, 98, 159, "zodziai", 5.55, True]
# print(len(sarasas))

# ilgiausias_zodis = "nebeprisikiškiakopūsteliaujantiesiems"
# print(len(ilgiausias_zodis))

# pats_ilgiausias_zodis = "Nebeprisivaizdotinklaraštininkaujantiesiems"
# print(len(pats_ilgiausias_zodis))

# amzius = {"Rokas": 20, "Andrius": 34, "Laura": 25}
# #print(amzius)
# # print(amzius["Laura"])
# print(amzius["Rokas"])

# automobilis = {"Gamintojas": "Tesla", "Modelis": "Model S P100D", "Metai": 2016}
# # automobilis["Galia"]=500
# # automobilis["Vienas Sąvininkas"]="Vienas_pensininkas"
# # automobilis["Metai"]=2021
# del automobilis["Metai"]
# print(automobilis)

# automobilis={'gamintojas':'Subaru','Modelis':'Outback','Metai':'2000','Savininkas':'Vienas'}
# automobilis["Kaina"]=3000
# del automobilis['Savininkas']
# print(automobilis)

# sarasas={'Gamintojas':'Wolksvagen','Modelis':'Golf','Metai':'2000'}
# sarasas['Metai']=2015
# del sarasas['Gamintojas']
# sarasas['Savininkas']='Vienas'
# #sarasas.clear()                
# print(sarasas)

# list=(5,9,8)
# x=list.index(8)
# print(x)

# sarasas=(5,9,8,6,)
# xz=sarasas.count(6)
# print(xz)

# stuff=['something','nice','and']
# stuff.insert(3,'warm')
# print(stuff)


# suma = 0

# while True:
#     skaicius = int(input("Įveskite skaičių: "))
#     if skaicius < 0:
#         break
#     suma += skaicius

# print(suma)

# zodziai = []

# while True:
#     ivedimas = (input("Įveskite žodį: "))
#     if ivedimas == "":
#         break
#     zodziai.append(ivedimas)

# for numeris, zodis in enumerate(zodziai):
#     print(f"{numeris + 1}: {zodis}, simbolių kiekis: {len(zodis)}")
# print("Žodžių kiekis:", len(zodziai))



# Kauliukai


# from random import randint
# list=[]
# i=0
# while i!=3:
#     list.append(randint(1,6))
#     i=i+1

# print(list)
# if 5 in list: 
#     print('pralaimėjai')
# else:
#     print('Laimėjai')




# Sukurti norimą sąrašą ir žodyną ir juose:

# Atspausdinti vieną norimą įrašą
# Pridėti įrašą
# Ištrinti įrašą
# pakeisti įrašą
# Išbandyti kitas sąrašų ir žodynų funkcijas: clear(), index(), insert(), remove...

# https://www.w3schools.com/python/python_ref_list.asp https://www.w3schools.com/python/python_ref_dictionary.asp
# 2 užduotis
# Parašyti programą, kuri:

# Leistų vartotojui įvesti skaičių.
# Jei įvestas skaičius yra teigiamas, paprašyti įvesti dar vieną skaičių
# Jei įvestas skaičius neigiamas, nutraukti programą ir atspausdinti visų įvestų teigiamų skaičių sumą
# Patarimas: Naudoti ciklą while, sąlygą if, break

# Patarimas: Naudoti sąrašą (list), ciklą for, funkcijas len ir index

# 3 užduotis
# Sukurti programą, kuri:

# Leistų vartotojui po vieną įvesti 5 žodžius
# Pridėtų įvestus žodžius į sąrašą
# Atspausdintų kiekvieną žodį, jo ilgį ir eilės numerį sąraše (nuo 1)
# Sudėtingiau: kad programa leistų įvesti norimą žodžių kiekį

# Patarimas: Naudoti sąrašą (list), ciklą for, funkcijas len ir index

# Kauliukų žaidimas

# Sukurti programą, kuri:

# Sugeneruotų tris atsitiktinius skaičius nuo 1 iki 6
# Jei vienas iš šių skaičių yra 5, atspausdinti „Pralaimėjai...“
# Kitu atveju atspausdinti „Laimėjai!“
# Patarimas: Naudoti while ciklą, funkciją random.randint (import random), else, break

# Random skaičiaus generavimo pavyzdys:

# import random

# print(random.randint(1, 6))

