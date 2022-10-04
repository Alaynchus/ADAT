import math
import random


class Persona:
    def __init__(self, nombre = "", edad = 0 , sexo = "H" , peso = 0, altura = 0):
        self.__nombre = nombre
        self.__edad = edad
        self.__dni = self.__generaDNI()
        self.__sexo = sexo
        self.__peso = peso
        self.__altura = altura

    def calcularIMC(self):
        imc=self.__peso / (self.__altura ** 2)

        if imc<20:
            return -1
        elif imc<=25 and imc>=20:
            return 0
        else:
            return 1

    def esMayorDeEdad(self):
        if self.__edad>18:
            return True
        else:
            return False

    def toString(self):
        print("Nombre:"+self.__nombre+" edad:",(self.__edad)," DNI:"+self.__dni+" sexo:"+self.__sexo+" peso:",(self.__peso)," altura:",(self.__altura))

    def __generaDNI(self):
        numero = random.randint(10000000, 99999999)
        letra = chr(random.randint(65, 90))
        total = (str)(numero) + letra
        return total

    def __setNombre(self, nom):
        self.__nombre= nom

    def __setEdad(self, ed):
        self.__edad= ed

    def __setSexo(self, se):
        self.__sexo= se

    def __getNombre(self, nom):
        return self.__nombre


    def __getNombre(self, nom):
        return self.__nombre

    def __getEdad(self, ed):
        return self.__edad

    def __getSexo(self, se):
        return self.__sexo

    nombre= property(__getNombre, __setNombre)
persona1 = Persona("Ramon", 19, "M", 1.85, 90);
print(persona1.esMayorDeEdad())
persona1.toString()

