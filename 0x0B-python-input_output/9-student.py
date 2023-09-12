#!/usr/bin/python3
"""module that contains a Student class"""


class Student:
    """a class Student that defines a student """

    def __init__(self, first_name, last_name, age):
        """initialized attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation of a Student instance"""
        return(self.__dict__)
