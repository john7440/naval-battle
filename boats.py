class Boats:
    """
    This class is used to creat boats for the naval battle.
    """

    def __init__(self, name, part, pos):
        """
        This function creates boats for the naval battle.
        :param name: the name of the boat.
        :param part: the number of parts of the boat.
        :param pos: the position of the boat.
        """
        self.name = name
        self.part = part
        self.pos = set(pos)
        self.hits = set()


    def is_hit(self, coord):
        """
        This function checks if the given coordinate is on the boat, if
        that's the case then we update it.
        :param coord: the coordinate to check.
        :return: a boolean according to the condition.
        """
        if coord in self.pos:
            self.hits.add(coord)
            return True
        return False


    def is_sunk(self):
        """
        This function checks if all pos of the boat are hit or not.
        If that's the case then the boat is sunk, else not.
        :return: a boolean.
        """
        return self.pos == self.hits
