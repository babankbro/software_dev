from piece import Piece

class PuppetKing(Piece):
    def __init__(self, color, shape):
        super().__init__(color)
        self.shape = shape
        
     