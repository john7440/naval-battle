from grid import Grid
from boats import Boats


class Game:

    def __init__(self):
        self.grid = Grid()
        self.boats =self.setup_of_boats()
        self.played_coords = set()

    @staticmethod
    def setup_of_boats():
         return [
             Boats('aircraft', 5, [('B', '2'), ('C', '2'), ('D', '2'), ('E', '2'), ('F', '2')]),
             Boats('cruiser', 4, [('A', '4'), ('A', '5'), ('A', '6'), ('A', '7')]),
             Boats('destroyer', 3, [('C', '5'), ('C', '6'), ('C', '7')]),
             Boats('submarine', 3, [('H', '5'), ('I', '5'), ('J', '5')]),
             Boats('torpedo', 2, [('E', '9'), ('F', '9')])
         ]
