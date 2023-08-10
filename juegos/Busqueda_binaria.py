# Busqueda binaria es una algoritmo eficiente para encontrar un elemento en un lista ordenada de elementos.
# Funciona al dividir repetidamente a la mitad la porción d ela lista que prodría contener el elemento,
# hasta reducir las ubicaciones posibles a solo una.

import random
class Busqueda_binaria():

    __listado = set()
    __valor_minimo = 0
    __valor_maximo = 0
    __rango_inferior = None
    __rango_superior = None
    __valor_buscado = 0
    __punto_medio = 0
    def __init__(self):

        #Se inicializa la lista de números
        self.__listado = self.__crear_lista()

        tamaño_lista_generada = len(self.__listado)

        #Valor maximo de la lista generada
        self.__valor_maximo = list(self.__listado)[tamaño_lista_generada]

        # Se selecciona el valor a adivinar
        self.__valor_buscado = list(self.__listado)[random.randint(0, tamaño_lista_generada)]

        print(self.__valor_buscado)
        print("+========= Adivina el número ==========+")
        print("+======================================+")
        print("Comenzemos")

    def jugar(self):

        self.__valor_usuario = self.__valor_usuario_valido()

        self.__busqueda__binaria()


    def __busqueda__binaria(self):
        #30
        self.__punto_medio = (self.__rango_inferior + self.__rango_superior) // 2

        valor_punto_medio = list(self.__listado)[self.__punto_medio]

        if self.__valor_usuario == self.__valor_buscado:
            print(f"Adivinaste el valor es: {self.__valor_buscado}")
            return 1

        if self.__valor_buscado < self.__valor_usuario:






    def __crear_lista(self):
        lista_generada = set()
        for i in range(100):
            lista_generada.add(i)
        return lista_generada

    def __valor_usuario_valido(self):
        valor = input("Ingresa un número: ")

        try:
            return int(valor)
        except:
            print("El valor ingresado es incorrecto, intenta de nuevo.")
            return self.__valor_usuario_valido()