import csv
from xml.etree import ElementTree as ET
from xml.dom import minidom

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
            olimpiadas.append(row)
        olimpiadas = sorted(olimpiadas, key=lambda x: x["Year"])
        olimpiadas = sorted(olimpiadas, key=lambda x: x["Season"], reverse=True)

        root = ET.Element("olimpiadas")
        for olim in olimpiadas:
               anio = ET.Element("olimpiada")
               anio.set("Year",olim['Year'])
               juego = ET.SubElement(anio,"juegos")
               juego.text = olim['Games']
               Temporada = ET.SubElement(anio, "Temporada")
               Temporada.text = olim['Season']
               Ciudad = ET.SubElement(anio, "Ciudad")
               Ciudad.text = olim['City']
               root.append(anio)
        todostr = minidom.parseString(ET.tostring(root)).toprettyxml(indent="\t")
        f = open("olimpiadas.xml", "w")
        f.write(todostr)
        f.close()

def deportistasXML():
    deportistas = []
    with open("athlete_events_reducido.csv") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            deportistas.append(row)
        root = ET.Element("deportista")
        for depor in deportistas:
            deportista = ET.Element("deportista")
            deportista.set("id", depor["ID"])
            nombre = ET.SubElement("nombre")
            nombre.text = depor["Name"]
            sexo = ET.SubElement("sexo")
            sexo.text = depor["Sex"]

mostrarmenu()
