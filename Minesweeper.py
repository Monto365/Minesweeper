import unittest


class Game:
    pass


class Level:
    def __init__(self):
        self.dimensions = Dimensions
        self.number_of_mines = 0
        self.table = [[0] * self.get_number_of_rows()] * self.get_number_of_columns()

    def set_level_dimensions(self, rows, columns):
        self.set_number_of_rows(rows)
        self.set_number_of_columns(columns)

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


    def print_table(self):
        table=''
        for i in range(7):
            for j in range(7):
                table += str(self.table[i][j])
            table += '\n'
        return table

    def get_table(self):
        return self.table

    def set_value_in_position_table(self, value, row, column, table):
        pass

    # def set_table(self,rows,columns):
    #     tabletemp=[[0]*rows]*columns

class Dimensions:
    rows = 0
    columns = 0
