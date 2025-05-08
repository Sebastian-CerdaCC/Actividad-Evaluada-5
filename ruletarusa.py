#Intento de codigo para crear un juego de ruleta rusa

import random
jugadores = int(input("ingrese el numero de jugadores: "))
while jugadores < 2 or jugadores > 6:
    if jugadores <= 1 or jugadores > 6:
        print("el numero de jugadores no puede ser menor a 2 o mayor a 6")
        jugadores = int(input("ingrese el numero de jugadores: "))
    else:
        print("el numero de jugadores es correcto, podemos iniciar el juego")
        break
nombres_jugadores = {}
for i in range(1, jugadores + 1):
    nombre = input(f"Ingrese el nombre del jugador {i}: ")
    nombres_jugadores[f"jugador_{i}"] = nombre
    print(f"El jugador {nombre} ha sido registrado")
print("Todos los jugadores han sido registrados, podemos iniciar el juego \n")
print("Lista de jugadores:", nombres_jugadores)
print("DESCRIPCION DEL JUEGO\n")
print("El juego consiste en un revolver con 6 espacios, de los cuales 1 tiene una bala")
print("En cada turno, cada jugador tendra la oportunidad de disparar a un jugador diferente o a si mismo")
print("Si el jugador dispara a un jugador diferente, y no sale la bala, el jugador que disparó debe disparar nuevamente, pero esta vez a si mismo")
print("Si el jugador se dispara a si mismo y no sale la bala, se pasa el turno al siguiente jugador")
print("Cuando el jugador dispara y la bala sale, a quien le haya llegado el disparo, queda eliminado del juego")
print("despues de disparar, se recargara el revolver otra vez con 1 bala y 5 espacios vacios")
print("El juego termina cuando solo queda un jugador en pie\n")



#funcion para crear el revolver
def recargar ():
    revolver = [0] * 6 
    bala = random.randint(0, 5)  
    revolver[bala] = 1  
    return revolver



#funcion para disparar
def disparar(revolver, jugador):
    posicion = random.randint(0, 5)
    if revolver[posicion] == 1:  
        print(f"¡Bang! {jugador} ha sido eliminado.")
        return True  
    else:
        print(f"{jugador} ha disparado y no ha pasado nada.")
        return False  
    

#funcion para jugar


def jugar():
    revolver = recargar()
    jugadores_vivos = list(nombres_jugadores.values())
    turno = 0
    while len(jugadores_vivos) > 1:
        jugador = jugadores_vivos[turno]
        print(f"Turno de {jugador}")
        
        print("¿A quién quieres disparar?")
        for i, j in enumerate(jugadores_vivos):
            print(f"{i + 1}. {j}")
        print(f"{len(jugadores_vivos) + 1}. A ti mismo")
        
        while True:
            try:
                eleccion = int(input("Elige una opción: "))
                if 1 <= eleccion <= len(jugadores_vivos) + 1:
                    break
                else:
                    print("Opción inválida. Intenta de nuevo.")
            except ValueError:
                print("Entrada inválida. Por favor, ingresa un número.")
        
        if eleccion == len(jugadores_vivos) + 1:
            objetivo = jugador
        else:
            objetivo = jugadores_vivos[eleccion - 1]
        
        print(f"{jugador} ha decidido disparar a {objetivo}.")
        
        while True:
            accion = input('Escribe "disparar" para ejecutar el disparo: ').lower()
            if accion == "disparar":
                break
            else:
                print('Entrada inválida. Debes escribir "disparar".')
        
        disparo_exitoso = disparar(revolver, objetivo)

        if disparo_exitoso:
            jugadores_vivos.remove(objetivo)
            print(f"{objetivo} ha sido eliminado.")
            revolver = recargar()
            print("El revolver ha sido recargado.\n")
            if turno >= len(jugadores_vivos):
                turno = 0
        else:
            print(f"{objetivo} sigue en el juego.")
            if objetivo != jugador:

                print(f"{jugador} ahora debe dispararse a sí mismo.")

                while True:
                    accion = input('Escribe "disparar" para ejecutar el disparo: ').lower()
                    if accion == "disparar":
                        break
                    else:
                        print('Entrada inválida. Debes escribir "disparar".')
                
                disparo_exitoso = disparar(revolver, jugador)
                if disparo_exitoso:
                    jugadores_vivos.remove(jugador)
                    print(f"{jugador} ha sido eliminado.")
                    revolver = recargar()
                    print("El revolver ha sido recargado.\n")
                else:
                    print(f"{jugador} sigue en el juego.")
                    turno = (turno + 1) % len(jugadores_vivos)
            else:
                turno = (turno + 1) % len(jugadores_vivos)

    print(f"¡Felicidades! {jugadores_vivos[0]} ha ganado el juego.")


iniciar = input("¿Quieres iniciar el juego? (si/no): ").lower()
if iniciar == "si":
    jugar()