class Piece:
    'General base class for all Chess Pieces'

    def __init__(self, color, side):
        self.color = color
        self.side = side

    def __str__(self):
        return "Color: {0}, Side: {1}".format(self.color, self.side)

        __repr__ = __str__

p = Piece("white", "left")
print p
