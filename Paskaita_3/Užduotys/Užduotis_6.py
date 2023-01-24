# # Užduotis 1-1

# print('Įveskite 3 kintamuosius')
# sk1=int(input())
# sk2=int(input())
# sk3=int(input())
# suma=sk3*2
# if sk1==sk2:
#     print(f'{sk1} ir {sk2} skayčiai yra lygus')
# if sk2==sk3:
#     print(f'{sk2} ir {sk3} skaičiai yra lygus')
# if sk1>sk2:
#     print(f'Skaičius {sk1} didesnis už skaičiu {sk2}')
# if sk2>suma:
#     print(f'Skaičius {sk2} yra didesnis už padvigubinta tračia skaičių {suma}')
# if sk1 % 2 == 0:
#     print(f'skaičius {sk1} yra lyginis')
# if sk2 % 2 !=0:
#     print(f'Skaičius {sk2} yra nelyginis')
# if sk3>0:
#     print(f'Skaičius {sk3} yra lyginis')
# if sk1<0:
#     print(f'Skaičius {sk1} yrs nelyginis')
# if sk2 % 4 == 0:
#     print(f'Skaičius {sk2} dalinasi iš 4')
# if sk3 % 8 == 0:
#     print (f'Skaičius {sk3} dalinasi iš 8')

# #Užduotis 1-2

# print('Įveskite savo amžiu')
# Amzius = int(input())
# if Amzius >= 18:
#     print('Jūs galite balsuoti! :)')
# elif Amzius < 18:
#     print('Dėje jūs negalite balsoti :(')

# #Užduotis 1-3

# print('Kiek pažymių')
# SkaiciusPazymiu=int(input())
# pazimys=0
# for i in range(SkaiciusPazymiu):
#     print(f'Pažimys {i+1}')
#     pazimys+=int(input())
# print(f'Pazimys {pazimys}')
# vidurkis = pazimys / SkaiciusPazymiu
# print (f'vidurkis {vidurkis}')
# if vidurkis >= 5:
#     print('Vidurkis teigiamas')
# elif vidurkis < 5:
#     print('Vidurkis Neigiamas')

# #Užduotis 1-4

# print('Įveskite skaičių')
# sk = int(input())
# if sk%5==0:
#     for i in range(5):
#         print(f'{sk} * {i+1}')
# if sk%2==0:
#     sk2=sk**2
#     sk3=sk/2
#     sk4=sk2/2
#     print(f'{sk}, {sk2}, {sk3}')
# if sk%7!=0:
#     print('Įveskitę antą skaičių')
#     sk1=int(input())
#     print(f'Suma: {sk+sk1}, Skirtumas: {sk-sk1}, Sandauga: {sk*sk1}, Dalyba: {sk/sk1}')

# #Užduotis 2-5

# print('Įveskite 3 skaičius')
# sk=int(input())
# sk2=int(input())
# sk3=int(input())
# if sk>sk2:
#     print(f'Skaičius {sk} yra didesnis už {sk2}')
# elif sk2>sk3:
#     print(f'Skaičius {sk2} yra didesnis už {sk3}')
# elif sk3>sk:
#     print(f'Skaičius {sk3} yra didesnis už {sk}')
# elif sk==sk2:
#     print(f'Skaičiai {sk} ir {sk2} yra lygus')
# elif sk2==sk3:
#     print(f'Skaičiai {sk2} ir {sk3} yra lygus')
# elif sk==0:
#     print(f'Skaičius {sk} yra lygus 0')
# elif sk2<0:
#     print(f'Skaičius {sk2} yra neigiamas')
# elif sk3>0:
#     print(f'Skaičius {sk3} yra teigiamas')

#Užduotis 2-6

# print('Įveskyte egzamino pažymį nuo 0 iki 10')
# sk=int(input())

# if sk==10:
#     print('Puiku')
# elif sk>=9:
#     print('Labai gerai')
# elif sk>=7:
#     print('Gerai')
# elif sk>=5:
#     print('Patenkinama')
# elif sk<=4:
#     print('Egzaminas neišlaikytas')
# else:
#     print('Įrašytas pažymys didesnis nei 10 bandykite darkarta')

#Užduotis 3-7

# print('Įveskite skaičių')
# sk=int(input())
# if sk>=0:
#     print('Skaičius teigiamas')
# else:
#     print('Skaičius neigiamas')

#Užduotis 3-8

# print('Įveskite skaičių')
# sk=int(input())
# if sk%7==0:
#     print(f'Skaičius {sk} dalinasi iš 7')
# else:
#     print(f'Skaičius {sk} nesidalina iš 7')

#Užduotis 3-9

# failas='Test.py'
# if failas.endswith('.py'):
#     print('Failas yra .py tipo')
# else:
#     print('Failas nėra .py tipo')

#Užduotis 4-10

# print('Įveskyte skaičių')
# sk=int(input())
# if sk%2==0:
#     print(f'Skaičius {sk} yra lyginis')

# elif sk%5==0:
#     print(f'Skaičius {sk} dalinasi iš 5')
# elif sk==3:
#     print(f'Skaičius {sk} lygus 3')
# else:
#     print('Skaičius neatitiko nė vienos salygos.\nBandykite darkartą')

#Užduotis 4-11

# print('Įveskite 3 skaičius')
# sk=int(input())
# sk2=int(input())
# sk3=int(input())
# sum=sk3*2
# if sk==sk2:
#     print(f'{sk} yra lygus {sk2} ')
# elif sk==sk3:
#     print(f'{sk} yra lygus {sk3}')
# elif sk3>sk:
#     print(f'{sk3} didesnis už {sk}')
# elif sk2==sum:
#     print(f'{sk2} yra lygus {sum}')
# elif sk%3==0:
#     print(f'{sk} dalinasi iš 3')
# else:
#     print('Skaičiai neatitiko nė vienos salygos.\nBandykite darkartą')

#Užduotis 4-12

# print('Įveskite 3 skaičius')
# sk1=int(input())
# sk2=int(input())
# sk3=int(input())
# if sk1<sk2 and sk2>sk3:
#     print(f'{sk2} yra didžiausias')
# elif sk1>sk2 and sk1>sk3:
#     print(f'{sk1} yra didžiausias')
# else:
#     print(f'{sk3} yra didžiausias')

#Užduotis 4-13

# print('Įveskite 3 skaičius')
# sk1=int(input())
# sk2=int(input())
# sk3=int(input())
# if sk1>sk2 and sk2<sk3:
#     print(f'{sk2} yra mažiausias')
# elif sk1<sk2 and sk1<sk3:
#     print(f'{sk1} yra mažiausias')
# else:
#     print(f'{sk3} yra mažiausias')

#Užduotis 4-14

# print('Įveskite 3 egzaminų rezultatus nuo 1-10')
# sk1=int(input())
# sk2=int(input())
# sk3=int(input())
# vidurkis=(sk1+sk2+sk3)/3
# #print(f'{vidurkis}')
# if vidurkis<0 or vidurkis>10:
#     print('Kažkur įvyko klaida vidurkis per mažas arba per didelis bandykite darkartą')
#     exit()
# elif vidurkis>=8 and vidurkis <=10:
#     print(f'Vidurkis yra tarp 8 ir 10  {vidurkis}')
# elif vidurkis>=5 and vidurkis <=8:
#     print(f'Vidurkis yra tarp 5 ir 8   {vidurkis}')
# else:
#     print(f'Vidurkis yra mažiau 5   {vidurkis}')

#Užduotis 4-15

# print('Įveskite 2 skaičius')
# sk1=int(input())
# sk2=int(input())
# if sk1>sk2 or sk2==0:
#     print(f'Pirmas skaičius didesis už antra arba antras skaičius lygus 0 {sk1, sk2}')
# elif sk2>sk1 or sk1==5:
#     print(f'Antras skaičius didesis už pirma arba pirmas skaičius lygus 5 {sk2, sk1}')
# elif sk1>sk2 and sk2==20:
#     print(f'Pirmas skaičius didesis už antra ir antras skaičius lygus 20 {sk1, sk2}')
# elif sk2>sk1 and sk1<100:
#     print(f'Antras skaičius didesis už pirma ir pirmas skaičius mažiau 100 {sk2, sk1}')
# else:
#     print('Įvesti duomenys neatitiko nė vienos salygos.\nBandykite dar kartą')

#papildoma

# metai = int(input("Iveskite metus: "))
# if (metai % 400 == 0) or (metai % 100 != 0 and metai % 4 == 0):
#     print("Keliamieji metai")
# else:
#     print("Nekeliamieji metai")

# for metai in range(1900, 2100):
#     if metai % 400 == 0:
#         print(metai)
#     elif metai % 100 == 0:
#         continue
#     elif metai % 4 == 0:
#         print(metai)
#     else:
#         continue
