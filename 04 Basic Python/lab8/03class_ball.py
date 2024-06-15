class Ball:
    def __init__(self, color, size, wieght):
        self.color = color #attribute
        self.size = size
        self.weight = wieght
    
    def display(self): # method function 
        print("Ball:")
        print(f"\tColor: {self.color}")
        print(f"\tSize: {self.size} cm.")
        print(f"\tWeight: {self.weight} kg.")
    
ball2 = Ball("Green", 20, 2)
ball2.display()
ball = Ball("Red", 12, 1.5)
ball.display()
ball3 = Ball("black", 25, 3)
ball3.display()