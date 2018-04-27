from src.cell import Cell


class Region(object):

    def __init__(self, cells):
        self.cells = cells
        self.cell_values = self.get_cell_values()

    def print(self):
        print(self.cells)

    def get_missing_numbers(self):
        missing_numbers = []
        for i in range(1, 10):
            if i in self.cell_values:
                continue

            missing_numbers.append(i)

        return missing_numbers

    def get_cells(self):
        return self.cells

    def get_cell_values(self):
        results = []
        for cell in self.cells:
            results.append(cell.value)

        return results