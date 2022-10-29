class Rectangle(object):
    """ Rectangle class """

    def __init__(self, width=1, height=2):
        """Init"""
        self.width = width
        self.height = height

    def area(self):
        """Area"""
        return self.width * self.height

    def perimeter(self):
        """Perimeter"""
        return 2 * (self.width + self.height)

my_rec = Rectangle (3,4)
print(my_rec.area())
print(my_rec.perimeter())

my_rec = Rectangle ()
print(my_rec.perimeter())
