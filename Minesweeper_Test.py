import unittest
from Minesweeper import *


class Minesweeper(unittest.TestCase):
    def test_dimensions(self):
        # Arrange
        level = Level()

        # Act
        level.set_level_dimensions(8, 8)
        rows = level.get_number_of_rows()
        columns = level.get_number_of_columns()

        # Assert
        self.assertEqual(rows, 8)
        self.assertEqual(columns, 8)

    def test_number_of_mines(self):
        # Arrange
        level = Level()

        # Act
        level.set_level_dimensions(8, 8)
        number_of_mines = level.get_number_of_mines()

        # Assert
        self.assertEqual(number_of_mines, 10)


if __name__ == "__main__":
    unittest.main()
