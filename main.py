import random

# Valores de las cartas
cartas = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10, 'A':11}

# Función que muestra las reglas del juego
def mostrarReglas():
    print("============================================================================================")
    print("Bienvenido al Blackjack!")
    print("El objetivo del juego es conseguir superar la mano del crupier sin pasarse de 21.")
    print("Los ases valen 11 puntos, las letras valen 10 puntos y el resto de cartas mantiene su valor.")
    print("Si superas los 21 puntos pierdes el juego")
    print("============================================================================================")

# Funcion que calcula el valor total de una mano
def total(mano):
    total = 0
    ases = 0
    for carta in mano:
        total += cartas[carta]
        if carta == 'A':
            ases += 1
    while total > 21 and ases > 0:
        total -= 10
        ases -= 1
    return total

# Funcion para jugar al juego
def juego():
    mano_jugador = []
    mano_crupier = []
    baraja = list(cartas.keys()) * 4
    random.shuffle(baraja)
    mano_jugador.append(baraja.pop())
    mano_crupier.append(baraja.pop())
    mano_jugador.append(baraja.pop())
    mano_crupier.append(baraja.pop())
    print("Tu mano: " + ' '.join(mano_jugador) + " | TOTAL: " + str(total(mano_jugador)))
    print("La mano del crupier: " + mano_crupier[0] + " y otra carta.")
    while True:
        action = input("Quieres otra carta o te mantienes? [otra-mantenerse]: ").lower()
        if action == 'otra':
            mano_jugador.append(baraja.pop())
            print("==============================================================")
            print("Tu mano: " + ' '.join(mano_jugador) + " | TOTAL: " + str(total(mano_jugador)))
            if total(mano_jugador) > 21:
                print("Has perdido.")
                print("============")
                seguir = input("Quieres seguir jugando? (si-no): ").lower()
                print("=================================================")
                if seguir == 'si':
                    juego()
                elif seguir == 'no':
                    print("Gracias por jugar a Blackjack!")
                return

        elif action == 'mantenerse':
            print("==============================================================")
            print("La mano del crupier: " + ' '.join(mano_crupier) + " | TOTAL: " + str(total(mano_crupier)))
            while total(mano_crupier) < 17:
                mano_crupier.append(baraja.pop())
                print("La mano del crupier: " + ' '.join(mano_crupier) + " | TOTAL: " + str(total(mano_crupier)))
            if total(mano_crupier) > 21:
                print("El crupier se ha pasado, eres el ganador!")
                print("========================================")
            elif total(mano_jugador) > total(mano_crupier):
                print("Has ganado!")
                print("===========")

            elif total(mano_jugador) == total(mano_crupier):
                print("Es un empate!")
                print("=============")
            else:
                print("Has perdido.")
                print("============")
            seguir = input("Quieres seguir jugando? (si-no): ").lower()
            if seguir == 'si':
                print("=========================================")
                juego()
            elif seguir == 'no':
                print("==============================")
                print("Gracias por jugar a Blackjack!")
            return


mostrarReglas()
juego()


