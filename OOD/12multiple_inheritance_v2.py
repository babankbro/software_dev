class T:
    def f(self):
        print("Top")

class L(T):
    def f(self):
        print("Left")  
        T.f(self) 
        
class R(T):
    def f(self):
        print("Right")
        T.f(self)

class B(L, R):
    def f(self):
        print("Button")
        L.f(self)
        R.f(self)
        
b = B()
b.f()
print(B.mro())