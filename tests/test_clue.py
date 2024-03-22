import unittest
from launch_game import *
from classes.player import *

class TestGameFunctions(unittest.TestCase):

    def setUp(self):
        self.places = ["PlaceA", "PlaceB", "PlaceC","PlaceD" ]
        self.weapons = ["WeaponA", "WeaponB", "WeaponC"]
        self.players = [
            player(1, ["PlaceA", "PlaceB"], ["WeaponA", "WeaponB"]),
            player(2, ["PlaceB", "PlaceC"], ["WeaponB", "WeaponC"]),
            player(3, ["PlaceC", "PlaceA"], ["WeaponC", "WeaponA"]),
            player(4, ["PlaceC", "PlaceD"], ["WeaponC", "WeaponA"])
        ]

    def test_choose_common_visited_place(self):
        victim = self.players[1]
        murderer = self.players[0]
        result = choose_common_visited_place(victim,murderer)
        #the common visited place is PlaceB
        self.assertEqual(result,"PlaceB")
        result = choose_common_visited_place(self.players[3],murderer)
        #there are no common visited place
        self.assertEqual(result,None)

    def test_murder(self):
        murderer = self.players[0]
        victim,place,weapon = murder(murderer,self.players)
        # the victim is an alive player
        self.assertIn(victim,self.players)
        # check if the murder place visited by the murderer and the victim
        self.assertIn(place,murderer.visited_places)
        self.assertIn(place,victim.visited_places)
        # the murder weapon is one of the ,murderer favorite weapons
        self.assertIn(weapon,murderer.fav_weapons)
    
    def test_pick_murderer(self):
        result = pick_murderer(self.players)
        self.assertIn(result,self.players)
        self.assertIsInstance(result,player)
        self.assertTrue(result.is_murderer)
    
    def test_empty_player_list(self):
        with self.assertRaises(ValueError):
            pick_murderer([])

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            pick_murderer("not_a_list")

    def test_invalid_player_objects(self):
        with self.assertRaises(ValueError):
            pick_murderer(["not_a_player"])
    
    def test_get_player_by_name(self):
        result = get_player_by_name(self.players , 1)
        self.assertEqual(result, self.players[0])
        result = get_player_by_name(self.players , 5)
        self.assertEqual(result, None)
    


if __name__ == '__main__':
    unittest.main()