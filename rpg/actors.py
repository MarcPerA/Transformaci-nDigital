import random


ARCHER = 1
WARRIOR = 2

ARCHER_ATTACK = (2, 15)
ARCHER_EVASION = 10
WARRIOR_EVASION = 5
WARRIOR_ATTACK = (5, 25)
HEALTH_RANGE = (50, 100)

FLED = 2

MONSTER_ATTACK = (1, 5)
MONSTER_EVASION = 2


class Player():
    def __str__(self):
        return self.name

    def __init__(self, name, class_type):
        self.name = name
        self.health = random.randint(*HEALTH_RANGE)
        self.has_fled = False

        if class_type == ARCHER:
            self.damage = ARCHER_ATTACK   # Rango entre dos numeros
            self.evasion = ARCHER_EVASION
        else:
            self.damage = WARRIOR_ATTACK   # Rango entre dos numeros
            self.evasion = WARRIOR_EVASION

    def attack(self, action, enemy):
             
        if int(action) == FLED:
            self.has_fled = True
            return False
            
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

        if self.health < 0:
            self.health = 0
            print('Has muerto!!!')

        print(
            'Recibes {} puntos de daño, te queda {} puntos de vida'.format(
                damage, self.health)
        )

    def is_alive(self):
        return self.health > 0


class Enemy():
    def __str__(self):
        return self.name
    
    def __init__(self, enemy_type):
        self.name = enemy_type
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

        if self.health < 0:
            self.health = 0
            print('El enemigo ha muerto!!!')

        print(
            'El enemigo recibe {} puntos de daño, le queda {} puntos de vida'.format(
                damage, self.health)
        )

    def is_alive(self):
        
        return self.health > 0