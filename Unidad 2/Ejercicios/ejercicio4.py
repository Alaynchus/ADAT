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
    opcion = (int)(input(print(""" Que deseas hacer?
               1. Crear un fichero serializable de olimpiadas
               2. Añadir edición olímpica
               3. Buscar olimpiadas por sede
               4. Eliminar edición olímpica
               5. Cerrar""")))
    if (opcion == 1):
        crearFicheroSerializable()
    elif (opcion == 2):
        añadirEdicion()
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
    anio = input(print("Introduce el año de la olimpiada"))
    juegos = input(print("Introduce los juegos"))
    temporada = input(print("Introduce la temporada de la olimpiada"))
    ciudad = input(print("Introduce la ciudad de la olimpiada"))
    olimpiadanueva = Olimpiada(anio, juegos, temporada, ciudad)
    with open("olimpiadas.pickle", "ab") as f:
        pickle.dump(olimpiadanueva, f)
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
    anio = input(print("Introduce el año de la olimpiada"))
    temporada = input(print("Introduce la temporada de la olimpiada"))
    with open("olimpiadas.pickle", "")as f:

mostrarmenu()
leerficheroseri()
