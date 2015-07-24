class TextBoard:
        'Text-based board for Chess Pieces'

        def __init__(self):
                self.pieces = []

        def __str__(self):
                letters = ["a", "b", "c", "d", "e", "f", "g", "h"]
                board = "\nBOARD VIEW:\n"
                board+=( str("   "))
                for a in range(0, 8):
                        board+=(str("[") + str(letters[a]) + str("]"))
                board+=str("\n")
                for y in range(8, 0, -1):
                        board+=(str("[") + str(y) + str("]"))
                        for x in range(0, 8):
                                board+=(str("[") + str(self.getPieceText(y, x+1)) + str("]"))
                        board+=str("\n")
                return board

        def addPiece(self, piece):
                self.pieces.append(piece)

        def getPieceText(self, row, col):
            response = " "
            for piece in self.pieces:
                if row == piece.row and col == piece.col:
                    response = piece.toTextBoard()
            return response
                

class Piece:
    'General base class for all Chess Pieces'

    def __init__(self, type, color, side, row, col):
        self.type = type
        self.color = color
        self.side = side
        self.row = row
        self.col = col

    def __str__(self):
        return "Color: {0}, Side: {1}".format(self.color, self.side)

    def toTextBoard(self):
        return str(self.type[0])


p1 = Piece("Nnight", "white", "left", 1, 2)
p2 = Piece("Nnight", "white", "right", 1, 7)

board = TextBoard()
board.addPiece(p1)
board.addPiece(p2)

print(board)
