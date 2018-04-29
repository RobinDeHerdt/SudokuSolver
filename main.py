from sudoku_solver.board import Board
from tkinter import *


class SudokuSolver(object):
    grid = []

    def __init__(self, board=None):
        self.window = Tk()
        self.build(board)

    def build(self, board):
        self.window.title("Sudoku solver")

        for line_index, line in enumerate(range(0, 9)):
            fields = []
            for cell_index, cell in enumerate(range(0, 9)):
                e = Entry(self.window, width=2)

                # When importing an existing board, make sure
                # it is in the correct format, to prevent index errors.
                if board:
                    try:
                        if board[line_index][cell_index]:
                            e.insert('0', board[line_index][cell_index])
                    except (IndexError, ValueError):
                        print("Invalid existing board format")
                        self.window.destroy()
                        quit()

                e.grid(column=cell_index, row=line_index, padx=2.5, pady=2.5)
                fields.append(e)

            self.grid.append(fields)

        submit = Button(self.window, text="Solve", command=self.solve)
        submit.grid(row=9, columnspan=9, sticky='e')

    def solve(self):
        board = Board(self.get_board_from_grid())
        if board.solve():
            self.build(board.board)
            label = Label(self.window, text="Solved!")
            label.grid(row=9, columnspan=9, sticky='w')
            return

        label = Label(self.window, text="Impossible sudoku!")
        label.grid(row=9, columnspan=9, sticky='w')


    def get_board_from_grid(self):
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


example_board = [
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

SudokuSolver(example_board)
mainloop()
