import random
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
    return enemy.is_alive() or not player.has_fled() or not player.is_alive()


def main():
    print('======== RPG ===========')

    player_name = input('Elige el nombre de tu personaje: ')
    player_class = input('Elige entre Arquero(1) y Guerrero(2): ')
    player = Player(player_name, player_class)
    # TODO Contador de salas a las que has podido llegar

    while True:
        navigation_action = choose_action()
        encounter = decide_encounter(navigation_action)

        if has_enemy_in_encounter(encounter):
            enemy = create_enemy(encounter)

            # Battle mode
            while is_battle_active(player, enemy):
                # TODO Que hacer aqui para que haya turnos
                player.attack(enemy)
                enemy.attack(player)

        if not player.is_alive():
            print('GAME OVERRRRRRR!!')
            break

        # TODO Aumentar contador de salas


if __name__ == '__main__':
    main()