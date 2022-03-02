import sys
import pygame
from random import *


class Game:
    pass


class Level:
    def __init__(self, rows, columns):
        self.number_of_mines = 0
        self.columns = 0
        self.rows = 0
        self.table = []
        self.mines_list = []
        self.set_level_dimensions(rows, columns)
        self.set_table()
        self.set_number_of_mines()
        self.set_mines_list()
        self.set_mines_in_table()

    def set_level_dimensions(self, rows, columns):
        self.set_number_of_rows(rows)
        self.set_number_of_columns(columns)

    def set_number_of_rows(self, number_of_rows):
        self.rows = number_of_rows

    def set_number_of_columns(self, number_of_columns):
        self.columns = number_of_columns

    def get_number_of_rows(self):
        return self.rows

    def get_number_of_columns(self):
        return self.columns

    def set_number_of_mines(self):
        self.number_of_mines = int((self.get_total_positions() / 64) * 10)

    def get_number_of_mines(self):
        return self.number_of_mines

    def set_table(self):
        self.table = [[0] * self.get_number_of_rows() for i in range(self.get_number_of_columns())]

    def print_table(self):
        return self.table

    def get_table(self):
        return self.table

    def get_total_positions(self):
        return self.get_number_of_rows() * self.get_number_of_columns()

    def set_mines_list(self):
        for i in range(self.get_number_of_mines()):
            rand = randint(0, self.get_total_positions())
            if rand in self.mines_list:
                pass
            else:
                self.mines_list.append(rand)
        self.mines_list.sort()

    def set_mines_in_table(self):
        index = 0
        for i in range(self.get_number_of_columns()):
            for j in range(self.get_number_of_rows()):
                if index in self.mines_list:
                    self.table[i][j] = -5
                    # debo incrementar 1 en las 8 celdas circundantes
                    # derecha
                    if j < self.get_number_of_columns() - 1:
                        self.table[i][j + 1] += 1
                    # izquierda
                    if j > 0:
                        self.table[i][j - 1] += 1
                    # arriba
                    if i > 0:
                        # arriba
                        self.table[i - 1][j] += 1
                        # diagonal arriba izquierda
                        if j > 0:
                            self.table[i - 1][j - 1] += 1
                        # diagonal arriba derecha
                        if j < self.get_number_of_columns() - 1:
                            self.table[i - 1][j + 1] += 1
                    # abajo
                    if i < self.get_number_of_rows() - 1:
                        # abajo
                        self.table[i + 1][j] += 1
                        # abajo izquierda
                        if j > 0:
                            self.table[i + 1][j - 1] += 1
                        # abajo derecha
                        if j < self.get_number_of_columns() - 1:
                            self.table[i + 1][j + 1] += 1
                index += 1

        for i in range(self.get_number_of_columns()):
            for j in range(self.get_number_of_rows()):
                if self.table[i][j] < 0:
                    self.table[i][j] = 9

        self.print_table()

    def print_table(self):
        print("Table:")
        for i in range(self.get_number_of_rows()):
            print(self.table[i])






        pygame.init()
        black = (0, 0, 0)
        white = (255, 255, 255)
        red = (255, 0, 0)

        size = self.get_number_of_rows()*30, self.get_number_of_columns()*30
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption("BUSCAMINAS")
        clock = pygame.time.Clock()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            mouse_pos = pygame.mouse.get_pos()
            print(mouse_pos)
            x = mouse_pos[0]
            y = mouse_pos[1]
            screen.fill(white)

            for x in range(0, self.get_number_of_columns()*30, 30):
                for y in range(0, self.get_number_of_rows()*30, 30):
                    if self.table[x][y] < 0:
                        pygame.draw.rect(screen, black, (x, y, 25, 25))
                    else:
                        pygame.draw.rect(screen, red, (x, y, 25, 25)

            pygame.display.flip()
            clock.tick(60)


        # ventana
    #
    # def construir_mapa(self, mapa):
    #     ventana = pygame.display.set_mode(self.get_number_of_rows * 10, self.get_number_of_columns * 10)
    #     reloj = pygame.time.Clock()
    #
    #     muros = []
    #     x = 0
    #     y = 0
    #     for fila in mapa:
    #         for muro in fila:
    #             if muro == 9:
    #                 muros.append(pygame.Rect(x, y, 80, 80))
    #             x += 80
    #         x = 0
    #         y += 80
    #     return muros
    #
    #
    #     # bucle principal
    #     jugando = True
    #     while jugando:
    #         reloj.tick(60)
    #
    #     #Eventos
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             jugando = False
    #         if event.type == pygame.Cursor:
    # #datos
    #     muros = construir_mapa(mapa)
    #
    # def dibujar_mapa(self, superficie, muros):
    #     for muro in muros:
    #         dibujar_muro(superficie, muro)
