import unittest
from app.player import Player

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player("John")
        
    def test_add_score(self):
        self.player.add_score(10)
        self.assertEqual(self.player.score, 10)
        
        self.player.add_score(20)
        self.assertEqual(self.player.score, 30)
        
    def test_reset_score(self):
        self.player.add_score(10)
        self.player.reset_score()
        self.assertEqual(self.player.score, 0)
        
    def test_set_name(self):
        self.player.set_name("Jack")
        self.assertEqual(self.player.name, "Jack")
        
    def test_str(self):
        self.assertEqual(str(self.player), "John")
        
if __name__ == '__main__':
    unittest.main()
