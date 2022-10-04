class Cryptograofo:

    def encriptar(self, txt):
        palabra = ""
        for caracter in txt:
            letra = ord(caracter) + 1
            palabra= palabra + chr(letra)
        print(palabra)

    def desencriptar(self, txt):
        palabra = ""
        for caracter in txt:
            letra = ord(caracter) - 1
            palabra = palabra + chr(letra)
        print(palabra)

texto = input("Introduce un texto para encriptar")
cry =Cryptograofo()
cry.encriptar(texto)
texto = input("Introduce un texto para desencriptar")
cry.desencriptar(texto)