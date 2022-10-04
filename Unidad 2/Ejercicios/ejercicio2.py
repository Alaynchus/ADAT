import csv

def mostrarmenu():
    opcion = (int)(input(print(""" Que deseas hacer?
               1. Genera fichero de las olimpiadas
               2. Buscar deportista
               3. Buscar depotistas por deporte y olimpiada""")))
    if (opcion == 1):
        leerFichero()
    elif (opcion == 2):
        buscardepor()
    #elif (opcion == 3)

def leerFichero():
    with open("athlete_events.csv", newline="") as archivocsv:
        readerar = csv.DictReader(archivocsv)
        listaolim=[]
        with open("olimpiadas.csv", "w") as olimpadascsv:
            listacabezera = ["Games", "Season", "City", "Year"]
            writerar = csv.DictWriter(olimpadascsv, listacabezera)

            writerar.writeheader()
            for row in readerar:
                juego=row["Games"]
                if(juego not in listaolim):
                    listaolim.append(juego)
                    writerar.writerow({listacabezera[0]:row["Games"],listacabezera[1]: row["Season"], listacabezera[2]:row["City"], listacabezera[3]:row["Year"]})
                    print(row["Games"], row["Season"], row["City"], row["Year"])

            olimpadascsv.close()
        archivocsv.close()

def buscardepor():
    with open("athlete_events.csv", newline="") as archivocsv:
        readerar = csv.DictReader(archivocsv)
        cadena = input(print("Introduce una cadena por la que quieras buscar"))
        for row in readerar:
            nombre=row["Name"]
            if(cadena in nombre):
                print(row["Name"])
mostrarmenu()