import unittest

from actors import Player, Enemy, ARCHER
from app import ENCOUNTERS, ENCOUNTERS_WITH_ENEMIES, ENEMY_TYPES, has_enemy_in_encounter

class GameTestCase(unittest.TestCase):
    def test_player_get_damage_alive(self):
        player = Player('Robin Hood', ARCHER)
        player.health = 20

        player.get_damage(15)

        self.assertTrue(player.is_alive())

    def test_player_get_damage_dead(self):
        player = Player('Robin Hood', ARCHER)
        player.health = 14

        player.get_damage(15)

        self.assertFalse(player.is_alive())

    # TODO Player y enemy


    # TODO is_attack_avoided
    def test_is_attack_avoided(self):
         player = Player('Robin Hood', ARCHER)
         player.health = 13

         player.get_damage(15)
         player.is_attack_avoided = 100

        
    # TODO Test has_enemy_in_encounter
    def test_has_enemy_in_encounter(self):
        ENCOUNTERS = Enemy('enemy_orco')
        ENCOUNTERS_WITH_ENEMIES = ENCOUNTERS
        ENEMY_TYPES = 'enemy_orco'
        

    # TODO Test decide_encounter


    # TODO I battle active, cuando el enemigo esta vivo o muerto, o cuando el jugador esta vivo o esta muerto

if __name__ == '__main__':
    unittest.main()