from game.exeptions import *
from game.cli import Cliente

def main():

    cliente = Cliente()
    iniciar = cliente.inicializar_chess()

    while True:
        cliente.comenzar_iteracion(iniciar[0], iniciar[1])
        try:
            
            input = cliente.funcion_entrada()

            if input == False:
                break
            
            movimiento = iniciar[0].move(input[0], input[1], input[2], input[3])

            if movimiento == "ReyEliminado":
                print("El rey ha sido eliminado. La partida ha terminado.")
                print("El ganador es: " + iniciar[0].get_ganador())
                break

            cliente.limpiar_consola()

            if movimiento == "Valido":
                continue

            cliente.detectar_excepcion(movimiento)

        except ValueError as e:
            print("El valor introducido no es un entero. Intentelo de nuevo.")
        except (CasillaOcupada, PiezaNoExiste,IndexErrorPersonalizada, MismaCasilla, ColorIncorrecto, InvalidMove) as e:
            print(e)


if __name__ == '__main__':
    main()