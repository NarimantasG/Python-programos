# Užduotis 1

class Sakinys:
    def __init__(self,zodis='Žodis'):
        self.zodis=zodis
    def Atbulai(self):
        return self.zodis[::-1]
    def Mazosios(self):
        return  self.zodis.lower()
    def Dydziosios(self):
        return self.zodis.upper()
    def Pagal_eiles_numeri(self):
        return self.zodis[2]
    def Kiek_simboliu(self):
        return len(self.zodis)
    def Pakeistas(self,senas,naujas):
        return self.zodis.replace(senas,naujas)
    def Galutinis(self):
        print(len(self.zodis))
        zodziu_kiekis = len(self.zodis.split())
        skaiciai = sum(i.isnumeric() for i in self.zodis)
        didziosios = sum(i.isupper() for i in self.zodis)
        mazosios = sum(i.islower() for i in self.zodis)
        print(f"Žodžių kiekis: {zodziu_kiekis},\nSkaičiai: {skaiciai},\nDidžiosios: {didziosios},\nMažosios: {mazosios}")
sakinys1 = Sakinys('Naujas')
print(sakinys1.Atbulai())
print(sakinys1.Mazosios())
print(sakinys1.Dydziosios())
print(sakinys1.Pagal_eiles_numeri())
print(sakinys1.Kiek_simboliu())
print(sakinys1.Pakeistas('Žodis','Naujas'))
sakinys1.Galutinis()

###### 2Uzduotis
import datetime

import calendar



class Sukaktis:

    def __init__(self, metai=1987, menuo=6, diena=5, valandos=20, minutes=25):

        self.metai = metai

        self.menuo = menuo

        self.diena = diena

        self.valandos = valandos

        self.minutes = minutes

        self.data = datetime.datetime(metai, menuo, diena, valandos, minutes)


    def smulkiai(self):

        now = datetime.datetime.now()

        skirtumas = now - self.data

        print(f"Praėjo metų: ", skirtumas.days // 365)

        print("Praėjo mėnesių: ", skirtumas.days / 365 * 12)

        print("Praėjo savaičių: ", skirtumas.days / 7)

        print("Praėjo dienų: ", skirtumas.days)

        print("Praėjo valandų: ", skirtumas.total_seconds() / 3600)

        print("Praėjo minučių: ", skirtumas.total_seconds() / 60)

        print("Praėjo sekundžių: ", skirtumas.total_seconds())


    def arKeliamieji(self):

        if calendar.isleap(self.metai):

            print("Keliamieji metai")


    def atimtiDienas(self, dienos):

        return self.data - datetime.timedelta(days=dienos)


    def pridetiDienas(self, dienos):

        return self.data + datetime.timedelta(days=dienos)


    def __str__(self):

        return (

            f"Data: {self.metai}-{self.menuo}-{self.diena} {self.valandos}:{self.minutes}")



data1 = Sukaktis(2000, 1, 1, 12, 12)

data1.arKeliamieji()

data1.smulkiai()

print(data1.atimtiDienas(5))

print(data1.pridetiDienas(45))

print(data1)
#u=duotis 3
