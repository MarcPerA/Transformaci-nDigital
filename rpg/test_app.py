import unittest

from actors import Player, Enemy, ARCHER

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
    # TODO Test has_enemy_in_encounter
    # TODO Test decide_encounter
    # TODO I battle active, cuando el enemigo esta vivo o muerto, o cuando el jugador esta vivo o esta muerto

if __name__ == '__main__':
    unittest.main()