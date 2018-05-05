from sudoku_solver.board import Board
from tkinter import *


class SudokuSolver(object):
    status = None

    def __init__(self, initial_board=None):
        self.window = Tk()

        self.status = Label(self.window)

        self.grid = self.build_entry_fields()
        self.build(initial_board)

    @staticmethod
    def get_default_board():
        default_board = []
        for i in range(0, 9):
            fields = []
            for j in range(0, 9):
                fields.append(False)

            default_board.append(fields)

        return default_board

    def build_entry_fields(self):
        grid = []
        for i in range(0, 9):
            fields = []
            for j in range(0, 9):
                e = Entry(self.window, width=2)
                e.grid(column=j, row=i, padx=2.5, pady=2.5)
                fields.append(e)

            grid.append(fields)

        return grid

    def build(self, board=None):
        self.window.title("Sudoku solver")
        for line_index, line in enumerate(self.grid):
            for field_index, field in enumerate(line):
                if not board:
                    board = self.get_default_board()

                # When importing an existing board, make sure
                # it is in the correct format, to prevent index errors.
                try:
                    # Clear each field
                    field.delete(0, END)

                    # When there's no value for the field,
                    # don't insert anything.
                    if not board[line_index][field_index]:
                        continue

                    field.insert(0, board[line_index][field_index])

                except (IndexError, ValueError):
                    print("Invalid board format")
                    self.window.destroy()
                    quit()

        btn_solve = Button(self.window, text="Solve", command=self.solve)
        btn_solve.grid(row=9, columnspan=9, sticky='e')

        btn_clear = Button(self.window, text="Clear", command=self.clear)
        btn_clear.grid(row=9, columnspan=7, sticky='e')

    def solve(self):
        # Construct a board object, based on the raw field values.
        board = Board(self.get_board_raw_values())

        # Prepare the status label for display.
        self.status.grid(row=10, columnspan=9, sticky='w')

        solved = board.solve()
        if solved:
            # Populate the board with the found values.
            self.build(board.get_raw_values())
            self.status.configure(text="Solved!")
        else:
            self.status.configure(text="Impossible sudoku!")

    def clear(self):
        self.build()
        self.status.grid_remove()

    def get_board_raw_values(self):
        results = []
        for row in self.grid:
            fields = []
            for field in row:
                value = field.get()
                if value:
                    fields.append(int(value))
                    continue

                fields.append(False)

            results.append(fields)

        return results


easy_example_board = [
    [False, 7, 3, 1, False, False, 9, False, False],
    [False, 2, False, False, False, False, False, False, 3],
    [False, False, False, False, False, 8, 1, 2, False],
    [6, False, 7, False, 1, 2, False, 3, 9],
    [False, False, 9, 4, 5, 3, 7, False, False],
    [3, 1, False, 7, 6, False, 2, False, 8],
    [False, 6, 8, 3, False, False, False, False, False],
    [1, False, False, False, False, False, False, 7, False],
    [False, False, 4, False, False, 5, 3, 1, False],
]

hard_example_board = [
    [False, False, False, False, False, False, False, False, 4],
    [False, False, False, 4, 6, 3, 5, 9, False],
    [False, 1, False, False, False, False, 7, 2, False],
    [False, False, False, 6, False, False, False, 7, 5],
    [False, False, False, 3, 9, 2, False, False, False],
    [6, 9, False, False, False, 1, False, False, False],
    [False, 6, 3, False, False, False, False, 1, False],
    [False, 4, 5, 8, 7, 6, False, False, False],
    [7, False, False, False, False, False, False, False, False]
]

expert_example_board = [
    [False, 7, False, False, False, False, False, False, False],
    [1, False, False, 7, 6, False, 2, False, False],
    [5, False, 3, False, False, 8, False, False, False],
    [False, False, False, False, False, False, 1, 3, False],
    [False, 8, False, 2, False, 4, False, 7, False],
    [False, 4, 5, False, False, False, False, False, False],
    [False, False, False, 5, False, False, 3, False, 7],
    [False, False, 4, False, 8, 1, False, False, 6],
    [False, False, False, False, False, False, False, 8, False]
]

SudokuSolver(hard_example_board)
mainloop()
