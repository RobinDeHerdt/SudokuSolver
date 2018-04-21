from src.board import Board

board = Board([
    [6, False, 3, 2, 9, 8, 1, 7, False],
    [2, False, False, 1, 7, 4, 6, 5, 3],
    [1, False, False, False, False, 3, 2, 9, 8],
    [False, False, False, 3, 8, 9, 7, 4, 1],
    [3, 8, 9, 7, 4, 1, 5, False, False],
    [False, False, False, 5, 6, 2, 3, False, False],
    [False, False, False, 8, 2, False, 4, 1, False],
    [False, False, 5, 4, 1, 7, 9, 3, 6],
    [4, False, 7, False, False, False, False, 2, 5],
])

board.solve()
