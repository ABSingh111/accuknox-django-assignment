# Rectangle class
# This class takes length and width during object creation

class Rectangle:

    # Constructor method
    # Initializes length and width
    def __init__(self, length: int, width: int):

        self.length = length
        self.width = width

    # __iter__ method makes the object iterable
    # It returns values one by one during iteration
    def __iter__(self):

        # First return length in dictionary format
        yield {'length': self.length}

        # Then return width in dictionary format
        yield {'width': self.width}


# Creating Rectangle object
r = Rectangle(10, 5)

# Iterating over Rectangle object
for item in r:
    print(item)