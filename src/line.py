class Line(object):

    def __init__(self, line):
        self.line = line

    def print(self):
        print(self.line)

    def get_missing_numbers(self):
        missing_numbers = []

        for i in range(1, 10):
            if i in self.line:
                continue

            missing_numbers.append(i)

        return missing_numbers
