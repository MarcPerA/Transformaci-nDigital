import random # para generar numeros aleatorios
import time # para los print y que duren un poquito mas
# VARIABLES
movpc=random.randint(0,8)
ganador=0
player_name = input('Hola, Escribe aqui tu nombre, por favor: ')

MAXIMUM_COLUMNS = 4
tablero = [range(1, MAXIMUM_COLUMNS) for index in range(3)]

print ("Debes introducir los movimientos indicando un numero del 1 al 9 de este modo")

def imprimetablero():
    print(' _' * 6)
    for row in tablero:
        print('|'.join(row))
    print(' _' * 6)

def comprobarjugada():
    # Fila
    for row in tablero:
        first_element = row[0]
        if all(first_element == item for item in row[1:]):
            return True

    # TODO Columna
    for index, row in enumerate(tablero):
        for indexj, column in enumerate(row):
            first_element = row[index][indexj]

    # TODO Diagonal

    # Por defecto
    return False

def resultado(ganador):
    if ganador==1:
        print ("Ganaste !!")
    elif ganador==2:
        print ("Eres un perdedor!!")
    else:
        print ("Empate !!, continua intentandolo")
#Imprimimos los pasos a seguir

print ("-----------------")
print ("|",tablero_position[0],"|",tablero_position[1],"|",tablero_position[2],"|")
print (" -"*6)
print ("|",tablero_position[3],"|",tablero_position[4],"|",tablero_position[5],"|")
print (" -"*6)
print ("|",tablero_position[6],"|",tablero_position[7],"|",tablero_position[8],"|")
print ("-----------------")

# bucle; movimientos 5 humano (empieza) 4 maquina
for turno in range(1,6):

    # movimiento del humano y comprobacion
    movhuman=int(input("{}, por favor inserta movimiento (1-9) ".format(player_name)))
    movhuman-=1
    while movhuman>8 or movhuman<0 or tablero[movhuman]=="X" or tablero[movhuman]=="O":
        movhuman=int(input("Inserta movimiento valido (1-9) "))
        movhuman-=1
    tablero[movhuman]="X"
 # impresion del turno humano

    print ("Movimiento de {}".format(player_name))
    imprimetablero()

    # comprueba si alguno de los 2 ha ganado ganado
    ganador=comprobarjugada()


    # pc 4 turnos el ultimo no lo juega por falta de espacio en el tablero
    if turno < 5:
        #movimiento maquina genero el numero aleatorio con la resta aplicada, el while evita que la compu ponga ficha encima de las existentes
        movpc=random.randint(0,8)
        while tablero[movpc]=="X" or tablero[movpc]=="O":
            movpc=random.randint(0,8)
        tablero[movpc]="O"

        # Turno de la máquina

        print ("Es el turno de la Maquina:")
        print(" --------------------------")
        time.sleep(2)
        imprimetablero()

        # comprueba si alguno de los 2 ha ganado
        ganador=comprobarjugada()

resultado(ganador)