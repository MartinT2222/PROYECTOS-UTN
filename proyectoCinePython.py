from Codigo_Espanol import *
from Codigo_Ingles import *


idioma= str(input("Elija Idioma Espanol o Ingles : "))

while (idioma != "espanol") and (idioma != "ingles"):
    print("Error. Deberia ser espanol o ingles")
    idioma = str(input("Digite nuevamente: "))
if idioma == "espanol":
    codigoEspanol()
elif idioma == "ingles":
    codigoIngles()







