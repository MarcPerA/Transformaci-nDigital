import random,os,time
from actors import Player, Enemy


ENCOUNTERS = dict(
    enemy_orco='Te has encontrado a un orco',
    enemy_goblin='Te has encontrado a un goblin',
    empty_room='sala vacia')
ENCOUNTERS_WITH_ENEMIES = ('enemy_orco', 'enemy_goblin')
ENEMY_TYPES = dict(
    enemy_orco='orco',
    enemy_goblin='goblin'
)


def choose_action():
    return input('Elige entre ir (a)delante, a(t)ras, dere(c)ha, (i)zquierda: ')


def decide_encounter(navigation_action):
    return random.choice(list(ENCOUNTERS.keys()))


def has_enemy_in_encounter(encounter):
    return encounter in ENCOUNTERS_WITH_ENEMIES


def create_enemy(encounter):
    return Enemy(ENEMY_TYPES[encounter])


def is_battle_active(player, enemy):
    return enemy.is_alive() and player.is_alive() and not player.has_fled
    
    


def main():
    print('======== RPG ===========')

    player_name = input('Elige el nombre de tu personaje: ')
    player_class = input('Elige entre Arquero(1) y Guerrero(2): ')
    player = Player(player_name, player_class)
    room_count = 1
    enemy_count = 0
   

    while True:
        player.has_fled = False
        navigation_action = choose_action()
        encounter = decide_encounter(navigation_action)

        if has_enemy_in_encounter(encounter):
            enemy = create_enemy(encounter)
            print('Un {} salvaje aparecio'.format(enemy))

            

            
            while is_battle_active(player, enemy):
               
                print("\nTURNO DE",player_name)
                action = input('Elige accion: (1) Atacar, (2) Huir: ')
                print('Procesando acción...')
                time.sleep(1)
                player.attack(action, enemy)
                enemy.attack(player)
            enemy_count += 1
            print('derrotaste a {} enemigos'.format(enemy_count))
        room_count += 1
        print('Has pasado por la habitación nº', room_count)
        if not player.is_alive():
            print('Tu puntuación es de {} salas'.format(room_count))
            print('GAME OVERRRRRRR!!')
            break

        


if __name__ == '__main__':
    main()