import pandas as pd


class Grid:
    """
    This class create a grid of naval battle.
    """
    def __init__(self, size = 10):
        """
        This function creates a grid of naval battle of n size.
        :param size: the size of the grid.
        """
        self.size = size
        self.grid = pd.DataFrame(
            [['~'] * size for _ in range(size)],
            index = [str(i+1) for i in range(size)],
            columns = [chr(65+ i ) for i in range(size)],
        )

    def update(self, x, y, symbol):
        """
        This function updates the grid with the given symbol
         at the given coordinates.
        :param x: the x coordinate.
        :param y: the y coordinate.
        :param symbol: the symbol to update.
        """
        self.grid.at[x,y] = symbol

    def display(self):
        """
        This function displays the grid.
        :return: the grid.
        """
        print(self.grid.to_string())
