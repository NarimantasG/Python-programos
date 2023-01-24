# #Užduotis 1-1

# skaicius=1
# while skaicius<=20:
#     print(skaicius)
#     skaicius+=1

# #Užduotis 1-2

# skaicius=1
# while skaicius<=40:
#     if skaicius%2==0:
#         print(f'{skaicius} - Lyginis')
#     if skaicius%2!=0:
#         print(f'{skaicius} - Nelyginis')
#     skaicius+=1

# #Užduotis 1-3
    
# skaicius=25
# while skaicius<=50:
#     if skaicius%3==0:
#         print(f'Skaičius dalinasi iš 3')
#     else:
#         print(skaicius)
#     skaicius+=1

# #Užduotis 1-4

# skaicius=1
# while skaicius<=100 and skaicius%7!=0:
#     print(skaicius)
#     skaicius+=1

# #Užduotis 1-5

# skaicius=1
# while skaicius%3!=0 and skaicius%5!=0:
#     print(skaicius)
#     skaicius+=1

# #Užduotis 1-5

# pradzia=int(input('Įveskite pradžios skaičių: '))
# pabaiga=int(input('Įveskite pabaigos skaičių: '))
# if pradzia>pabaiga:
#      print('Įvyko klayda Pradžia didesnė už pabaiga. Bandykite vėl.')
#      exit()
# while pradzia<pabaiga:
#     if pradzia%2==0:
#         print(f'{pradzia} - Lyginis  Pakeltas kvadratu: {pradzia**2}')
#     if pradzia%2!=0:
#         print(f'{pradzia} - Nelyginis  Pakeltas kvadratu: {pradzia**2}')
#     pradzia+=1

# #Užduotis 2-6

# skc2 = 1

# while skc2 < 100:
#     skc2 += 1
#     print(skc2)
#     if skc2 % 2 != 0 and skc2 % 3 != 0 and skc2 % skc2 == 0 and skc2 > 20:
#         print(skc2, "skaicius yra pirminis ir didesnis nei 20.")
#         break


# def yraPirminis(s):
#     if (s==1 or s==0):
#         return False
#     for i in range(2,s):
#         if (s%i==0):
#             return False
#     return True
# s=20
# for i in range(1,s+1):
#     if(yraPirminis(i)):
#         print(i,end=" ")

# #Užduotis 2-7

# skaicius=int(input('Įrašykite kaičių: '))
# suma=0
# if skaicius>0:
#     while skaicius>0 and skaicius!=0:
#         suma=skaicius+suma
#         skaicius=skaicius-1
#     print(f'suma: {suma}')
# elif skaicius<0:
#     while skaicius<0 and skaicius!=0:
#         suma=skaicius+suma
#         skaicius=skaicius+1
#     print(f'suma: {suma}')

# #Užduotis 2-8

# sk=1
# sum=0
# while sk!=0:
#     sk=int(input('iveskite skaicius: '))
#     sum+=sk
# print(f'suma: {sum}')

# #Užduotis 3-9

# kartoti=True
# while kartoti==True:
#     sk1=int(input('iveskite skaiciu 1: '))
#     sk2=int(input('iveskite skaiciu 2: '))
#     print(f'Skaicius 1: {sk1}')
#     print(f'Skaicius 2: {sk2}')
#     print(f'{sk1}+{sk2}={sk1+sk2}')
#     print(f'{sk1}-{sk2}={sk1-sk2}')
#     print(f'{sk1}*{sk2}={sk1*sk2}')
#     print(f'{sk1}/{sk2}={sk1/sk2}')
#     kartoti=input('ar kartoti? t/n ')

# #Užduotis 3-10
 
# i=1
# while True:
#     sk=int(input('Iveskite skaiciu: '))
#     while i!=sk+1:
#         print(f'{sk}*{i}={sk*i}')
#         i=i+1
#     kartoti=input('Kartoti? t/n: ')
#     if kartoti=='n':
#         break

# #Užduotis 4-11

# sk=1
# i=0-1
# sum=0
# while sk!=0:
#     sk=int(input('iveskite skaicius: '))
#     sum+=sk
#     i=i+1
# print(f'suma: {sum} Vidurkis: {sum/i} Iteracinis: {i}')

# #Užduotis 4-12

# while True:
#     pazymiu_suma = 0
#     pazymiu_kiekis = 0
#     pazymys = -1
#     print('Iveskite tiek pazymiu kiek norite (atskiriant enter)')
#     print('Norint baigti irasykite 0')
#     while pazymys != 0:
#         pazymys = int(input('Iveskite pazymi: '))
#         if pazymys != 0:
#             pazymiu_suma += pazymys
#             pazymiu_kiekis += 1
#     vidurkis = round(pazymiu_suma / pazymiu_kiekis, 1)
#     print('Suvestu pazymiu vidurkis:', vidurkis)
#     kartoti=input('Kartoti? t/n ')
#     if kartoti=='n':
#         break

# #Užduotis 5-13

# from random import randint
# list=0
# spejimu_limitas=99999
# i=0
# sk1=0
# sk2=10
# sudetingumas=input('Pasirinkite sudetingumo lygi zemas/vidutinis/sunkus  z/v/s ')
# spejimai=input('Riboti spejimus? t/n ')
# if spejimai=='t':
#         spejimu_limitas=10
# if sudetingumas=='z':
#     sk=10
# if sudetingumas=='v':
#     sk=30
# if sudetingumas=='s':
#     sk=50
# while i!=1:
#     list=randint(1,sk)
#     i=i+1
# while sk1!=spejimu_limitas:
#     if spejimai=='t':
#         print(f'turite {sk2} spejimus')
#         sk2=sk2-1
#     spejimas=int(input('spekite skaiciu: '))
#     if spejimas<list:
#         print('Skaicius didesnis')
#     if spejimas>list:
#         print('Skaicius Mazesnis')
#     if spejimas==list:
#         print('Laimejai')
#         break
#     sk1+=1
# print('nebeturite spejimu')
# print('pralaimejai')