# Hardcoded for now, find clean solution later
def get_horizontal_indexes(index):
    if index in [1, 2, 3]:
        return [1, 2, 3]

    if index in [4, 5, 6]:
        return [4, 5, 6]

    if index in [7, 8, 9]:
        return [7, 8, 9]


# Hardcoded for now, find clean solution later
def get_vertical_indexes(index):
    if index in [1, 4, 7]:
        return [1, 4, 7]

    if index in [2, 5, 8]:
        return [2, 5, 8]

    if index in [3, 6, 9]:
        return [3, 6, 9]