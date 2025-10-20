import pandas as pd


class Grid:
    def __init__(self, size = 10):
        self.size = size
        self.grid = pd.DataFrame(
            [['~'] * size for _ in range(size)],
            index = [str(i+1) for i range(size)],
            columns = [chr(65+ i ) for i in range(size)],
        )