import unittest


class Game:
    pass


class Level:
    def __init__(self):
        self.dimensions = Dimensions
        self.table = 0

    def set_level_dimensions(self, rows, columns):
        self.dimensions.rows = rows
        self.dimensions.columns = columns

    # def set_level_dimensions(self, dimensions):
    #     self.dimensions.set_number_of_columns(dimensions.columns)
    #     self.dimensions.set_number_of_rows(dimensions.rows)

    def set_number_of_rows(self, number_of_rows):
        self.dimensions.rows = number_of_rows

    def set_number_of_columns(self, number_of_columns):
        self.dimensions.columns = number_of_columns

    def get_number_of_rows(self):
        return self.dimensions.rows

    def get_number_of_columns(self):
        return self.dimensions.columns


class Dimensions:
    def __init__(self):
        self.rows = 0
        self.columns = 0


