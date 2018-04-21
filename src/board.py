from src.quadrant import Quadrant
from src.line import Line


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
        for quadrant in self.get_quadrants():
            missing_numbers = quadrant.get_missing_numbers()

            for cell in quadrant.get_cells():
                print(cell.get_value())
