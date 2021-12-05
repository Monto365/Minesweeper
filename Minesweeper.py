import unittest


class Game:
    pass


class Level:
    def __init__(self):
        self.dimensions = Dimensions
        self.number_of_mines = 0

    def set_level_dimensions(self, rows, columns):
        self.dimensions.rows = rows
        self.dimensions.columns = columns

    def set_number_of_rows(self, number_of_rows):
        self.dimensions.rows = number_of_rows

    def set_number_of_columns(self, number_of_columns):
        self.dimensions.columns = number_of_columns

    def get_number_of_rows(self):
        return self.dimensions.rows

    def get_number_of_columns(self):
        return self.dimensions.columns

    def calculate_number_of_mines(self):
        total_places = self.get_number_of_rows() * self.get_number_of_columns()
        self.number_of_mines = (total_places / 64) * 10

    def get_number_of_mines(self):
        self.calculate_number_of_mines()
        return self.number_of_mines


class Dimensions:
    def __init__(self):
        self.rows = 0
        self.columns = 0
