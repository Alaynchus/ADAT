import pickle
from xml.etree import ElementTree as ET
from xml.dom import minidom

class Olimpiada:

    def __init__(self, anio, juegos, temporada, ciudad):
        self.anio = anio
        self.juegos = juegos
        self.temporada = temporada
        self.ciudad = ciudad
    def verOlimpiada(self):
        print(self.anio ," ", self.juegos, " ", self.temporada, " ", self.ciudad)

def mostrarmenu():
    opcion = (int)(input(""" Que deseas hacer?
               1. Crear un fichero serializable de olimpiadas
               2. Añadir edición olímpica
               3. Buscar olimpiadas por sede
               4. Eliminar edición olímpica
               5. Cerrar"""))
    if (opcion == 1):
        crearFicheroSerializable()
    elif (opcion == 2):
        añadirEdicionOrdenado()
    elif (opcion == 3):
        buscarOlimpiadas()
    elif opcion == 4:
        eliminarEdicion()
    elif opcion == 5:
        exit()

def crearFicheroSerializable():
    raiz=ET.parse("olimpiadas.xml").getroot()
    listaolim=raiz.findall("olimpiada")
    pickle_file = open("olimpiadas.pickle", "wb")
    for olim in listaolim:
        anio = olim.get("Year")
        juegos = olim.find("juegos").text
        temporada = olim.find("Temporada").text
        ciudad = olim.find("Ciudad").text
        olimpiadanueva = Olimpiada(anio, juegos, temporada, ciudad)

        pickle.dump(olimpiadanueva, pickle_file)
    pickle_file.close()
    mostrarmenu()
def leerficheroseri():
    with open("olimpiadas.pickle", "rb") as f:
        while True:
            try:
                olimpiada = pickle.load(f)
                olimpiada.verOlimpiada()
            except EOFError:
                break

def añadirEdicion():
    anio = input("Introduce el año de la olimpiada")
    juegos = input(print("Introduce los juegos"))
    temporada = input("Introduce la temporada de la olimpiada")
    ciudad = input("Introduce la ciudad de la olimpiada")
    olimpiadanueva = Olimpiada(anio, juegos, temporada, ciudad)
    with open("olimpiadas.pickle", "ab") as f:
        pickle.dump(olimpiadanueva, f)
    mostrarmenu()

def añadirEdicionOrdenado():
    anio = input("Introduce el año de la olimpiada")
    juegos = input("Introduce los juegos")
    temporada = input("Introduce la temporada de la olimpiada")
    ciudad = input("Introduce la ciudad de la olimpiada")
    olimpiadanueva = Olimpiada(anio, juegos, temporada, ciudad)
    listaolimpOrdenada = []
    añadido = False
    with open("olimpiadas.pickle", "rb") as f:
        while True:
            try:
                olimpiada = pickle.load(f)
                if(anio < olimpiada.anio and añadido == False):
                    listaolimpOrdenada.append(olimpiadanueva)
                    añadido = True
                listaolimpOrdenada.append(olimpiada)
            except EOFError:
                break
    print(listaolimpOrdenada)
    with open("olimpiadas.pickle", "wb") as f:
        for olim in listaolimpOrdenada:
            pickle.dump(olim, f)
    leerficheroseri()
    mostrarmenu()


def buscarOlimpiadas():
    sedeBuscar = input(print("Introduce la sede de la olimpiada"))
    listaselec = []
    with open("olimpiadas.pickle", "rb") as f:
        while True:
            try:
                olimpiada = pickle.load(f)
                if sedeBuscar in olimpiada.ciudad:
                    listaselec.append(olimpiada)
            except EOFError:
                break
        for olim in listaselec:
            print("Año: "+olim.anio+" Juegos: "+olim.juegos+ " Temporada: "+olim.temporada+" Ciudad: "+olim.ciudad)
    mostrarmenu()

def eliminarEdicion():
    anio = input("Introduce el año de la olimpiada")
    temporada = input("Introduce la temporada de la olimpiada")
    listaolimp = []
    confirmador = False
    with open("olimpiadas.pickle", "rb")as f:
        while True:
            try:
                listaolimp.append(pickle.load(f))
            except EOFError:
                break
    with open("olimpiadas.pickle", "wb") as f:
        for olim in listaolimp:
            if (temporada != olim.temporada or anio != olim.anio):
                pickle.dump(olim, f)
            else:
                confirmador = True

    if(confirmador == False):
        print("No existe ninguna olimpada con el año "+ anio + " en la temporada "+ temporada)
    mostrarmenu()



mostrarmenu()
leerficheroseri()
