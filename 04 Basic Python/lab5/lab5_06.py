from lab5_04 import top_leaf
from lab5_03 import line_base
# copy จาก lab5_02.py
def middle_leaf():
    line_base(2, 3)
    line_base(1, 5)
    line_base(0, 7)
    
def bottom_leaf():
    line_base(2, 5)
    line_base(1, 7)
    line_base(0, 9)

def base():
    line_base(2, 3)
    line_base(2, 3)
    line_base(2, 3)

def tree():
    print("---------------------------")
    top_leaf()
    middle_leaf()
    bottom_leaf()
    base()
    print("---------------------------")
    
tree()