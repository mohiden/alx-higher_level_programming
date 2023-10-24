#!/usr/bin/python3
"""Square class defination"""


class Square:
    """Represents a square
    Attributes:
        __size (int): size of a side of the Square
    """
    def __init__(self, size):
        """Initializes a square
        Args:
            size (int): size of side of square
        Returns: None
        """
        self.__size = size
