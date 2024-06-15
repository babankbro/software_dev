class Piece:
    def __init__(self, color):
        self.color = color
    
    def move(self):
        raise NotImplementedError("Subclass")