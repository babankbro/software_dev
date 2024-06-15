class T:
    def f(self):
        print("Top")

class L(T):
    def f(self):
        print("Left")  
        super().f() 
        
class R(T):
    def f(self):
        print("Right")
        super().f() 

class B(R, L):
    def f(self):
        print("Button")
        super().f() 
        
b = B()
b.f()
print(B.mro())