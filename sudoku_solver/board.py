from sudoku_solver.cell import Cell
from sudoku_solver.region import Region

import time
import copy


class Board(object):

    iteration = 0

    def __init__(self, board):
        self.start_time = time.time()
        self.board = board
        self.build()

    def solve(self):
        self.iteration += 1

        board_changed = False
        for line_index, line in enumerate(self.board):
            for cell_index, cell in enumerate(line):
                if cell.value:
                    continue

                possibilities = self.get_possibilities(cell)
                if not possibilities:
                    return False

                if len(possibilities) == 0:
                    return False

                # The value of this cell is certain,
                # since there is only one possibility.
                if len(possibilities) == 1:
                    board_changed = True
                    cell.value = possibilities[0]
                    self.board[line_index][cell_index] = cell
                    continue

                # Take a snapshot of the board in its
                # current state, so we can revert later.
                snapshot = copy.deepcopy(self.board)

                # Try to solve the board for each possible value recursively.
                for possibility in possibilities:
                    cell.value = possibility
                    self.board[line_index][cell_index] = cell

                    solved = self.solve()
                    if solved:
                        return True
                    else:
                        # Revert to the previously taken snapshot.
                        self.board = copy.deepcopy(snapshot)

                return False

        # When the board was altered during this loop,
        # loop again
        if board_changed:
            return self.solve()

        # When no changes were made to the board in this loop,
        # end the program.
        execution_time = round(time.time() - self.start_time, 4)
        print("\n FOUND SOLUTION ({0} iterations, {1} seconds) \n".format(self.iteration, execution_time))
        self.print()
        return True

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

        sliced_board = self.board[y_start:y_start+3]
        for index, line in enumerate(sliced_board):
            sliced_board[index] = line[x_start:x_start+3]

        cells = []
        for line in sliced_board:
            for cell in line:
                cells.append(cell)

        return Region(cells)

    def get_possibilities(self, cell):
        if cell.value:
            return False

        possibilities = {i for i in range(1, 10)}

        horizontal_line = self.get_horizontal_line(cell.y_pos)
        possibilities -= set(horizontal_line.get_cell_values())

        vertical_line = self.get_vertical_line(cell.x_pos)
        possibilities -= set(vertical_line.get_cell_values())

        quadrant = self.get_quadrant(cell.x_pos, cell.y_pos)
        possibilities -= set(quadrant.get_cell_values())

        return list(possibilities)

    def print(self):
        for line in self.board:
            print(' '.join(str(cell.value) for cell in line).replace("False", "."))

    def build(self):
        tmp_board = []
        for line_index, line_values in enumerate(self.board):
            line = []
            for cell_index, cell_value in enumerate(line_values):
                line.append(Cell(cell_index, line_index, cell_value))

            tmp_board.append(line)

        self.board = tmp_board
        self.print()

    def get_raw_values(self):
        lines = []
        for line in self.board:
            cells = []
            for cell in line:
                cells.append(cell.value)

            lines.append(cells)

        return lines
