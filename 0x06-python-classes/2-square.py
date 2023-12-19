#!/usr/bin/python3
"""Define Square class"""
class Square:
    def __init__(self, size=0):
        """Represent a square
        Args: size """
        try:
            self.__size = size
            if size < 0:
                raise(ValueError)
        except TypeError:
            print("size must be an integer")
        except ValueError:
            print("size must be >= 0")
