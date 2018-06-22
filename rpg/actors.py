import random


ARCHER = 1
WARRIOR = 2

ARCHER_ATTACK = (2, 15)
ARCHER_EVASION = 10
WARRIOR_EVASION = 5
WARRIOR_ATTACK = (5, 25)
HEALTH_RANGE = (100, 150)

MONSTER_ATTACK = (1, 5)
MONSTER_EVASION = 2


class Player():
    def __init__(self, name, class_type):
        self.name = name
        self.health = random.randint(*HEALTH_RANGE)

        if class_type == ARCHER:
            self.damage = ARCHER_ATTACK   # Rango entre dos numeros
            self.evasion = ARCHER_EVASION
        else:
            self.damage = WARRIOR_ATTACK   # Rango entre dos numeros
            self.evasion = WARRIOR_EVASION

    def attack(self, enemy):
        if self.is_attack_avoided(enemy):
            print('Ataque evitado')
            return False

        damage = random.randint(*self.damage)
        enemy.get_damage(damage)
        return enemy

    def is_attack_avoided(self, enemy):
        attack_chance = random.randint(0, 100) - enemy.evasion
        return attack_chance < 0

    def get_damage(self, damage):
        self.health -= damage
        print(
            'Recibes {} puntos de daño, te queda {} puntos de vida'.format(
                self.health, damage)
        )
        if self.health < 0:
            self.health = 0
            print('Has muerto!!!')

    def has_fled(self):
        # TODO To be implemented
        return False

    def is_alive(self):
        return self.health > 0


class Enemy():
    def __init__(self, enemy_type):
        self.health = random.randint(*HEALTH_RANGE)
        self.damage = MONSTER_ATTACK
        self.evasion = MONSTER_EVASION

    def attack(self, player):
        if self.is_attack_avoided(player):
            print('Ataque evitado')
            return False

        damage = random.randint(*self.damage)
        player.get_damage(damage)
        return player

    def is_attack_avoided(self, player):
        attack_chance = random.randint(0, 100) - player.evasion
        return attack_chance < 0

    def get_damage(self, damage):
        self.health -= damage
        print(
            'El enemigo recibe {} puntos de daño, le queda {} puntos de vida'.format(
                self.health, damage)
        )
        if self.health < 0:
            self.health = 0
            print('El enemigo ha muerto!!!')

    def is_alive(self):
        return self.health > 0