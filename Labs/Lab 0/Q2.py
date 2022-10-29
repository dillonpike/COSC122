class Rectangle(object):
    """ Implements a simple rectangle class '"""
    def __init__(self, width=1, height=2):
        """Init"""
        self.width = width
        self.height = height

    def __str__(self):
        """Print"""
        string = ''
        for i in range(self.height):
            string += '#' * self.width
            if i != self.height-1:
                string += '\n'
        return string

recker = Rectangle(3,2)
print(recker)

recker = Rectangle(2,3)
print(recker)

recker = Rectangle(20,5)
print(recker)
