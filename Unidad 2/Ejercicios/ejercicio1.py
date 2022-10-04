import os.path
import shutil


class Menu:
    def mostrarmenu(self):
        opcion = (int)(input(print(""" Que deseas hacer?
                1. Crea un directorio
                2. Lista un directorio
                3. Copiar un archivo
                4. Mover un archivo
                5. Eliminar un archivo/directorio
                6. Salir del programa""")))
        if (opcion == 1):
            self.crearDirectorio()
        elif (opcion == 2):
            self.listarUnDirectorio()
        elif (opcion==3):
            self.copiarArchivo()
        elif (opcion==4):
            self.moverArchivo()
        elif (opcion==5):
            self.eliminarArchDir()
        else:
            print("Has salido")
    def crearDirectorio(self):
        ruta = input(print("Introduce la ruta del directorio"))
        nombreDir = input(print("Introduce el nombre del nuevo directorio"))
        if not(os.path.exists(ruta)):
            print("No es una ruta")
        else:
            os.mkdir(os.path.join(ruta, nombreDir))
        self.mostrarmenu()
    def listarUnDirectorio(self):
        ruta = input(print("Introduce la ruta del directorio"))
        if not(os.path.exists(ruta)):
            print("No es una ruta")
        else:
            lista = os.scandir(ruta)
            print(lista)
        for elemento in lista:
            if(os.path.isdir(elemento)):
                print("Directorio: ",elemento)
            else:
                print("Archivo: ", elemento)
        self.mostrarmenu()

    def copiarArchivo(self):
        rutanueva = input(print("Introduce la ruta del destino"))
        rutaarchi = input(print("Introduce la ruta del  archivo que quieras copiar"))
        if not(os.path.exists(rutaarchi)):
            print("No es una ruta")
        else:
            shutil.copy(rutaarchi, rutanueva);
        self.mostrarmenu()

    def moverArchivo(self):
        rutanueva = input(print("Introduce la ruta del destino"))
        rutaarchi = input(print("Introduce la ruta del  archivo que quieras mover"))
        if not(os.path.exists(rutaarchi)):
            print("No es una ruta")
        else:
            shutil.move(rutaarchi, rutanueva)
        self.mostrarmenu()

    def eliminarArchDir(self):
        ruta = input(print("Introduce la ruta del directorio o ruta que deseas eliminar"))
        if not(os.path.exists(ruta)):
            print("No es una ruta")
        else:
            if(os.path.isfile(ruta)):
                os.remove(ruta)
            else:
                #lista = os.listdir(ruta)
                #if(len(lista) != 0):
                 #   print("Este directorio tiene cosas dentro")
                #else:
                try:
                    os.rmdir(ruta)
                except(OSError):
                    print("No se ha podido borrar")
        self.mostrarmenu()


m1 = Menu()
m1.mostrarmenu()
