import csv

def mostrarmenu():
    opcion = (int)(input(print(""" Que deseas hacer?
               1. Genera fichero de las olimpiadas
               2. Buscar deportista
               3. Buscar depotistas por deporte y olimpiada
               4. Añadir persona""")))
    if (opcion == 1):
        leerFichero()
    elif (opcion == 2):
        buscarDeportista()
    elif (opcion == 3):
        buscarDeporPorOlim()
    elif opcion == 4:
        anadirPersona()

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

def buscarDeportista():
    with open("athlete_events.csv", newline="") as archivocsv:
        readerar = csv.DictReader(archivocsv)
        cadena = input(print("Introduce una cadena por la que quieras buscar"))
        ultnom = ""
        cont=0
        for row in readerar:
            nombre = row["Name"]
            if cadena in nombre and ultnom != nombre:
                ultnom=row["Name"]
                print(row["Name"])
                print("\t" + row["Games"] + row["City"] + row["Event"])
                cont=1
            elif ultnom == nombre:
                print("\t" + row["Games"] + " " + row["City"] + " " + row["Event"])
        if cont == 0:
            print("No hay deportistas con esa cadena")

def buscarDeporPorOlim():
    with open("athlete_events.csv", newline="") as archivocsv:
        readerar = csv.DictReader(archivocsv)
        deporteusu = input(print("Introduce un deporte"))
        aniousu = input(print("Introduce un año"))
        temporadausu = input(print("Introduce una temporada"))
        ultnom = ""
        cont = 0
        for row in readerar:
            nombre = row["Name"]
            if deporteusu == row["Sport"] and aniousu == row["Year"] and temporadausu == row["Season"]:
                if cont == 0:
                    cont = 1
                    print(row["Games"] + " " + row["City"] + " " + row["Sport"])
                print("\t" + row["Name"] + " " + row["Event"] + " " + row["Medal"])
        if cont == 0:
            print("No se ha encontrado ningún resultado")

def anadirPersona():
    idusu = input(print("Introduce un id"))
    nombreusu = input(print("Introduce un nombre"))
    saxusu = input(print("Introduce un sexo"))
    edadusu = input(print("Introduce un edad"))
    alturausu = input(print("Introduce una altura"))
    pesousu = input(print("Introduce un peso"))
    equipousu = input(print("Introduce un equipo"))
    siglasusu = input(print("Introduce sus siglas del equipo"))
    juegosusu = input(print("Introduce unos juegos"))
    ciudadusu = input(print("Introduce una ciudad"))
    eventousu = input(print("Introduce un evento"))
    medallausu = input(print("Introduce su medalla"))
    deporteusu = input(print("Introduce un deporte"))
    aniousu = input(print("Introduce un año"))
    temporadausu = input(print("Introduce una temporada"))
    with open("athlete_events.csv", "a") as archivocsv:
        columnas=["ID", "Name", "Sex", "Age","Height","Weight","Team","NOC","Games","Year","Season","City","Sport","Event","Medal"]
        writerar = csv.DictWriter(archivocsv, columnas)
        writerar.writeheader()
        writerar.writerow({columnas[0]: "100000000000", columnas[1]: "Adrian Llahe", columnas[2]: "M", columnas[3]: "22", columnas[4]: "170", columnas[5]: "35", columnas[6]: "España", columnas[7]: "ESP", columnas[8]: "Vitoria 2022", columnas[9]: "2022", columnas[10]: "Summer", columnas[11]: "Vitoria", columnas[12]: "Lanzamiento de piedras", columnas[13]: "Lanzamiento de piedras M", columnas[14]: "GOOOLD"})


mostrarmenu()