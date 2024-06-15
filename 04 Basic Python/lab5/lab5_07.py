from lab5_03 import line_base

def top_leaf():
    top_start = 5
    line_base(top_start+ 2, 1)
    line_base(top_start+ 1, 3)
    line_base(top_start+ 0, 5)
    
def middle_leaf():
    middle_start = 2
    line_base(middle_start + 4, 3)
    line_base(middle_start + 2, 7)
    line_base(middle_start + 0, 11)
    
def bottom_leaf():
    line_base(5, 5)
    line_base(3, 9)
    line_base(0, 15)

def base():
    base_start = 6
    line_base(base_start, 3)
    line_base(base_start, 3)
    line_base(base_start, 3)

def tree():
    print("---------------------------")
    top_leaf()
    middle_leaf()
    bottom_leaf()
    base()
    print("---------------------------")
    
tree()