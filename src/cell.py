class Cell(object):

    x_pos = 0
    y_pos = 0
    value = 0

    def __init__(self, x_pos, y_pos, value):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.value = value

    def print(self):
        print(self.value)
