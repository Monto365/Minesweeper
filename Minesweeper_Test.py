import unittest
from Minesweeper import *


#
# # Show full diff in unittest
# unittest.util._MAX_LENGTH = 2000


class Minesweeper(unittest.TestCase):
    def test_dimensions(self):
        # Arrange
        level = Level(8, 8)

        # Act
        rows = level.get_number_of_rows()
        columns = level.get_number_of_columns()

        # Assert
        self.assertEqual(rows, 8)
        self.assertEqual(columns, 8)

    # def test_number_of_mines(self):
    #     # Arrange
    #     level = Level(8, 8)
    #
    #     # Act
    #     number_of_mines = level.get_number_of_mines()
    #
    #     # Assert
    #     self.assertEqual(number_of_mines, 10)

    # def test_create_table(self):
    #     # Arrange
    #     level = Level(8, 8)
    #
    #     # Act
    #     table_created = level.get_table()
    #
    #     # Assert
    #
    #     table_expected = [[0] * 8] * 8
    #     print("Self mines list: ")
    #     print(level.mines_list)
    #     print(level.table[4][3])
    #     print(level.table)
    #     self.assertEqual(table_created, table_expected)

    # def test_list_of_mines(self):
    #     level = Level(8, 8)
    #     level.create_list_mines()


if __name__ == "__main__":
    unittest.main()
