class Cell(object):

    def __init__(self, value):
        self.value = value

    def print(self):
        print(self.value)

    def get_value(self):
        return self.value