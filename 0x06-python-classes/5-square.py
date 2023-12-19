#!/usr/bin/python3
"""Define a Square"""
class Square:
    """Represent a square"""
    def __init__(self, size=0):
        """Initialize a square
        args: size=0 """
        if not (isinstance(size, int)):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    def area(self):
        """Returns square area
        args: self"""
        return self.__size ** 2
    @property
    def size(self):
        """Retrieve size"""
        return self.__size
    @size.setter
    def size(self, value):
        """Set size value
        args: value"""
        if not (isinstance(value, int)):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = valuð
    def my_print(self):
        """prints a square"""
        if self.__size == 0:
            print()
        else:
            for j in range(self.__size):
                for i in range(self.__size):
                    print('#', end="")
                    print()
