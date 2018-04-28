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
        for line in self.board:
            line_string = ""
            for cell in line:
                if not cell.value:
                    line_string += ". "
                    continue

                line_string += str(cell.value) + " "

            print(line_string)

    def build(self):
        tmp_board = []
        for line_index, line_values in enumerate(self.board, start=1):
            line = []
            for cell_index, cell_value in enumerate(line_values, start=1):
                line.append(Cell(cell_index, line_index, cell_value))

            tmp_board.append(line)

        self.board = tmp_board

    def get_horizontal_line(self, y_pos):
        cells = []
        for line in self.board:
            for cell in line:
                if cell.y_pos == y_pos:
                    cells.append(cell)

        return Region(cells)

    def get_vertical_line(self, x_pos):
        cells = []
        for line in self.board:
            for cell in line:
                if cell.x_pos == x_pos:
                    cells.append(cell)

        return Region(cells)

    def get_quadrant(self, x_pos, y_pos):
        x_start = (x_pos // 3) * 3
        y_start = (y_pos // 3) * 3

        sliced_board = self.board[x_start:x_start+3]
        for index, line in enumerate(sliced_board):
            sliced_board[index] = line[y_start:y_start+3]

        cells = []
        for line in sliced_board:
            for cell in line:
                cells.append(cell)

        return Region(cells)

    def solve(self):
        for line in self.board:
            for cell in line:
                possibilities = self.get_possibilities(cell)

    def get_possibilities(self, cell):
        possibilities = {i for i in range(1, 10)}

        horizontal_line = self.get_horizontal_line(cell.y_pos)
        possibilities -= set(horizontal_line.get_cell_values())

        vertical_line = self.get_vertical_line(cell.x_pos)
        possibilities -= set(vertical_line.get_cell_values())

        quadrant = self.get_quadrant(cell.x_pos, cell.y_pos)
        possibilities -= set(quadrant.get_cell_values())

        return list(possibilities)