class Boats:
    """
    This class is used to creat boats for the naval battle.
    """

    def __init__(self, name, pos):
        """
        This function creates boats for the naval battle, each
        of them have a name, number of parts and positions.
        :param name: the name of the boat.
        :param pos: the positions of the boat.
        """
        self.name = name
        self.pos = set(pos)
        self.hits = set()


    def is_hit(self, coord):
        """
        This function checks if the given coordinate are the coordinate of one of
        the boat, if that's the case then we return True else False.
        :param coord: the coordinate to check.
        :return: a boolean according to the condition.
        """
        if coord in self.pos:
            self.hits.add(coord)
            return True
        return False


    def is_sunk(self):
        """
        This function checks if all boat's positions are hit or not.
        If that's the case then the boat is sunk, else not.
        :return: a boolean.
        """
        return self.pos == self.hits
