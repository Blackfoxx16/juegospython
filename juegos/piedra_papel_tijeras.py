
import random
class Piedra_papel_tijera():

    def __init__(self):
        self.__opciones = ["piedra", "papel", "tijera"]
        print("=====================================")
        print("Bienvenido(a) al juego piedra papel tijera")
        print("=====================================")

    def jugar(self):
        opcion_usuario = input("Elige una opción: \n 0 : piedra \n 1: papel \n 2 : tijeras \n").lower()
        opcion_computadora = random.choice(self.__opciones)

        opcion_seleccionada = self.__opciones[int(opcion_usuario)]

        if opcion_seleccionada == opcion_computadora:
            print('Empate!')
        elif self.__jugador_gana(opcion_seleccionada, opcion_computadora):
            print('Ganaste!')
        else:
            print('Perdiste!')

    def __jugador_gana(self, usuario, computadora):
        # piedra gana a tijera
        if usuario == self.__opciones[0] and computadora == self.__opciones[2]:
            return True

        # tijera gana a papel
        if usuario == self.__opciones[2] and computadora == self.__opciones[1]:
            return True

        # papel gana a piedra
        if usuario == self.__opciones[1] and computadora == self.__opciones[0]:
            return True

        return False