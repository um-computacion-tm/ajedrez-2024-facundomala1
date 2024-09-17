from exeptions import CasillaOcupada, PiezaNoExiste, MismaCasilla, ColorIncorrecto, MovimientoInvalido, IndexErrorPersonalizada
from cli import Cliente

def main():

    cliente = Cliente()
    iniciar = cliente.inicializar_juego()

    while True:

        cliente.comenzar_iteracion(iniciar[0], iniciar[1])

        try:
            
            input = cliente.input_function()

            if input == False:
                break
            
            movement = iniciar[0].move(input[0], input[1], input[2], input[3])

            # Si el rey ha sido eliminado, terminamos la partida
            if movement == "ReyEliminado":
                print("El rey ha sido eliminado. La partida ha terminado.")
                print("El ganador es: " + iniciar[0].get_ganador())
                break

            # Limpiar consola por cada iteracion
            cliente.clear_console()

            # Si el movimiento es valido, nos ahorramos las Excepciones
            if movement == "Valido":
                continue

            cliente.detectar_exepcion(movement)

        #Aca atrapamos TODOS los errores
        except ValueError as e:
            print("El valor introducido no es un entero. Intentelo de nuevo.")
        except (IndexErrorPersonalizada, CasillaOcupada, PiezaNoExiste, MismaCasilla, ColorIncorrecto, MovimientoInvalido) as e:
            print(e)


if __name__ == '__main__':
    main()