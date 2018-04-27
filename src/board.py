from src.cell import Cell
from src.region import Region

class Board(object):

    quadrants = []
    horizontal_lines = []
    vertical_lines = []

    def __init__(self, board):
        self.board = board
        self.build()

    # TODO: Improve this very primitive board display
    def print(self):
        position = 0
        line_string = ""
        for cell in self.board:
            if cell.y_pos > position:
                line_string += "\n"
                position = cell.y_pos

            if not cell.value:
                line_string += "_ "
                continue

            line_string += str(cell.value) + " "

        print(line_string)

    def build(self):
        tmp_board = []
        for line_index, line_values in enumerate(self.board, start=1):
            for cell_index, cell_value in enumerate(line_values, start=1):
                tmp_board.append(Cell(cell_index, line_index, cell_value))

        self.board = tmp_board

    def get_horizontal_line(self, y_pos):
        cells = []
        for cell in self.board:
            if cell.y_pos == y_pos:
                cells.append(cell)

        return Region(cells)

    def get_vertical_line(self, x_pos):
        cells = []
        for cell in self.board:
            if cell.x_pos == x_pos:
                cells.append(cell)

        return Region(cells)

    def get_quadrant(self, x_pos, y_pos):
        cells = []

        # TODO: Add quadrant functionality.

        return Region(cells)

    def solve(self):
        for cell in self.board:
            horizontal_line = self.get_horizontal_line(cell.y_pos)
            horizontal_line.get_missing_numbers()

            vertical_line = self.get_vertical_line(cell.x_pos)
            vertical_line.get_missing_numbers()

            quadrant = self.get_quadrant(cell.x_pos, cell.y_pos)
            quadrant.get_missing_numbers()
