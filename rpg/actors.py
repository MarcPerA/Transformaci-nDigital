import random


ARCHER = 1
WARRIOR = 2

ARCHER_ATTACK = (2, 15)
ARCHER_EVASION = 10
WARRIOR_EVASION = 5
WARRIOR_ATTACK = (5, 25)
HEALTH_RANGE = (100, 150)


class Player():
    def __init__(self, name, class_type):
        self.name = name
        self.health = random.randint(*HEALTH_RANGE)

        if class_type == ARCHER:
            self.attack = ARCHER_ATTACK   # Rango entre dos numeros
            self.evasion = ''
        else:
            self.attack = ''   # Rango entre dos numeros
            self.evasion = ''

    def has_fled(self):
        # TODO
        pass

    def is_alive(self):
        # TODO
        pass


class Enemy():
    def __init__(self, enemy_type):
        # TODO
        self.health = ''  # random.randint()
        self.attack = ''
        self.evasion = ''

    def attack(self, player):
        # TODO
        pass

    def is_alive(self):
        # TODO
        pass