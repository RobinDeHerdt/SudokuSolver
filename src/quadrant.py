from src.cell import Cell


class Quadrant(object):

    def __init__(self, quadrant):
        self.quadrant = quadrant

    def print(self):
        print(self.quadrant)

    def get_missing_numbers(self):
        missing_numbers = []

        for i in range(1, 10):
            if i in self.quadrant:
                continue

            missing_numbers.append(i)

        return missing_numbers

    def get_cells(self):
        cells = []
        for cell in self.quadrant:
            cells.append(Cell(cell))

        return cells
