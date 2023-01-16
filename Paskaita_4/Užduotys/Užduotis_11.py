# #Užduotis1-1

# likutis=['Jonas','Jonaitis','Rokas']
# pirmas=likutis[0]
# paskutinis=likutis[-1]
# print(likutis)
# print('Pirmas: ',pirmas,'Paskutinis: ',paskutinis)
# print('saraso dydis: ',len(likutis),' elementai')

# #Užduotis1-2

# likutis={'Jonas':1.50,'Petras':1.60,'Juozas':1.70}
# print(likutis,'ugiu skaicius: ',len(likutis))

# #Užduotis1-3

# likutis=[]
# while True:
#     pazimys=input('Iveskite pazimy ')
#     likutis.append(pazimys)
#     Kartoti=input('Ivesti daugiau pazymiu? t/n ')
#     if Kartoti=='n':
#         print(likutis, 'Pazymiu kiekis',len(likutis))
#         break

# #Užduotis2-4

# likutis=['Vlnius','Kaunas','Šiauliai']
# miestas=str(input('Įveskite miesta '))
# ari=input('Ar norite pasirinkti Įvedimo vieta? t/n ')
# if ari=='t':
#     v=int(input('Sarasas skaiciuojamas nuo 0. Įveskite skaičių '))
#     likutis.insert(v, miestas)
# else:
#     likutis.append(miestas)
# print(likutis)

# #Užduotis2-5

# likutis=[10,15,96,54,75,88,62]
# i=0
# while True:
#     kp=input('kiek irašu pašalinti? ')
#     while i!=kp:
#         likutis.pop(kp)
#         i=i+1
#     print(likutis)
#     tp=input('Toliau šalinti sarašo elementus? t/n ')
#     if tp=='n':
#         break
#     if len(likutis):
#         print('Sarašas tuščias')
#         break
    
# #Užduotis3-6

# likutis=[5,8,6,4]
# list2=[5,8,6,4,9]
# print(likutis)
# print(list2)
# print('Po patikrinimo')
# if len(likutis)>=5:
#     likutis.clear
#     print(likutis)
# if len(list2)>=5:
#     list2.clear
#     print(list2)

# #Užduotis3-7

# likutis=['Automobilis','Kompiuteris','Lėktuvas','Laivas']
# verte=input('Iveskite žody ')
# if verte in likutis:
#     print('Žodis saraše yra')
#     print(likutis.index(verte))
# else:
#     print('Tokio žodžio nėra')

# #Užduotis3-8

# studentas=[5,10,2,8,10,9,10,10]
# print('Studentas turi:', studentas.count(10), 'dešimtukų/us')

# #Užduotis4-9

# automobiliai=['Wolkswagen','Subaru','Audi','BMW']
# print(automobiliai)
# automobiliai.reverse()
# print(automobiliai)

# #Užduotis4-10

# studentas=[5,2,8,9,10]
# i=0
# while i!=3:
#     x=max(studentas)
#     print(x)
#     x2=studentas.index(x)
#     studentas.pop(x2)
#     i=i+1

# #Užduotis4-11

# studentas=[5,2,8,2,9,4,10,4,4]
# if 4 in studentas:
#     print(studentas.count(4),'Ketvertai')
# if 3 in studentas:
#     print(studentas.count(3),'Trejetai')
# if 2 in studentas:
#     print(studentas.count(2),'Dvejetai')
# if 1 in studentas:
#     print(studentas.count(1),'Vienetai')

# #Užduotis5-12

# likutis=[5,8,9,1,7,2,63,54
# ,98,52,75]
# print(likutis[:3])
# print(likutis[2:4])
# print(likutis[7:11])
# print(likutis[2::2])
# likutis.reverse()
# print(likutis[:11])

# #Užduotis5-13

# studentas=[5,2,8,9,10]
# geriausi_pazimiai=[]
# i=0
# while i!=3:
#     x=max(studentas)
#     geriausi_pazimiai.append(x)
#     x2=studentas.index(x)
#     studentas.pop(x2)
#     i=i+1
# print(geriausi_pazimiai)

# #Užduotis5-14

# zodynas=[]
# while True:
#     zodynas.append(input('Ivaskite zody '))
#     if len(zodynas)>=1:
#         zodynas.sort()
#     print(zodynas)
#     testi=input('Testi? t/n ')
#     if testi =='n':
#         break

# #Užduotis5-15

# likutis=[10,15
# ,5,3]
# list2=[]
# list2.append(likutis[2])
# list2.append(likutis[3])
# print(list2)

# #Užduotis6-16

# #16-1  
# sarasas=', '.join(['Vardenis','Pavardenis','miestas'])
# print(sarasas)
# #16-2 
# sarasas=' | '.join(['Vardenis','Pavardenis','miestas'])
# print(sarasas)
# #16-3
# sarasas=' '.join(['Vardenis','Pavardenis','miestas'])
# print(sarasas)

# #Užduotis7-17

# a, b, *other =['Python','desktop','.py']
# print(a)
# print(b)
# print(other)

# #Užduotis8-18

# a, b, c={'Jonas Babelis', 'Juozas Morkinas','Vardenis Pavardenis'}
# print(f'Prie projekto dirba šie komandos nariai: \n{a}\n{b}\n{c}')

# #Užduotis8-19

# list=['Skaičiai ir matematika','Kintamieji ir duomenų tipai','Informacijos išvedimas',
# 'Skaičiai ir matematika ','Aritmetiniai veiksmai','Informacijos įvedimas','Sąlyga if','range()',
# 'Ciklas for','Ciklas While','Sąrašas list']
# i=0
# item=0
# while i!=len(list):
#     print(i,'-as',list[item])
#     i=i+1
#     item=item+1
# i=0
# item=0
# for i in range(1,len(list)):
#     print(i,'-as',list[item])
#     item=item+1

# #Užduotis9-20

# studiju_programos=['Python','Automatinis testavimas','Rankinis testavimas','Java']
# print('Studijos:')
# i=0
# item=0
# while i!=len(studiju_programos):
#     print(studiju_programos[item])
#     i=i+1
#     item=item+1

# #Užduotis9-21

# salis=['Lietuva','Lenkija','Amerika','Ukraina','Norvegija']
# print('Studijos:')
# i=0
# item=0
# while i!=len(salis):
#     print('Šalis - ',salis[item])
#     i=i+1
#     item=item+1

# #Užduotis10-22

# prekes=['Agurkai','Pomidorai','Burokai','Kopūstas']

# print('Studijos:')
# i=0
# item=0
# print('Saraše yra',len(prekes),'Prekių/ės')
# while i!=len(prekes):
#     print(i+1,'-a Prekė ',prekes[item])
#     i=i+1
#     item=item+1

# #Užduotis10-23

# pazymiai=[5,10,9,4,2,3,7]
# i=0
# item=0
# pazymiai.sort(reverse=True)
# print(pazymiai)
# while i!=len(pazymiai):
#     if pazymiai[item]==10:
#         print(pazymiai[item],'Puikiai')
#     if pazymiai[item]<=9 and pazymiai[item]>=7:
#         print(pazymiai[item],'Labai gerai')
#     if pazymiai[item]==6:
#         print(pazymiai[item],'Gerai')
#     if pazymiai[item]==5:
#         print(pazymiai[item],'Patenkinamai')
#     if pazymiai[item]<=4:
#         print(pazymiai[item],'Neišlaikyta')
#     i=i+1
#     item=item+1

# #Užduotis11-24

# from random import randint
# list=[]
# i=0
# kiek=int(input('kiek kartų kurti atsitiktinius skaičius? '))
# while i!=kiek:
#     list.append(randint(1,kiek*5))
#     i=i+1
# print(list)
# i=0
# item=0
# while i!=kiek:
#     print(list[item], 'Kvadratas', list[item]**2)
    
#     item=item+1
#     i=i+1

# #Užduotis11-25

# a, b, c=[5,10,15]
# print(a,b,c)
# a=15
# b=20
# c=25
# print(a,b,c)

#Užduotis12-26

# from random import randint
# list=[4]
# i=0
# while i!=20:
#     list.append(randint(1,100))
#     i+=1
# print(list[1])
    
# i=0
# item=int(0)
# print=('Lyginiai Skaičiau')
# while i!=20:
#     print(list)
#     i+=1
#     item+=1

# NEBAIGTA!!!!!!!

