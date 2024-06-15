from player import Player

class DeepBlue(Player):
    def __init__(self, chess_set):
        super().__init__(chess_set)
        
    def caculate_move(self):
        print("Juidiciously pick a piece and make a smart move!")
        
