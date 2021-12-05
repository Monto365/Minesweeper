import unittest
import Minesweeper

class Minesweeper(unittest.TestCase):
    def test_dimensions(self):
        #Arrange
        level=Level()

        #Act
        set_level_dimensions(8, 8)

        #Assertk