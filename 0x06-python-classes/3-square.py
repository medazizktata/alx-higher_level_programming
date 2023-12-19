#!/usr/bin/python3
"""Define a Square"""
class Square:
    """Represent a square"""
    def __init__(self, size=0):
        """Initialize a square
        args: size=0 """
        if size < 0:
            raise ValueError("size must be an integer")
        if not (isinstance(size, int)):
            raise TypeError("size must be >= 0")
        self.__size = size
    def area(self):
        """Returns square area
        args: self"""
        return self.__size ** 2
