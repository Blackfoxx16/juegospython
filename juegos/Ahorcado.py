import random
import string
from juegos.AhorcadoResources.PalabrasAhorcado import palabras
class Ahorcado():

    def __init__(self):
        print("=====================================")
        print("Bienvenido(a) al juego del ahorcado")
        print("=====================================")

        self.__palabra = self.__obtener_palabra_valida(palabras)

        self.__letras_por_adivinar = set(self.__palabra)
        self.__letras_adivinadas = set()
        self.__abecedario = set(string.ascii_uppercase)
        self.__vidas = 7


    def jugar(self):
        print(self.__palabra)


    #Selecciona una palabra válida del listado de palabras
    def __obtener_palabra_valida(self, lista_de_palabras):
        palabra_seleccionada = random.choice(lista_de_palabras)

        while '_' in palabra_seleccionada or ' ' in palabra_seleccionada:
            palabra_seleccionada = random.choice(lista_de_palabras)

        return palabra_seleccionada.upper()