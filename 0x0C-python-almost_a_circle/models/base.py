#!/usr/bin/python3

class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        self.id = id

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        if value is not None:
            self.__id = value
        else:
            Base.__nb_objects += 1
            self.__id = self.__nb_objects
