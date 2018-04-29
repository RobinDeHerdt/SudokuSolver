class Cell(object):

    def __init__(self, x_pos, y_pos, value):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.value = value

    def __repr__(self):
        return str(self.value)

    def print(self):
        print(self.value)
