import random
from actors import Player, Enemy


NAVIGATION_ACTIONS = dict(
    enemy_orco='Te has encontrado a un orco',
    enemy_goblin='Te has encontrado a un goblin',
    empty_room='sala vacia')


def choose_direction():
    # TODO
    pass


def decide_encounter(navigation_action):
    # TODO Te has encontrado un orco o
    # no hay nada en esta sala
    # random con una lista de acciones
    return random.choice(NAVIGATION_ACTIONS)


def has_enemy_in_encounter(encounter):
    # TODO
    pass


def create_enemy(encounter):
    # TODO enemy = Enemy(encounter)
    pass


def main():
    print('RPG')

    player_name = input('Elige el nombre de tu personaje: ')
    player_class = input('Elige entre Arquero(1) y Guerrero(2)')
    player = Player(player_name, player_class)
    # TODO Contador de salas a las que has podido llegar

    while True:
        # TODO Navegar y realizar una acción de navegación
        # ir a la derecha, izquierda, adelante, atras
        # Cada vez que hay una accion de navegacion
        # puede salir un bicho, o una frase aleatoria
        navigation_action = choose_direction()
        encounter = decide_encounter(navigation_action)

        if has_enemy_in_encounter(encounter):
            enemy = create_enemy(encounter)

            # Battle mode
            while enemy.is_alive() or not player.has_fled() or not player.is_alive():
                player.attack(enemy)
                enemy.attack(player)

        if  not player.is_alive():
            print('GAME OVERRRRRRR!!')
            break

        # TODO Aumentar contador de salas


if __name__ == '__main__':
    main()