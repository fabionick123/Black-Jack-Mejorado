
from random import shuffle
from BlackJack import *
from BlackJack.Carta import *

figuras = ["A", 2, 3, 4, 5, 6 ,7, "Sota", "Caballo", "Rey"]
valores = [11, 2, 3, 4, 5, 6, 7, 10, 10, 10]
palo = ["Espadas", "Copas", "Oros", "Bastos"]

def CreaBaraja(baraja):
    for i in range(4):
        for j in range(len(figuras)):
            baraja.append(generarValores(valores[j], palo[i], figuras[j]))
baraja = []
CreaBaraja(baraja)
def pintarMano(baraja: list[generarValores]):
    for carta in baraja:
        print(f"{carta.figura} de {carta.palo} con valor de ({carta.valor})")
shuffle(baraja)
cartasDeJugador = []
cartasDeLaCasa = []

def sumarValores(mano):
    sum = 0
    for carta in mano:
        sum += carta.valor
    return sum
def repartirCarta(baraja, mano):
    mano.append(baraja.pop())
    ases_cambiados = True
    while sumarValores(mano) > 21 and ases_cambiados:
        ases_cambiados = False
        for carta in mano:
            if carta.valor == 11:
                carta.valor = 1
                ases_cambiados = True
def mostrarManosPrimeraRonda(cartasDeJugador: list[generarValores], cartasDeLaCasa: list[generarValores]):
    global carta
    valorDeJugador = 0
    print("*** TUS CARTAS SON ***")
    for carta in cartasDeJugador:
        valorDeJugador+=carta.valor
        print(f"{carta.figura} de {carta.palo}")
    print(f"Valor total: {valorDeJugador}")
    print("-----------------------")
    print("*** CARTAS DE LA CASA ***")
    for i in range(len(cartasDeLaCasa)):
        if i == 0:
            print(f"{cartasDeLaCasa[i].figura} de {cartasDeLaCasa[i].palo}")
        else:
            print("???")

def mostrarManosDemasRondas(cartasDeJugador: list[generarValores], cartasDeLaCasa: list[generarValores]):
    valorDeJugador = 0
    valorDeCasa = 0
    print("*** TUS CARTAS SON ***")
    for carta in cartasDeJugador:
        valorDeJugador+=carta.valor
        print(f"{carta.figura} de {carta.palo}")
    print(f"Valor total: {valorDeJugador}")
    print("-----------------------")
    print("*** CARTAS DE LA CASA ***")
    for carta in cartasDeLaCasa:
        valorDeCasa+=carta.valor
        print(f"{carta.figura} de {carta.palo}")
    print(f"Valor total: {valorDeCasa}")
    print("-----------------------")
def Hit():
    repartirCarta(baraja,cartasDeJugador)
    mostrarManosPrimeraRonda(cartasDeJugador,cartasDeLaCasa)

def Stand():
    if sumarValores(cartasDeLaCasa) < 16:
        repartirCarta(baraja,cartasDeLaCasa)
    mostrarManosDemasRondas(cartasDeJugador,cartasDeLaCasa)
def compararValores():
    if sumarValores(cartasDeJugador) > 21 and sumarValores(cartasDeLaCasa) > 21:
        print(f"¡Has perdido!, Gana la casa, perdiste!")
    if sumarValores(cartasDeJugador) > 21:
        print(f"¡Te has pasado!\nGana la casa")
    elif sumarValores(cartasDeLaCasa) > 21:
        print(f"¡La casa se ha pasado!\nHas ganado ")
    if sumarValores(cartasDeLaCasa) < sumarValores(cartasDeJugador) <= 21:
        print(f"Has ganado")
    if sumarValores(cartasDeJugador) < sumarValores(cartasDeLaCasa) <= 21:
        print(f"Ha ganado la casa")
    if sumarValores(cartasDeJugador) == sumarValores(cartasDeLaCasa):
        print(f"Ha ganado la casa. Han empatado en puntos")
repartirCarta(baraja, cartasDeJugador)
repartirCarta(baraja, cartasDeJugador)
repartirCarta(baraja, cartasDeLaCasa)
repartirCarta(baraja, cartasDeLaCasa)
mostrarManosPrimeraRonda(cartasDeJugador,cartasDeLaCasa)
continuar = True
stand = False
opcion = int(input("Que opcion quieres introducir?\n1)Hit\n2)Stand\n"))
while sumarValores(cartasDeJugador)<21:
    if opcion == 1:
        Hit()
        compararValores()
        if sumarValores(cartasDeJugador) < 21:
            opcion = int(input("Que opcion quieres introducir?\n1)Hit\n2)Stand\n"))
    if opcion == 2:
        stand = True
        while sumarValores(cartasDeLaCasa) < 16 or continuar:
            Stand()
            compararValores()
            continuar = False