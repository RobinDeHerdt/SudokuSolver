from src.board import Board
from tkinter import *


def init(existing_board=None):
    rows = []

    def submit():
        board = Board(get_grid_field_values(rows))
        board.solve()

    root = Tk()
    root.title("Sudoku solver")

    for line_index, line in enumerate(range(0, 9)):
        fields = []
        for cell_index, cell in enumerate(range(0, 9)):
            e = Entry(root, width=2)

            # When importing an existing board, make sure
            # it is in the correct format, to prevent index errors.
            if existing_board:
                try:
                    if existing_board[line_index][cell_index]:
                        e.insert('0', existing_board[line_index][cell_index])
                except (IndexError, ValueError):
                    print("Invalid existing board format")
                    root.destroy()
                    quit()

            e.grid(column=cell_index, row=line_index, padx=2.5, pady=2.5)
            fields.append(e)

        rows.append(fields)

    submit = Button(root, text="Solve", command=submit)
    submit.grid(row=9, columnspan=9, sticky='e')


def get_grid_field_values(grid_rows):
    results = []
    for row in grid_rows:
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

init(example_board)
mainloop()
