from juegos.piedra_papel_tijeras import Piedra_papel_tijera
from juegos.Ahorcado import Ahorcado
from juegos.Busqueda_binaria import Busqueda_binaria as Adivina_numero

# Jugar piedra papel o tijera

ejecutando = True

juegos = ["Piedra, papel o tijera",  "Ahorcado", "Adivina el número"]
def iniciar():
    # seleccionar juego
    numero_de_juego = input("Elige tu juego: \n 1: Píedra, papel o tijera\n 2: Ahorcado \n 3: Adivina el número \n 0: Salir \n")

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
        juego = Piedra_papel_tijera()

    if numero_de_juego == 2:
        juego = Ahorcado()

    if numero_de_juego == 3:
        juego = Adivina_numero()

    juego.jugar()

while(ejecutando):
    iniciar()
