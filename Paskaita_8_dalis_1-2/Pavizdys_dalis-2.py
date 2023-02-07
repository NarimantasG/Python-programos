# # # # # # class Gyvunas():
# # # # # #     def __init__(self, vardas, spalva):
# # # # # #         self.vardas = vardas
# # # # # #         self.spalva = spalva

# # # # # #     def begti(self):
# # # # # #         print("Bėgu")

# # # # # #     def murkti(self):
# # # # # #         print("Murrrrr")

# # # # # # # Kate pavelti gyvunas
# # # # # # class Kate(Gyvunas):
# # # # # #     def miaukseti(self):
# # # # # #         print("Miau")

# # # # # # # Suo pavelti gyvunas
# # # # # # class Suo(Gyvunas):
# # # # # #     def loti(self):
# # # # # #         print("Au")


# # # # # # # vezlys = Gyvunas("Tadas", "Rudas")
# # # # # # # vezlys.begti()
# # # # # # # kate=Gyvunas('Murka','Juodas')
# # # # # # # kate.murkti()

# # # # # # kate1 = Kate("Mūza", "Pilka")
# # # # # # suo1 = Suo("Čakas", "Baltas")

# # # # # # kate1.begti()
# # # # # # suo1.loti()

# # # # # class Gyvunas():
# # # # #     def __init__(self, vardas, spalva):
# # # # #         self.vardas = vardas
# # # # #         self.spalva = spalva

# # # # #     def begti(self):
# # # # #         print("Bėgu")


# # # # # class Vezlys(Gyvunas):
# # # # #     def begti(self):
# # # # #         print("Aš lėtai einu, ne bėgu")

# # # # # gyvunas = Gyvunas("Jonas", "d")
# # # # # gyvunas.begti()

# # # # # vezlys = Vezlys("Tadas", "Rudas")
# # # # # vezlys.begti()

# # # # class Tevas:
# # # #     def __init__(self, vardas, pavarde):
# # # #         self.vardas = vardas
# # # #         self.pavarde = pavarde


# # # # class Vaikas(Tevas):
# # # #     def __init__(self, vardas, pavarde, mokymosi_istaiga):
# # # #         super().__init__(vardas, pavarde)
# # # #         self.mokymosi_istaiga = mokymosi_istaiga


# # # # tevas = Tevas("Rokas", "Budreika")
# # # # vaikas = Vaikas("Urtė", "Budreikaitė", "Čiurlionio menų gimnazija")

# # # # # print(tevas.mokymosi_istaiga)
# # # # print(vaikas.mokymosi_istaiga)


# # # class Irasas:
# # #     def __init__(self, suma):
# # #         self.suma = suma

# # # class PajamuIrasas(Irasas):
# # #     pass

# # # class IslaiduIrasas(Irasas):
# # #     pass

# # # biudzetas = []

# # # irasas1 = PajamuIrasas(2000)
# # # irasas2 = IslaiduIrasas(20)
# # # biudzetas.append(irasas1)
# # # biudzetas.append(irasas2)

# # # for x in biudzetas:
# # #     if isinstance(x, PajamuIrasas):
# # #         print(x.suma)
# # #         print("Čia pajamos")
# # #     elif isinstance(x, IslaiduIrasas):
# # #         print(x.suma)
# # #         print("Čia Išlaidos")

# # class Darbuotojas:
# #     def __init__(self, vardas, pavarde, atlyginimas):
# #         self.vardas = vardas
# #         self.pavarde = pavarde
# #         self.__atlyginimas = atlyginimas

# #     def set_atlyginimas(self, naujas):
# #         if naujas < 0:
# #             print("Atlyginimas negali būti neigiamas")
# #         else:
# #             self.__atlyginimas = naujas

# # domas = Darbuotojas("Domas", "Rutkauskas", 1200)
# # domas.set_atlyginimas(-1200)

# # Getters and Setters in python are often used when:
# # We use getters & setters to add validation logic around getting and setting a value.
# # To avoid direct access of a class field i.e. private variables cannot be accessed directly or modified by external user.

# class Darbuotojas:
#     def __init__(self, vardas, pavarde, atlyginimas):
#         self.vardas = vardas
#         self.pavarde = pavarde
#         self.__atlyginimas = atlyginimas

#     def set_atlyginimas(self, naujas):
#         if naujas < 0:
#             print("Atlyginimas negali būti neigiamas")
#         else:
#             self.__atlyginimas = naujas

#     def get_atlyginimas(self):
#         return self.__atlyginimas

# domas = Darbuotojas("Domas", "Rutkauskas", 1200)
# print(domas.get_atlyginimas())
# domas.__atlyginimas=500
# print(domas.get_atlyginimas())

class Darbuotojas:
    def __init__(self, vardas, pavarde, atlyginimas):
        self.vardas = vardas
        self.pavarde = pavarde
        self.__atlyginimas = atlyginimas

    @property
    def atlyginimas(self):
        return self.__atlyginimas

    @atlyginimas.setter
    def atlyginimas(self, naujas):
        if naujas < 0:
            print("Atlyginimas negali būti neigiamas")
        else:
            self.__atlyginimas = naujas


domas = Darbuotojas("Domas", "Rutkauskas", 1200)
print(domas.atlyginimas)
domas.atlyginimas=500
print(domas.get_atlyginimas())