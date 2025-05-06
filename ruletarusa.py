#Intento de codigo para crear un juego de ruleta rusa
import random
jugadores = int(input("ingrese el numero de jugadores: "))
while jugadores < 2 or jugadores > 6:
    if jugadores <= 1:
        print("el numero de jugadores no puede ser menor a 2")
        jugadores = int(input("ingrese el numero de jugadores: "))
    elif jugadores > 6:
        print("el numero de jugadores no puede ser mayor a 6")
        jugadores = int(input("ingrese el numero de jugadores: "))
    else:
        print("el numero de jugadores es correcto, podemos iniciar el juego")
        break
nombres_jugadores = {}
for i in range(1, jugadores + 1):
    nombre = input(f"Ingrese el nombre del jugador {i}: ")
    nombres_jugadores[f"jugador_{i}"] = nombre
    print(f"El jugador {nombre} ha sido registrado")
print("DESCRIPCION DEL JUEGO")
print("Todos los jugadores han sido registrados, podemos iniciar el juego \n")
print("Lista de jugadores:", nombres_jugadores)
print("DESCRIPCION DEL JUEGO\n")
print("El juego consiste en un revolver con 6 espacios, de los cuales 1 tiene una bala")
print("En cada turno, cada jugador tendra la oportunidad de disparar a un jugador diferente o a si mismo")
print("Si el jugador dispara a un jugador diferente, y no sale la bala, el jugador que disparó debe disparar nuevamente, pero esta vez a si mismo")
print("Si el jugador se dispara a si mismo y no sale la bala, se pasa el turno al siguiente jugador")
print("Cuando el jugador dispara y la bala sale, a quien le haya llegado el disparo, queda eliminado del juego")
print("despues de disparar, se recargara el revolver otra vez con 1 bala y 5 espacios vacios")
print("El juego termina cuando solo queda un jugador en pie")