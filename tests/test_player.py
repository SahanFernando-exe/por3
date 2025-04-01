from src.player import Player
import unittest

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player(4, "Jeff")

    def test_id(self):
        self.assertEqual(self.player.uid, "4")

    def test_name(self):
        self.assertEqual(self.player.name, "Jeff")

    def test_change_error(self):
        with self.assertRaises(AttributeError):
            self.player.name = "Jack"

    def test_sort_players(self):
        players = [Player(name="Alice", uid='01', score=10), Player(name="Bob", uid='02', score=5), Player(name="Charlie", uid='03', score=15)]
        # note: ensure initialization code is valid for **your** implementation

        # do **not** change the following code:
        sorted_players = sorted(players)

        # players must be sorted by score as shown here:
        manually_sorted_players = [Player(name="Bob", uid='02', score=5), Player(name="Alice", uid='01', score=10), Player(name="Charlie", uid='03', score=15)]

        self.assertListEqual(sorted_players, manually_sorted_players)

    def test_players_can_be_compared_by_score(self):
        # note: ensure initialization code is valid for **your** implementation
        alice = Player(name="Alice", uid='01', score=10)
        bob = Player(name="Bob", uid='02', score=5)

        # Add the appropriate expression to the following assert test
        self.assertTrue(alice > bob)

if __name__ == '__main__':
    unittest.main()