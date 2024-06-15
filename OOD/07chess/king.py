#from piece import Piece
import piece

class King(piece.Piece):
    def __init__(self, color, shape):
        super().__init__(color)
        self.shape = shape
        
    def move(self):
        print("King move!")