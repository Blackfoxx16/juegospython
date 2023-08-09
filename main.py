from juegos.piedra_papel_tijeras import Piedra_papel_tijera
from juegos.Ahorcado import Ahorcado

# Jugar piedra papel o tijera

ejecutando = True

juegos = ["Piedra, papel o tijera",  "Ahorcado"]
def jugar():
    # seleccionar juego
    numero_de_juego = input("Elige tu juego: \n 1: Píedra, papel o tijera\n 2: Ahorcado \n 0: Salir \n")

    try:
        numero_de_juego = int(numero_de_juego)
    except:
        print("El valor seleccionado es incorrecto")
        numero_de_juego = 0

    if numero_de_juego == 0:
        global ejecutando
        ejecutando= False
        return

    if numero_de_juego == 1:
        juego = Piedra_papel_tijera().jugar()

    if numero_de_juego == 2:
        juego = Ahorcado().jugar()


while(ejecutando):
    jugar()
