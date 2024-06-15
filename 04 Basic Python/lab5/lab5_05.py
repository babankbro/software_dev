from lab5_04 import top_leaf
from lab5_03 import line_base
# copy จาก lab5_02.py
def middle_leaf():
    print("2. Draw middle leaf.")
    
def bottom_leaf():
    print("3. Draw bottom leaf.")

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