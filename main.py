from area_calculator import Rectangle, Square

regular_rectangle = Rectangle(90, 40)
print(regular_rectangle)
print('The perimeter of this rectangle is :', regular_rectangle.get_perimeter())
print('The area of this rectangle is :', regular_rectangle.get_area())
print()

regular_square = Square(50)
print(regular_square)
print('The perimeter of this square is :', regular_square.get_perimeter())
print('The area of this square is :', regular_square.get_area())