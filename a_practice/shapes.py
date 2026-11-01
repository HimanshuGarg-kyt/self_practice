import math

class Circle:
    def __init__(self,radius):
        self.radius = radius

    def circumference(self):
        return f"{2*3.14159*self.radius}"

    def area(self):
        return f"{3.14159*self.radius*self.radius}"

# print("shapes.py: __name__ is", __name__) 
if __name__ == "__main__": 
    c = Circle(5) 
    print(c.area(), c.circumference()) 
else: 
    pass