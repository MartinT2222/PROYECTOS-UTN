def matriz(cantidadEntradas):
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
            numeroMod = int(input("Seleccione su butaca: "))
            
            if numeroMod not in arrayButaca:
                arrayButaca.append(numeroMod)
                x += 1
            else:
                print("El número está repetido, inténtelo con otro...")
                numeroMod = int(input("Seleccione su butaca: "))
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
            print("Escriba la sigiente butaca: ")


    return arrayButaca

def seleccionPelicula():
    num4 = int(input("Digite su opcion de pelicula: "))
    while (0 >= num4 or num4 > 3):
        num4 = int(input("Opción incorrecta. Por favor, digite nuevamente: "))
    if num4 == 1:
        peli = "SONIC 2 LA PELÍCULA."
    elif num4 == 2:
        peli = "RÁPIDOS Y FURIOSOS 9."
    elif num4 == 3:
        peli = " MORBIUS."

    return peli

def cartillaPeliculaEspanol():
    print("GRACIAS POR SU CONFIRMACION!")
    print("")
    print("Los precios de las entradas son los siguientes:")
    print("MAYORES DE 18 AÑOS: $200")
    print("MENORES DE 18 AÑOS $150")
    print("")
    print("A CONTINUACIÓN, LE OFRECEMOS LA SIGUIENTE CARTELERA: ")
    print("Opción 1: SONIC 2 LA PELÍCULA.")
    print("Opción 2: RÁPIDOS Y FURIOSOS 9.")
    print("Opción 3: MORBIUS.")

def precio(entradaMayores, entradaMenores):
    precioMayor = entradaMayores *200
    precioMenor = entradaMenores * 150
    
    return precioMayor + precioMenor

def entradas(entradaMayores, entradaMenores):
    return entradaMayores + entradaMenores
   
def entradaMay(entrada, entradaMenores):
    return entrada - entradaMenores

def horarioEspanol():
    print("Por favor, seleccione el horario en el que desea asistir:")
    print("   1.- 3:00 pm.")
    print("   2.- 5:00 pm.")
    print("   3.- 7:00 pm.")
    print("   4.- 9:00 pm.")
    jornada = int(input("Digite el horario de su pelicula: "))
    while (0 >= jornada or jornada > 4):
        jornada = int(input("Opción incorrecta. Por favor, digite nuevamente: "))
    if jornada == 1:
        horas = "3:00 pm."
    elif jornada == 2:
        horas = "5:00 pm."
    elif jornada == 3:
        horas = "7:00 pm."
    elif jornada == 4:
        horas = "9:00 pm."
    return horas



def confirmacionEspanol():
    entrada = int(input("¿cuantas entradas desea comprar?: "))
    menores = int(input("¿Hay algun menor de edad? Por favor, digite la cantidad: "))
    entradaMenores = menores
    entradaMayores = entradaMay(entrada, entradaMenores)
    cantidadEntradas = entradas(entradaMayores, entradaMenores)
    precios= precio(entradaMayores, entradaMenores)
    cartillaPeliculaEspanol()
    pelis=seleccionPelicula()
    hora=horarioEspanol()
    arreglo= matriz(cantidadEntradas)
    print("Usted está por comprar la entrada de: ")
    print(f"Pelicula = {pelis}")
    print(f"Con un costo de = $ {precios}")
    print(f"Empieza a las = {hora}")
    print(f"En la/s butaca/s número/s =  {arreglo}")
    opc = ' '
    while (opc != "si" and opc != "no"):
        opc= str(input("¿Desea confirmar la compra? Si o NO "))
        if ( "si" == opc):
            print("¡¡¡ GRACIAS POR SU COMPRA !!!")
            print("")
            print("¡Los/as esperamos!")
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
            print("LO SENTIMOS. SU COMPRA NO PUDO REALIZARSE.")
    
    
def codigoEspanol ():
    
    opcion = 0
    while (opcion != 1 and opcion != 3):
        print("POR FAVOR, SELECCIONE LA OPERACIÓN QUE DESEA REALIZAR:")
        print("")
        print("1. COMPRAR UNA ENTRADA. ")
        print("2. VER LA CARTELERA Y PRECIOS. ")
        print("3. SALIR.")
        opcion = int(input())
        if opcion == 1:
            confirmacionEspanol()
        elif opcion == 2:
            cartillaPeliculaEspanol()
        


idioma= str(input("Elija Idioma Espanol o Ingles : "))

while (idioma != "espanol") and (idioma != "ingles"):
    print("Error. Deberia ser espanol o ingles")
    idioma = str(input("Digite nuevamente: "))
if idioma == "espanol":
    codigoEspanol()
elif idioma == "ingles":
    numidioma = 2







