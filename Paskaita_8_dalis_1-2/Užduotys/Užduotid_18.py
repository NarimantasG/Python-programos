# #Užduotis 1
# class Automobilis:
#     def __init__(self, metai, modelis, kuro_tipas):
#         self.metai=metai
#         self.modelis=modelis
#         self.kuro_tipas=kuro_tipas
    
#     def vaziuoti(self):
#         print('Automobilis Važiuoja')

#     def stoveti(self):
#         print('Automobilis Priparkuotas')

#     def pildyti_degalus(self):
#         print('Automobilio Degalai įpilti')

#     def Informacija(self):
#         print('Metai ',self.metai,'\nModelis ',self.modelis,'\nKuro tipas ',self.kuro_tipas)

# Automobilis1=Automobilis(2005,' Tojota',' Standartinio oktaninio skaičiaus') #arba "aukšto oktaninio skaičiaus"
# Automobilis1.Informacija()

# class Elektromobilis(Automobilis):

#     def pildyti_degalus(self):
#         print('Automobilio Baterija įkrauta')

#     def Vaziuoti_autonomiskai(self):
#         print('Automobilis Važiuoja Autonomiškai')

# Automobilis2=Automobilis(2019,'Audi','aukšto oktaninio skaičiaus')
# Elektromobilis1=Elektromobilis(2012,' Ford',' Baterija')
# print(' ')
# Automobilis2.vaziuoti()
# Automobilis2.stoveti()
# Automobilis2.pildyti_degalus()
# print(' ')
# Elektromobilis1.vaziuoti()
# Elektromobilis1.pildyti_degalus()
# Elektromobilis1.Vaziuoti_autonomiskai()

#žduotis 2

import datetime

class Darbuotojas:

    def __init__(self,Vardas,Valandos_ikainis,Dirba_nuo):
        self.Vardas=Vardas
        self.Valandos_ikainis=Valandos_ikainis
        self.Dirba_nuo=Dirba_nuo

    def Kiek_dirba_valandu(self):
        nuo_kada_dirba=datetime.datetime.strptime(self.Dirba_nuo,"%Y, %m, %d, %H, %M, %S")
        dabar=datetime.datetime.today()
        skirtumas=dabar - nuo_kada_dirba
        return skirtumas.days*8
    
    def Paskaiciuoti_atlyginima(self):
        Atlyginimas=self.Valandos_ikainis * self.Kiek_dirba_valandu()
        print (self.Vardas + " uždirbo " + str(Atlyginimas))

class NormalusDarbuotojas(Darbuotojas):

    def _kiek_dirba_valandu(self):

        nuo_kada_dirba = datetime.datetime.strptime(self.Dirba_nuo, "%Y, %m, %d, %H, %M, %S")

        dabar = datetime.datetime.today()

        skirtumas = dabar - nuo_kada_dirba

        return (skirtumas.days * 8) / 7 * 5

Dovydas = Darbuotojas("Dovydas", 10, "2018, 03, 12, 12, 00, 00")

Dovydas_normalus = NormalusDarbuotojas("Dovydas", 10, "2018, 03, 12, 12, 00, 00")

Dovydas.Paskaiciuoti_atlyginima()

Dovydas_normalus.Paskaiciuoti_atlyginima()
    