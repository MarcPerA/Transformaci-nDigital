import random # para generar numeros aleatorios
import time # para los print y que duren un poquito mas
# VARIABLES
movpc=random.randint(0,8)
ganador=0
player_name = input('Hola, Escribe aqui tu nombre, por favor: ')
 
tablero=[" "," "," ",
         " "," "," ",
         " "," "," " ]
 
tablero_position=["7","8","9",
         "4","5","6",
         "1","2","3" ]

print ("Debes introducir los movimientos indicando un numero del 1 al 9 de este modo")

def imprimetablero():
    print (" _"*6)
    print ("|",tablero[6],"|",tablero[7],"|",tablero[8],"|")
    print (" -"*6)
    print ("|",tablero[3],"|",tablero[4],"|",tablero[5],"|")
    print (" -"*6)
    print ("|",tablero[0],"|",tablero[1],"|",tablero[2],"|")
    print (" -"*6)

def comprobarjugada():
#Con esto vamos a intentar comprobar el ganador poniendo los casos de victoria posibles.
    # Player
    if tablero[0]=="X":
        if tablero[1]=="X" and tablero[2]=="X":
            return 1
        if tablero[3]=="X" and tablero[6]=="X":
            return 1
        if tablero[4]=="X" and tablero[8]=="X":
            return 1
    elif tablero[4]=="X":
        if tablero[3]=="X" and tablero[5]=="X":
            return 1
        if tablero[1]=="X" and tablero[7]=="X":
            return 1
        if tablero[2]=="X" and tablero[6]=="X":
            return 1
    elif tablero[8]=="X":
        if tablero[2]=="X" and tablero[5]=="X":
            return 1
        if tablero[7]=="X" and tablero[6]=="X":
            return 1
#maquina
    elif tablero[0]=="O":
        if tablero[1]=="O" and tablero[2]=="O":
            return 2
        if tablero[3]=="O" and tablero[6]=="O":
            return 2
        if tablero[4]=="O" and tablero[8]=="O":
            return 2
    elif tablero[4]=="O":
        if tablero[3]=="O" and tablero[5]=="O":
            return 2
        if tablero[1]=="O" and tablero[7]=="O":
            return 2
        if tablero[2]=="O" and tablero[6]=="O":
            return 2
    elif tablero[8]=="O":
        if tablero[2]=="O" and tablero[5]=="O":
            return 2
        if tablero[7]=="O" and tablero[6]=="O":
            return 2
    else:
    # final de la comprobacion si no ha ganado ninguno mantiene en 0 la variable ganador
        return 0
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