import csv
from xml import sax
from xml.etree import ElementTree as ET
from xml.dom import minidom

from parseador import parseador


def mostrarmenu():
    opcion = (int)(input(print(""" Que deseas hacer?
               1. Crear un fichero XML de olimpiadas
               2. Crear un fichero XML  de deportistas
               3. Listado de olimpiadas""")))
    if (opcion == 1):
        olimpiadasXML()
    elif (opcion == 2):
        metodo2()
    elif (opcion == 3):
        metodo3()

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


def metodo2():
    olimpiadas = []
    with open("athlete_events_reducido.csv") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            olimpiadas.append(row)
        print(len(olimpiadas))
    # olimpiadas = sorted(olimpiadas, key=lambda x: x["ID"])
    lista = []
    ldeporte = []

    root = ET.Element("deportistas")
    for o in olimpiadas:
        if o["Name"] not in lista:
            lista.append(o["Name"])
            deportista = ET.Element("deportista")
            deportista.set("id", o["ID"])
            root.append(deportista)

            nombre = ET.SubElement(deportista, "nombre")
            nombre.text = o["Name"]
            sexo = ET.SubElement(deportista, "sexo")
            sexo.text = o["Sex"]
            altura = ET.SubElement(deportista, "altura")
            altura.text = o["Height"]
            peso = ET.SubElement(deportista, "peso")
            peso.text = o["Weight"]
            participaciones = ET.SubElement(deportista, "participaciones")
            ldeporte.clear()

        if not o["Sport"] in ldeporte:
            ldeporte.append(o["Sport"])
            deporte = ET.SubElement(participaciones, "deporte")
            deporte.set("nombre", o["Sport"])

        participacion = ET.SubElement(deporte, "participacion")
        participacion.set("edad", o["Age"])

        equipo = ET.SubElement(participacion, "equipo")
        equipo.set("abbr", o["NOC"])
        equipo.text = o["Team"] + " - " + o["City"]
        juegos = ET.SubElement(participacion, "evento")
        juegos.text = o["Games"]
        evento = ET.SubElement(participacion, "evento")
        evento.text = o["Event"]
        medalla = ET.SubElement(participacion, "medalla")
        medalla.text = o["Medal"]

    str = minidom.parseString(ET.tostring(root)).toprettyxml(indent="\t")
    f = open("aaaaaaaa.xml", "w")
    f.write(str)
    f.close
    print(len(lista))
    print(lista)


def metodo3():
    ejemp = parseador()
    sax.parse("olimpiadas.xml", ejemp)



mostrarmenu()
