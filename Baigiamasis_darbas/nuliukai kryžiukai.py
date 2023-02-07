# dvieju žaidėjų kryžiukai nuliukai

šilentelė = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }

lentelės_simbolis = []

for simbolis in šilentelė:
    lentelės_simbolis.append(simbolis)

def spausdintiLentele(lentelė):
    print(lentelė['7'] + '|' + lentelė['8'] + '|' + lentelė['9'])
    print('-+-+-')
    print(lentelė['4'] + '|' + lentelė['5'] + '|' + lentelė['6'])
    print('-+-+-')
    print(lentelė['1'] + '|' + lentelė['2'] + '|' + lentelė['3'])

# pagrindinė funkcija/žaidimo logika
def žaidimas():

    ėjimas = 'X'
    skaičiuoja = 0


    for i in range(10):
        spausdintiLentele(šilentelė)
        print("Jūsų eilė," + ėjimas + ".kur padėti?")

        žingsnis = input()        

        if šilentelė[žingsnis] == ' ':
            šilentelė[žingsnis] = ėjimas
            skaičiuoja += 1
        else:
            print("ši vieta jau užpildyta.\nkur padėti?")
            continue

        # patikrinu ar žaidėjas X ar žaidėjas O laimėjo, kiekvieną kartą po 5 ėjimų
        if skaičiuoja >= 5:
            if šilentelė['7'] == šilentelė['8'] == šilentelė['9'] != ' ': # per viršutini
                spausdintiLentele(šilentelė)
                print("\nžaidimas Baigtas.\n")                
                print(" **** " +ėjimas + " Laimėjo. ****")                
                break
            elif šilentelė['4'] == šilentelė['5'] == šilentelė['6'] != ' ': # per vidurini
                spausdintiLentele(šilentelė)
                print("\nžaidimas Baigtas.\n")                
                print(" **** " +ėjimas + " Laimėjo. ****")
                break
            elif šilentelė['1'] == šilentelė['2'] == šilentelė['3'] != ' ': # per apatini
                spausdintiLentele(šilentelė)
                print("\nžaidimas Baigtas.\n")                
                print(" **** " +ėjimas + " Laimėjo. ****")
                break
            elif šilentelė['1'] == šilentelė['4'] == šilentelė['7'] != ' ': # apatinė dešinė pusė
                spausdintiLentele(šilentelė)
                print("\nžaidimas Baigtas.\n")                
                print(" **** " +ėjimas + " Laimėjo. ****")
                break
            elif šilentelė['2'] == šilentelė['5'] == šilentelė['8'] != ' ': # vidurinis
                spausdintiLentele(šilentelė)
                print("\nžaidimas Baigtas.\n")                
                print(" **** " +ėjimas + " Laimėjo. ****")
                break
            elif šilentelė['3'] == šilentelė['6'] == šilentelė['9'] != ' ': # apatinė kairė pusė
                spausdintiLentele(šilentelė)
                print("\nžaidimas Baigtas.\n")                
                print(" **** " +ėjimas + " Laimėjo. ****")
                break 
            elif šilentelė['7'] == šilentelė['5'] == šilentelė['3'] != ' ': # istryžai
                spausdintiLentele(šilentelė)
                print("\nžaidimas Baigtas\n")                
                print(" **** " +ėjimas + " Laimėjo. ****")
                break
            elif šilentelė['1'] == šilentelė['5'] == šilentelė['9'] != ' ': # istryžai
                spausdintiLentele(šilentelė)
                print("\nžaidimas Baigtas.\n")                
                print(" **** " +ėjimas + " Laimėjo. ****")
                break 

        #  Jai nei X nei O laimėjo ir lentelė pilna, paskelbtos lygiosios
        if skaičiuoja == 9:
            print("\nžaidimas Baigtas.\n")                
            print("Lygiosios!!")

        # Apkeičiami žaidėjai po ėjimo.
        if ėjimas =='X':
            ėjimas = 'O'
        else:
            ėjimas = 'X'        
    
    # Ar žaidėnas nori pradėti žaisti iš kaujo.
    testi = input("Norite žaisti darkartą?(t/n)")
    if testi == "t" or testi == "T":  
        for simbolis in lentelės_simbolis:
            šilentelė[simbolis] = " "

        žaidimas()
# ar kodas vietinis ar importuotas(sudėtas per if)
if __name__ == "__main__": 
    žaidimas()