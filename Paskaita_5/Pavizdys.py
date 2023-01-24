# def pasisveikinti():
#     print("Sveikas, pasauli!")

# pasisveikinti()
# pasisveikinti()
# pasisveikinti()


# def pasisveikinti(vardas):
#     print(f"Sveikas, {vardas}")

# pasisveikinti("Tomas")
# pasisveikinti("Jonas")
# pasisveikinti("")


# def kvadratas(skaicius):
#     kvadratu = skaicius ** 2
#     print(kvadratu)

# kvadratas(2)

# def kvadratu(skaicius):
#     rezultatas = skaicius ** 2
#     print(rezultatas)
# kvadratu(3)
# daugyba = kvadratu(3) * 2
# print(daugyba)
# print(kvadratu(3))

# def kvadratu(skaicius):
#     rezultatas = skaicius ** 2
#     return rezultatas

# daugyba = kvadratu(3) * 2
# print(daugyba)

# def skaiciu_suma(skaicius1, skaicius2, skaicius3):
#     suma = skaicius1 + skaicius2
#     daugyba = suma * skaicius3
#     return daugyba

# print(skaiciu_suma(2, 5, 20))

# def skaiciu_suma(skaicius1=10, skaicius2=10, skaicius3=1):
#     rezultatas = (skaicius1 + skaicius2) * skaicius3
#     return rezultatas
# print(skaiciu_suma())
# print(skaiciu_suma(2))
# print(skaiciu_suma(2, 5))
# print(skaiciu_suma(2, 5, 4))

# def skaiciu_suma(skaicius1=10, skaicius2=10, skaicius3=1):
#     rezultatas = (skaicius1 + skaicius2) * skaicius3
#     return rezultatas

# print(skaiciu_suma(skaicius3=3))
# print(skaiciu_suma(skaicius3=3, skaicius2=5))
# # print(skaiciu_suma(2, 5))
# # print(skaiciu_suma(2, 5, 4))


# def daug_kvadratu(*args):
#     for skaicius in args:
#         print(skaicius ** 2)


# daug_kvadratu(4, 5, 7, 8, 9, 10, 1.1)

#kwargs =od=iams
# def spausdinti_reiksmes(**kwargs):
#     for raktas, reiksme in kwargs.items():
#         print(raktas, reiksme)


# spausdinti_reiksmes(vardas="Tomas", pavarde="Rutkauskas", lytis="Vyras", amzius=29, daiktai=["Telefonas", "Ausinės", "Krepšys"])

# def spausdinti_reiksmes(vardas, pavarde, **kwargs):
#     print(f"Vardas: {vardas}, Pavardė: {pavarde}")
#     for raktas, reiksme in kwargs.items():
#         print(raktas, reiksme)
# spausdinti_reiksmes("Tomas", "Rutkauskas", lytis="Vyras", amzius=29, daiktai=["Telefonas", "Ausinės", "Krepšys"])

# def funkcija(parametras1, parametras2):
#     '''
#     :param parametras1:
#     :param parametras2:
#     :return:
#     '''
#     return

# def kvadratu(a):
#     return a**2
# lambda a: a ** 2

# kvadratu = lambda a: a ** 2
# print(kvadratu(2))

# sarasas = [2, 5, 4, 65, 78, 99, 38]
# sarasas2 = map(lambda a: a ** 2, sarasas)
# for skaicius in sarasas2:
#     print(skaicius)

# #Dar pora lambda panaudojimo pavyzdžių:

# daugyba_is_saves = [lambda i=skaicius: i*i for skaicius in range(1, 6)]
# for vienas in daugyba_is_saves:
#     print(vienas())

# keliamieji = [lambda i=metai: i for metai in range(1900, 2101) if (metai % 400 == 0) or (metai % 100 != 0 and metai % 4 == 0)]
# for vienas in keliamieji:
#     print(vienas())









# Sukurti funkciją, kuri patikrintų, ar paduotas Lietuvos piliečio asmens kodas yra validus.Padaryti, kad programa sugeneruotų teisingą asmens kodą (panaudojus anksčiau sukurtą funkciją) pagal įvestą lytį, gimimo datą ir eilės numerį).Asmens kodas susideda iš 11 skaitmenų, pvz.: 43604309202:

#     pirmasis rodo gimimo šimtmetį ir asmens lytį (1 – XIX a. gimęs vyras, 2 – XIX a. gimusi moteris, 3 – XX a. gimęs vyras, 4 – XX a. gimusi moteris, 5 – XXI a. gimęs vyras, 6 – XXI a. gimusi moteris);
#     tolesni šeši – asmens gimimo metų du paskutiniai skaitmenys, mėnuo (du skaitmenys), diena (du skaitmenys);
#     dar tolesni trys skaitmenys – tą dieną gimusių asmenų eilės numeris;
#     paskutinis – iš kitų skaitmenų išvedamas kontrolinis skaičius.

# Kontrolinis skaičius[redaguoti | redaguoti vikitekstą]
# Jei asmens kodas užrašomas ABCDEFGHIJK, tai:
# S = A*1 + B*2 + C*3 + D*4 + E*5 + F*6 + G*7 + H*8 + I*9 + J*1
# Suma S dalinama iš 11, ir jei liekana nelygi 10, ji yra asmens kodo kontrolinis skaičius K. Jei liekana lygi 10, tuomet skaičiuojama nauja suma su tokiais svertiniais koeficientais:
# S = A*3 + B*4 + C*5 + D*6 + E*7 + F*8 + G*9 + H*1 + I*2 + J*3
# Ši suma S vėl dalinama iš 11, ir jei liekana nelygi 10, ji yra asmens kodo kontrolinis skaičius K. Jei vėl liekana yra 10, kontrolinis skaičius K yra 0.


# def grazinti_ak_kontrolini(asmens_kodas):
#     kodas = str(asmens_kodas)
#     A = int(kodas[0])
#     B = int(kodas[1])
#     C = int(kodas[2])
#     D = int(kodas[3])
#     E = int(kodas[4])
#     F = int(kodas[5])
#     G = int(kodas[6])
#     H = int(kodas[7])
#     I = int(kodas[8])
#     J = int(kodas[9])
#     S = A * 1 + B * 2 + C * 3 + D * 4 + E * 5 + F * 6 + G * 7 + H * 8 + I * 9 + J * 1
#     if S % 11 != 10:
#         return S % 11
#     else:
#         S = A * 3 + B * 4 + C * 5 + D * 6 + E * 7 + F * 8 + G * 9 + H * 1 + I * 2 + J * 3
#         if S % 11 != 10:
#             return S % 11
#         else:
#             return 0
# #43604309202
# grazinti_ak_kontrolini=asmens_kodas['E','D','G','A','E','D','A','J','C','A','C']
# print(grazinti_ak_kontrolini[S])



def grazinti_ak_kontrolini(asmens_kodas):
    kodas = str(asmens_kodas)
    A = int(kodas[0])
    B = int(kodas[1])
    C = int(kodas[2])
    D = int(kodas[3])
    E = int(kodas[4])
    F = int(kodas[5])
    G = int(kodas[6])
    H = int(kodas[7])
    I = int(kodas[8])
    J = int(kodas[9])
    S = A * 1 + B * 2 + C * 3 + D * 4 + E * 5 + F * 6 + G * 7 + H * 8 + I * 9 + J * 1
    if S % 11 != 10:
        return S % 11
    else:
        S = A * 3 + B * 4 + C * 5 + D * 6 + E * 7 + F * 8 + G * 9 + H * 1 + I * 2 + J * 3
        if S % 11 != 10:
            return S % 11
        else:
            return 0


def asmens_kodo_validacija(asmens_kodas):
    paskutinis_sk = int(str(asmens_kodas)[-1])
    return paskutinis_sk == grazinti_ak_kontrolini(asmens_kodas)


def asmens_kodo_generavimas(lytis, gimimo_data, eiles_numeris):
    pirmas_skaicius = ""

    data_split = gimimo_data.split("-")
    metai = data_split[0][:2]

    if lytis == "vyras":
        pirmas_skaicius = str((int(metai) - 18) * 2 + 1)
    else:
        pirmas_skaicius = str((int(metai) - 18) * 2 + 2)

    menuo = data_split[1]
    diena = data_split[2]

    be_paskutinio = pirmas_skaicius + metai + menuo + diena + eiles_numeris

    return int(be_paskutinio + str(grazinti_ak_kontrolini(be_paskutinio)))


print(asmens_kodo_validacija(45102129987))
print(asmens_kodo_validacija(61907108400))

print(asmens_kodo_generavimas("vyras", "2000-12-12", "512"))
print(asmens_kodo_generavimas("moteris", "1995-12-12", "500"))


# layout = [
#     [' ', '0', '1', '2'],
#     ['0', '-', '-', '-'],
#     ['1', '-', '-', '-'],
#     ['2', '-', '-', '-']
# ]

# mark_letter ='X'

# def mark_rotator():
#     global mark_letter
#     if mark_letter == 'X':
#         mark_letter = 'O'
#     else:
#         mark_letter = 'X'

# def print_layout():
#     for i in layout:
#         str1 = ' '
#         print(str1.join(i))

# #returns the position selection in a list format
# def play():
#     print_layout()
#     print(f'Enter the position you want to place {mark_letter} sign in the format 0 0: ')
#     position = list(input().split())
#     if not "".join(position).isnumeric():
#         print("Please enter the numbers only.")
#         play()
#     position = list(map(int, position))
#     if len(position) != 2:
#         print("Check the number of arguments you enter.")
#         play()

#     if isValidSelection(position):
#         mark_cell(position)
#         #print_layout()
#         if isWin():
#             print(f'The {mark_letter} is WON!')
#             return 0
#         else:
#             mark_rotator()
#             play()
#     else:
#         play()
    