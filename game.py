from grid import Grid
from boats import Boats


class Game:
    """
    This class contains the logiq of the game.
    """
    def __init__(self):
        """
        This function initializes the game variables.
        """
        self.grid = Grid()
        self.boats = self.setup_of_boats()
        self.played_coords = set()

    @staticmethod
    def setup_of_boats():
        """
        This function creates a list of boats with the Boats class.
        :return: a list of boats.
        """
        return [
             Boats('aircraft', [('B', '2'), ('C', '2'), ('D', '2'), ('E', '2'), ('F', '2')]),
             Boats('cruiser', [('A', '4'), ('A', '5'), ('A', '6'), ('A', '7')]),
             Boats('destroyer', [('C', '5'), ('C', '6'), ('C', '7')]),
             Boats('submarine',  [('H', '5'), ('I', '5'), ('J', '5')]),
             Boats('torpedo',  [('E', '9'), ('F', '9')])
         ]

    def play(self):
        """
        This function plays the game, it first asks user to
        put a coordinate, then it checks if the hit is valid and wasn't already played,
        then it add the coordinate to 'played_coords' and calls process_hit to check
        if the boat is hit or not.
        If all boats are sunk it display the winning message.
        """
        while True:
            user_input = input("\nEnter coordinate (ex: A2, B3, etc) or 'quit': ").strip().upper()
            if user_input == 'QUIT':
                print('\nThank you for playing!')
                break

            if len(user_input) not in [2,3]:
                print("Invalid input. Please try again.")

            x, y = user_input[0], user_input[1:]
            if x not in self.grid.grid.columns or y not in self.grid.grid.index:
                print("Invalid coordinate! Column must be A–J and row 1–10.")
                continue

            coord = (x, y)
            if coord in self.played_coords:
                print("You already played that coord! Try a new one")
                continue

            self.played_coords.add(coord)
            self.process_hit(coord)

            if all(boats.is_sunk() for boats in self.boats):
                print('\n===================================')
                print('     Congratulations! You Won!  ')
                print('===================================')
                break

    def process_hit(self, coord):
        """
        This function processes the coordinate, and displays the
        message accordingly, then it displays the updated grid.
        :param coord: the coordinate entered by the user.
        :return: a message about the hit and the updated grid.
        """
        for boat in self.boats:
            if boat.is_hit(coord):
                self.grid.update(coord[1], coord[0], 'X')
                if boat.is_sunk():
                    print(f"\n!!!!!!! You sunk the {boat.name}! !!!!!!!!\n")
                    for bx, by in boat.pos:
                        self.grid.update(by, bx, '█')
                else:
                    print("Nice! You touched a boat!")
                break
        else:
            self.grid.update(coord[1], coord[0], 'O')
            print('You missed! Try again')

        remaining = sum(not b.is_sunk() for b in self.boats)
        print(f"--------> {remaining} boats left !<----------\n")
        self.grid.display()
