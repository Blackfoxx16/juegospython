# Busqueda binaria es una algoritmo eficiente para encontrar un elemento en un lista ordenada de elementos.
# Funciona al dividir repetidamente a la mitad la porción d ela lista que prodría contener el elemento,
# hasta reducir las ubicaciones posibles a solo una.

import random
class Busqueda_binaria():

    __listado = []
    __valor_minimo = 0
    __valor_maximo = 0
    __rango_inferior = None
    __rango_superior = None
    __valor_buscado = 0
    __punto_medio = 0
    def __init__(self):

        #Se inicializa la lista de números
        self.__listado = list(self.__crear_lista())

        tamaño_lista_generada = len(self.__listado)

        #Valor maximo de la lista generada
        self.__valor_maximo = list(self.__listado)[tamaño_lista_generada - 1 ]

        # Se selecciona el valor a adivinar
        self.__valor_buscado = list(self.__listado)[random.randint(0, tamaño_lista_generada)]


        print("+========= Adivina el número ==========+")
        print("+======================================+")
        print("Comenzemos")

    def jugar(self):


        while not self.__busqueda__binaria():
            print("Intenta otra vez")


    def __busqueda__binaria(self):
        #30
        self.__valor_usuario = self.__valor_usuario_valido()

        indice_seleccionado = self.__listado.index(self.__valor_usuario)

        if self.__valor_usuario == self.__valor_buscado:
            print(f"Adivinaste el valor es: {self.__valor_buscado}")
            return True

        if self.__valor_usuario < self.__valor_buscado:
            self.__rango_inferior = indice_seleccionado + 1
            self.__valor_minimo = self.__listado[self.__rango_inferior]

        if self.__valor_usuario > self.__valor_buscado:
            self.__rango_superior = indice_seleccionado - 1
            self.__valor_maximo = self.__listado[self.__rango_superior]

        print(f"Valor mínimo: {self.__valor_minimo} - Valor máximo: {self.__valor_maximo}")
        #print(f"Valor buscado: {self.__valor_buscado} - Valor usuario: {self.__valor_usuario}")

        return False

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