#write a class calculater capable of finding sqaure, cube , square root.
class Calculator():
    
    def __init__(self, num):
        self.num = num
        
    def square(self):
        print(f"The square value of {self.num} is {self.num **2}")
        
    def cube(self):
        print(f"The cube value of {self.num} is {self.num**3}")
        
    def square_root(self):
        print(f"The square root value of {self.num} is {self.num **0.5}")
        
a = Calculator(3)
a.square()
a.cube()
a.square_root()