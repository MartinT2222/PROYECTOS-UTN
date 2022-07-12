from codigo_Compartido import *

def matrizIngles(cantidadEntradas):
    matriz = [[10, 11, 12, 13, 14, 15, 16, 17, 18, 19],[20, 21, 22, 23, 24, 25, 26, 27, 28, 29],[30, 31, 32, 33, 34, 35, 36, 37, 38, 39],[40, 41, 42, 43, 44, 45, 46, 47, 48, 49]]
    b=""
    for i in range(4):
        for j in range(10):
            
            b += str(matriz[i][j])+ ' || '    
        print(b)
        b=""

    cantidadEntrada1 = 0
    cantidadEntrada = cantidadEntradas
    arrayButaca = []
    
    while (cantidadEntrada != cantidadEntrada1):
        numeroMod = 0
        x=1

        while ((numeroMod > 49 or numeroMod <= 9) and x <= cantidadEntrada):
            numeroMod = int(input("Please, select the position of the seat you want to sit:  "))
            
            if numeroMod not in arrayButaca:
                arrayButaca.append(numeroMod)
                x += 1
            else:
                print("The number is repeated, try another...")
                numeroMod = int(input("Please, select the position of the seat you want to sit: "))
                if numeroMod not in arrayButaca:
                    arrayButaca.append(numeroMod)


        for i in range(4):
            for j in range(10):
                if (matriz[i][j] == numeroMod):
                    matriz[i][j] = 99
        for i in range(4):
            for j in range(10):
                
                b += str(matriz[i][j])+ ' || '    
            print(b)
            b=""        

        
        cantidadEntrada = cantidadEntrada -1 
        

        if (cantidadEntrada != cantidadEntrada1):
            print("Write the next seat: ")


    return arrayButaca

def seleccionPeliculaIngles():
    num4 = int(input("NEXT, WE OFFER YOU THE FOLLOWING MOVIE BILLBOARD: "))
    while (0 >= num4 or num4 > 3):
        num4 = int(input("Wrong option. Please type again: "))
    if num4 == 1:
        peli = "SONIC 2 LA PELÍCULA."
    elif num4 == 2:
        peli = "RÁPIDOS Y FURIOSOS 9."
    elif num4 == 3:
        peli = " MORBIUS."

    return peli

def cartillaPeliculaIngles():
    print("THANKS FOR YOUR CONFIRMATION!")
    print("")
    print("The ticket prices are as follows:")
    print("OLDER THAN 18 YEARS OLD: $200")
    print("YOUNGER THAN 18 YEARS OLD: $150")
    print("")
    print("NEXT, WE OFFER YOU THE FOLLOWING MOVIE BILLBOARD:  ")
    print("Optión 1: SONIC 2 LA PELÍCULA.")
    print("Optión 2: RÁPIDOS Y FURIOSOS 9.")
    print("Optión 3: MORBIUS.")


def horarioIngles():
    print("Select the time you want to assist, please:")
    print("   1.- 3:00 pm.")
    print("   2.- 5:00 pm.")
    print("   3.- 7:00 pm.")
    print("   4.- 9:00 pm.")
    jornada = int(input("Wrong choice. Please, type again:"))
    while (0 >= jornada or jornada > 4):
        jornada = int(input("Wrong option. Please type again: "))
    if jornada == 1:
        horas = "3:00 pm."
    elif jornada == 2:
        horas = "5:00 pm."
    elif jornada == 3:
        horas = "7:00 pm."
    elif jornada == 4:
        horas = "9:00 pm."
    return horas



def confirmacionIngles():
    entrada = int(input("How many tickets do you want to buy? = "))
    menores = int(input("Is there any younger? Enter the cuantity ?, please = "))
    entradaMenores = menores
    entradaMayores = entradaMay(entrada, entradaMenores)
    cantidadEntradas = entradas(entradaMayores, entradaMenores)
    precios= precio(entradaMayores, entradaMenores)
    cartillaPeliculaIngles()
    pelis=seleccionPeliculaIngles()
    hora=horarioIngles()
    arreglo= matrizIngles(cantidadEntradas)
    print("You are about to buy the entrance of: ")
    print(f"Movie =  {pelis}")
    print(f"Whith a cost of = $ {precios}")
    print(f"Start at = {hora}")
    print(f"In the seats numbers =  {arreglo}")
    opc = ' '
    while (opc != "yes" and opc != "no"):
        opc= str(input("¿You want to confirm the purchase? YES o NO "))
        if ( "yes" == opc):
            print("¡¡¡ Thanks for your purchase !!!")
            print("")
            print(" We wait for you!")
            print("")
            print("*-FACUNDO MARTÍN GIACOMOZZI-* ")
            print("*-MATÍAS CANEVARO* ")
            print("*-MARTÍN ALEJANDRO TORRES-*")
            print("*-EDUARDO LUIS GÓMEZ-*")
            print("*-CINTHIA FERNANDA SEGOVIA-*")
            print("*-GABRIEL ROMERO-*")
            print("*-AGUSTÍN RODRÍGUEZ ÁLVAREZ-*")
            print("*-LAUTARO URQUIZA-*")
            print("*-SABRINA MANTERO-*")
        elif ( "no" == opc):
            print("WE ARE SORRY, YOUR PURCHASE COULD NOT BE COMPLETED.")
    
    
def codigoIngles ():
    
    opcion = 0
    while (opcion != 1 and opcion != 3):
        print("¡¡¡WELCOME TO THE MATE-CODERS CINEMA")
        print("SELECT THE OPERATION YOU WANT TO DO, PLEASE:")
        print("")
        print("1. BUY A TICKET.  ")
        print("2. SEE MOVIE BILLBOARD.  ")
        print("3. EXIT. ")
        opcion = int(input())
        if opcion == 1:
            confirmacionIngles()
        elif opcion == 2:
            cartillaPeliculaIngles()
        elif opcion == 3:
            print("THANK YOU FOR VISITING US.")
        