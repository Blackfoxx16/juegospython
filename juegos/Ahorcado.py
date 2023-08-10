import random
import string
from juegos.AhorcadoResources.PalabrasAhorcado import palabras
from juegos.AhorcadoResources.Ahorcado_diccionario_dibujo import vidas__diccionario_visual
class Ahorcado():

    def __init__(self):
        print("=====================================")
        print("Bienvenido(a) al juego del ahorcado")
        print("=====================================")

        self.__palabra_seleccionada = self.__obtener_palabra_valida(palabras)

        self.__letras_por_adivinar = set(self.__palabra_seleccionada)
        self.__letras_adivinadas = set()
        self.__abecedario = set(string.ascii_uppercase)
        self.__vidas = 7


    def jugar(self):

        while(len(self.__letras_por_adivinar) > 0 and self.__vidas > 0):
            print(f"Total de vidas: {self.__vidas}")
            print(f"Letras utilizadas: { ' '.join(self.__letras_adivinadas)}")

            #Mostrando letras adivinadas
            lista_letras = [letra if letra in self.__letras_adivinadas else '-' for letra in self.__palabra_seleccionada]

            #Mostrar estado del ahorcado
            print(vidas__diccionario_visual[self.__vidas])

            #Mostrar la palabra seleccionada
            print(f"Palabra: {' '.join(lista_letras)}")

            #Ingresar letra por usuario
            letra_usuario = input("Escoge una letra: ").upper()


            #Si la letra ingresada por el usuario esta en el abecedario y no se encuentra en la lista de letras adivinadas,
            #se añade a la lista de letras adivinadas
            if letra_usuario in self.__abecedario - self.__letras_adivinadas:
                self.__letras_adivinadas.add(letra_usuario)

                #Si la letra esta en la palabra remover la letra del conjunto de letras por adivinar
                #de lo contrario quitar una vida.
                if letra_usuario in self.__letras_por_adivinar:
                    self.__letras_por_adivinar.remove(letra_usuario)
                    print('')
                else:
                    self.__vidas -= 1
                    print(f"La letra: {letra_usuario} no esta en la palabra\n")
            #Si la letra ya ha sido seleccionada por el usuario
            elif letra_usuario in self.__letras_adivinadas:
                print(f"La letra: {letra_usuario} ya fue seleccionada. Por favor elige una nueva letra.")
            else:
                print("Esta letra no es valida")

        #El juego llega ha esta linea cuando se adivinan todas las letras de la palabra
        #o cuando se agotan las vidas

        if self.__vidas == 0:
            print("+========= Ahorcado ==========+")
            print("+========= Has perdido ==========+")
            print(vidas__diccionario_visual[0])
            print(f"La palabra era: {self.__palabra_seleccionada}")
        else:

            print("+========= Has ganado ==========+")
            print(f"La palabra es: {self.__palabra_seleccionada}")


    #Selecciona una palabra válida del listado de palabras
    def __obtener_palabra_valida(self, lista_de_palabras):

        palabra_random = random.choice(lista_de_palabras)

        while '_' in palabra_random or ' ' in palabra_random:
            palabra_random = random.choice(lista_de_palabras)

        return palabra_random.upper()