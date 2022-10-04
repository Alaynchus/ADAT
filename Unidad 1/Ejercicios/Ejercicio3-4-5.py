from statistics import mean

def sumatorio(pramlista):
    print(sum(pramlista))

def media(pramlista):
    print(mean(pramlista))

def maximo(pramlista):
    print(max(pramlista))

def minimo(pramlista):
    print(min(pramlista))

def salir():
    print("Has salido")

lista = []
for cont2 in range(3):
    variab = (int)(input("Introduce un número"))
    while variab%2==0:
        variab = (int)(input("Introduce un número impar"))
    lista.append(variab)
opcion = (int)(input("""Que desea hacer con la lista?
        1. Sumatorio
        2. Media
        3. Máximo 
        4. Minimo

        0. Salir"""));

while opcion < 0 or opcion > 4:
    opcion = (int)(input("Introduce un numero del 0 al 4"))
if opcion == 1:
    sumatorio(lista)
elif opcion == 2:
    media(lista)
elif opcion == 3:
    maximo(lista)
elif opcion == 4:
    minimo(lista)
else:
    salir()

