from src.quadrant import Quadrant
from src.line import Line
import helpers


class Board(object):

    def __init__(self, board):
        self.board = board

    def print(self):
        print(self.board)

    def get_quadrants(self):
        quadrants = []
        for quadrant in self.board:
            quadrants.append(Quadrant(quadrant))

        return quadrants

    def solve(self):
        for quadrant_index, quadrant in enumerate(self.get_quadrants(), start=1):
            missing_numbers = quadrant.get_missing_numbers()

            for cell_index, cell in enumerate(quadrant.get_cells(), start=1):

                horizontal_cells = []
                for i in helpers.get_horizontal_indexes(quadrant_index):
                    for j in helpers.get_horizontal_indexes(cell_index):
                        horizontal_cells.append(self.board[i - 1][j - 1])

                vertical_cells = []
                for i in helpers.get_vertical_indexes(quadrant_index):
                    for j in helpers.get_vertical_indexes(cell_index):
                        vertical_cells.append(self.board[i - 1][j - 1])

                horizontal_line = Line(horizontal_cells)
                vertical_line = Line(vertical_cells)
