import unittest
from Minesweeper import *


class Minesweeper(unittest.TestCase):
    def test_dimensions(self):
        # Arrange
        level = Level()


        # Act
        level.set_level_dimensions(8, 8)

        # Assert
        self.assertEqual(level.get_number_of_rows(), 8)
        self.assertEqual(level.get_number_of_rows(), 8)


if __name__ == "__main__":
    unittest.main()
