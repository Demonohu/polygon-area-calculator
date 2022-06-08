"""
GOAL: Create class and sub-class objects which represent 
different geometrical shapes, such as Rectangles and Squares.

Approach: represent geometry shapes as classes and give them 
the ability to compute routine geometry calculations in the 
forms of class methods. Leverage class parent/child 
relationships to extend class functionality.
"""


class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def set_breadth(self, breadth):
        self.breadth = breadth

    def set_length(self, length):
        self.length = length

    def get_perimeter(self):
        perimeter = 2 * (self.length + self.breadth)
        return perimeter

    def get_area(self):
        area = self.breadth * self.length
        return area

    def __str__(self):
        return f'This is a rectangle {self.length}mm long, {self.breadth}mm wide.'

class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)

    def set_sides(self, length):
        self.breadth = length
        self.length = length

    def __str__(self):
        return f'This is a square of length {self.length}mm.'