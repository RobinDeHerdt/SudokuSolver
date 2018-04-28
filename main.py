from src.board import Board

board = Board([
    [False, 7, 3, 1, False, False, 9, False, False],
    [False, 2, False, False, False, False, False, False, 3],
    [False, False, False, False, False, 8, 1, 2, False],
    [6, False, 7, False, 1, 2, False, 3, 9],
    [False, False, 9, 4, 5, 3, 7, False, False],
    [3, 1, False, 7, 6, False, 2, False, 8],
    [False, 6, 8, 3, False, False, False, False, False],
    [1, False, False, False, False, False, False, 7, False],
    [False, False, 4, False, False, 5, 3, 1, False],
])

board.solve()
