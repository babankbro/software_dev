#from myfunction import square
#from myfunction import *
import myfunction

#print( f"Square 3 is { square(3) }." )
print( f"Square 3 is { myfunction.square(3) }." )
print("-------------------------------------")
for i in range(10):
    print( f"Square {i} is { myfunction.square(i) }." )
    
