import unittest
from unittest.mock import Mock
from src.GameState import *
from src.Box import *
from src.Target import *
"""
There is no tests until i find a way to avoid infinity loop
"""
class GameStateTest(unittest.TestCase):

    another = None

    def setUp(self):
        self.gs = GameState(Mock())

    def tearDown(self):
        self.gs = None

    def testIsLevelCompleted(self):
        self.gs.game_objects['boxes'] = [
            Box((300, 300)),
            Box((400, 300)),
        ]
        self.gs.game_objects['targets'] = [
            Target((320, 320)),
            Target((420, 320)),
        ]
        assert Box((300, 300)).colliderect(Target((300, 300)).get_rect()) == True
        assert Box((400, 300)).colliderect(Target((420, 320)).get_rect()) == True
        assert self.gs.is_level_completed() == True
        self.gs.game_objects['targets'] = [
            Target((20, 320)),
            Target((320, 320)),
        ]
        assert self.gs.is_level_completed() == False


if __name__ == "__main__":
    unittest.main()
