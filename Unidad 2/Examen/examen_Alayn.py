import csv
import pickle
from xml.etree import ElementTree as ET
from xml.dom import minidom

def mostrarmenu():
    opcion = (input(""" Que deseas hacer?
                   1. Buscar batallas por región
                   2. Crear XML batallas
                   3. Crear fichero binario objetos
                   4. Eliminar battalla fic. Binario objetos
                   0. Salir"""))
    if (opcion == "1"):
        listarbatallasregion()
    elif opcion == "2":
        crearBattlesXML()
    elif opcion == "3":
        crearFicheroSerializable()
    elif opcion == "4":
        borrarBattalaFichero()
    elif opcion == "0":
        exit()
    else:
        print("Introduce un valor correcto")
        mostrarmenu()
def listarbatallasregion():
    regionpedida=input("Introduce la region que desees")
    cont=0
    with open("battles.csv", newline="") as archivocsv:
        readerar= csv.DictReader(archivocsv)
        for row in readerar:
            if regionpedida==row["region"]:
                print("Region: "+row["region"])
                print("Localización: "+row["location"])
                print("Nombre de la batalla: "+row["name"])
                print("Año: "+ row["year"])
                if row["attacker_king"]=="":
                    print("Rey atacante: no king")
                else:
                    print("Rey atacante: "+row["attacker_king"])

                if row["defender_king"]=="":
                    print("Rey defensor: no king")
                else:
                    print("Rey defensor: "+row["defender_king"])
                print("Resultado de la batalla: "+row["attacker_outcome"])
                print("")
                cont=1
    if cont==0:
        print("No se ha encontrado esa region")
    mostrarmenu()

def crearBattlesXML():
    batallas=[]
    with open("battles.csv") as archivocsv:
        reader=csv.DictReader(archivocsv)
        for row in reader:
            batallas.append(row)
        root= ET.Element("juego_tronos")
        for bata in batallas:
            batalla= ET.Element("batalla")
            batalla.set("id", bata["battle_number"])
            nombre= ET.SubElement(batalla,"nombre")
            nombre.text = bata["name"]
            anio = ET.SubElement(batalla, "anio")
            anio.text = bata["year"]
            region = ET.SubElement(batalla, "region")
            region.text = bata["region"]
            localizacion = ET.SubElement(batalla, "localizacion")
            if bata["location"]=="":
                localizacion.text = "Sin localicacion"
            else:
                localizacion.text = bata["location"]
            ataque = ET.SubElement(batalla, "ataque")
            ataque.set("tamanio", bata["attacker_size"])
            if bata["attacker_outcome"]=="win":
                ataque.set("gana", "si")
            elif bata["attacker_outcome"]=="loss":
                ataque.set("gana", "no")
            else:
                ataque.set("gana", "NA")

            rey = ET.SubElement(ataque, "rey")
            if bata["attacker_king"]=="":
                rey.text = "No King"
            else:
                rey.text = bata["attacker_king"]

            comandante = ET.SubElement(ataque, "comandante")
            comandante.text = bata["attacker_commander"]
            familia1 = ET.SubElement(ataque, "familia")
            familia1.text = bata["attacker_1"]
            if bata["attacker_2"]!="":
                familia2 = ET.SubElement(ataque, "familia")
                familia2.text = bata["attacker_2"]
            if bata["attacker_3"]!="":
                familia3 = ET.SubElement(ataque, "familia")
                familia3.text = bata["attacker_3"]
            if bata["attacker_4"]!="":
                familia4 = ET.SubElement(ataque, "familia")
                familia4.text = bata["attacker_4"]

            defensa = ET.SubElement(batalla, "defensa")
            defensa.set("tamanio", bata["defender_size"])
            if bata["attacker_outcome"] == "win":
                defensa.set("gana", "no")
            elif bata["attacker_outcome"] == "loss":
                defensa.set("gana", "si")
            else:
                defensa.set("gana", "NA")

            rey = ET.SubElement(defensa, "rey")
            if bata["defender_king"] == "":
                rey.text = "No King"
            else:
                rey.text = bata["defender_king"]

            comandante = ET.SubElement(defensa, "comandante")
            comandante.text = bata["defender_commander"]
            familia1 = ET.SubElement(defensa, "familia")
            familia1.text = bata["defender_1"]
            if bata["defender_2"] != "":
                familia2 = ET.SubElement(defensa, "familia")
                familia2.text = bata["defender_2"]
            if bata["defender_3"] != "":
                familia3 = ET.SubElement(defensa, "familia")
                familia3.text = bata["defender_3"]
            if bata["defender_4"] != "":
                familia4 = ET.SubElement(defensa, "familia")
                familia4.text = bata["defender_4"]

            root.append(batalla)
        todostr=minidom.parseString(ET.tostring(root)).toprettyxml(indent="\t")
        f=open("battles.xml", "w")
        f.write(todostr)
        f.close()
        print("Se ha creado el archivo xml")
    mostrarmenu()

class Batalla:
    def __init__(self, id, nombre, anio, region, localizacion, rey_atacante, rey_defensor, gana):
        self.id = id
        self.nombre = nombre
        self.anio = anio
        self.region = region
        self.localizacion = localizacion
        self.rey_atacante = rey_atacante
        self.rey_defensor = rey_defensor
        self.gana = gana
    def __str__(self):
        return("The "+self.nombre+" took place in "+self.localizacion+" ("+self.region+") in the year "+self.anio+". The King(s) "+self.rey_atacante+" fought against "+self.rey_defensor+" and he/they "+self.gana)

def crearFicheroSerializable():
    raiz=ET.parse("battles.xml").getroot()
    listaBata = raiz.findall("batalla")
    with open("battles.bin", "wb") as pickle_file:
        for bata in listaBata:
            id= bata.get("id")
            nombre= bata.find("nombre").text
            anio = bata.find("anio").text
            region = bata.find("region").text
            localizacion = bata.find("localizacion").text
            ata=bata.find("ataque")
            rey_atacante = ata.find("rey").text
            gana = ata.get("gana")
            defen = bata.find("defensa")
            rey_defensor= defen.find("rey").text

            batallanueva= Batalla(id, nombre, anio, region, localizacion, rey_atacante, rey_defensor, gana)
            pickle.dump(batallanueva, pickle_file)
    print("Se ha creado el archivo binario")
    mostrarmenu()

def borrarBattalaFichero():
    idintroducido = input("Introduce un identificador de batalla")
    listabata=[]
    confirmador=False
    with open("battles.bin", "rb") as archivobin:
        while True:
            try:
                listabata.append(pickle.load(archivobin))
            except EOFError:
                break
    with open("battles.bin", "wb") as archivobin:
        for bata in listabata:
            if idintroducido!=bata.id:
                pickle.dump(bata, archivobin)
            else:
                print(bata)
                resp = input("Deseas eliminarla?(SI o NO)")
                confirmador = True
                while resp!="SI" and resp != "NO":
                    resp=input("Respuesta incorrecta introduce SI o NO")
                if resp=="SI":
                    print("Ha sido borrada con exito")
                elif resp=="NO":
                    pickle.dump(bata, archivobin)
                    print("No ha sido borrada")


    if confirmador == False:
        print("No existe ninguna batalla con es identificador")
    mostrarmenu()

mostrarmenu()