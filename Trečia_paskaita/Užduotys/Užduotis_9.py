# #Užduotis 1-1

# Vardas='Narimantas'
# i=0
# for i in range(5):
#     i+1
#     print(f'{Vardas}')

# #Užduotis 1-2


# for i in range(11):
#     print(f'{i}')

# #Užduotis 1-3

# for i in range(0, 16, 2):
#     print(f'{i}')

# #Užduotis 1-4

# for i in range(1, 20, 3):
#     print(f'[{i}]')

# #Užduotis 1-5

# for i in range(1, 21):
#     if i%4==0:
#         print(f'{i}')

# #Užduotis 2-6

# for i in range(1, 16):
#     if i%2==0:
#         print(f'{i} - Lyginis')
#     elif i%2!=0:
#         print(f'{i} - Nelyginis')

# #Užduotis 2-7

# pradzia, pabaiga =1,11
# if pradzia>pabaiga:
#     print('Įvyko klayda Pradžia didesnė už pabaiga. Bandykite vėl.')
#     exit()
# if pradzia<pabaiga:
#     for i in range(pradzia, pabaiga):
#         print(f'{i}')
#         if i%2==0:
#             print('')

# #Užduotis 3-8

# pradzia, pabaiga =1,22
# if pradzia>pabaiga:
#     print('Įvyko klayda Pradžia didesnė už pabaiga. Bandykite vėl.')
#     exit()
# if pradzia<pabaiga:
#     for i in range(pradzia, pabaiga):
#         if i%2!=0:
#             print(f'{i}')
#         if i%8==0:
#             print(f'\n{i}\n')

# #Užduotis 3-9

# vardas=input('Įveskite vardą:')
# for i in vardas:
#     print(f'Labas: {vardas}')

# #Užduotis 3-10

# for elementas in [88, 65, 21, 26, 47]:
#     if elementas%2==0:
#         print(f'{elementas}')

# #Užduotis 4-11

# pradzia=int(input('Įveskite pradžios skaičių: '))
# pabaiga=int(input('Įveskite pabaigos skaičių: '))
# skaicaiusTipas=int(input('kokius skaičius norite matyti lyginius - 1 ar nelyginius -2: '))
# if pradzia>pabaiga:
#      print('Įvyko klayda Pradžia didesnė už pabaiga. Bandykite vėl.')
#      exit()
# if skaicaiusTipas==1:
    
#     for i in range(pradzia,pabaiga+1):
#         if i%2==0:
#             print(f'{i}')
# elif skaicaiusTipas==2:
#     for i in range(pradzia,pabaiga+1):
#         if i%2!=0:
#             print(f'{i}')
# else:
#     print('Įvestas norimo skaičiaus rodiklis virš ribų. Bandykite darkarta')
#     exit()

# #Užduotis 4-12

# dydis=int(input('Kiek eilučių: '))
# for i in range(dydis+1):
#     for j in range(i):
#         print(end='*')
#     print('')

# #Užduotis 5-13

# dydis=int(input('Kiek eilučių: '))
# zodis=input('Pasirinkite savo žody: ')
# for r in zodis:
#     print(r*dydis)

#Užduotis 5-14

# sk1=int(input('Skaičius 1: '))
# sk2=int(input('Skaičius 2: '))
# rezultatas=0
# for i in range(1,sk2+1):
#     rezultatas=rezultatas+sk1
# print(f'Sudaugintas skaičius yra: {rezultatas}')
