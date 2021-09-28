#!/usr/bin/python3
"""Define class square"""


class Square():
    """
        represent a Square
    """

    def __init__(self, size=0):
        '''Initialization of instance attributes
            Args:
            size (int): Zero or positve number.
        '''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
