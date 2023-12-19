#!/usr/bin/python3
"""Define a Square"""
class Square:
    """Represent a square"""
    def __init__(self, size=0, position=(0,0)):
        """Initialize a square
        args: size=0
        posittion=(0,0)"""
        if not (isinstance(size, int)):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        if not (isinstance(position, tuple) and len(position) == 2 and isinstance(value[0], int)
                and isinstance(value[1], int)
                and value[0] >= 0
                and value[1] >= 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__size = size
        self.__position = position
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
        self.__size = value
    def position(self):
        """retrive position"""
        return self.__position
    
    def position(self, value):
        """set position"""
        if not (isinstance(value, tuple)
                and len(value) == 2
                and isinstance(value[0], int)
                and isinstance(value[1], int)
                and value[0] >= 0
                and value[1] >= 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value    
    def my_print(self):
        """prints a square in #"""
        if self.__size == 0:
            print()
        else:
            for y in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for x in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()
