import csv

def mostrarmenu():
    opcion = (int)(input(print(""" Que deseas hacer?
               1. Crear un fichero XML de olimpiadas
               2. Crear un fichero XML  de deportistas
               3. Listado de olimpiadas""")))
    if (opcion == 1):
        olimpiadasXML()
    #elif (opcion == 2):

    #elif (opcion == 3):

    #elif opcion == 4:

def olimpiadasXML():
    olimpiadas = []
    with open("olimpiadas.csv") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            olimpiadas = sorted(olimpiadas, key=lambda x: x["Season"], reverse=True)
            olimpiadas = sorted(olimpiadas, key=lambda x: x["Year"])

