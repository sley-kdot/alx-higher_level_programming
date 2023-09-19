#!/usr/bin/python3
"""module contains a MyInt class"""


class MyInt(int):
    """class MyInt that inherits from int class"""

    def __ne__(self, value):
        """Override the != operator to invert its behavior"""
        return not super().__ne__(value)
 
    def __eq__(self, value):
        """Override the == operator to invert its behavior"""
        return not super().__eq__(value)
