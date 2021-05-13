import math
class circle:   
    def __init__(self, radius):
        self.radius = int(radius)
    def calculate_area(self):
        area =math.pi*self.radius**2
        return print(f'area = {area}')
circle = circle(3)
circle.calculate_area()
