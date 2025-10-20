

class Boats:


    def __init__(self, name, part, pos):
        self.name = name
        self.part = part
        self.pos = set(pos)
        self.hits = set()

    def is_hit(self, coord):
        if coord in self.pos:
            self.hits.add(coord)
            return True
        return False

    def is_sunk(self):
        return self.pos == self.hits
