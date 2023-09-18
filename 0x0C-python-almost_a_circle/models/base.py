#!/usr/bin/python3
"""module that contains Base class"""
import json


class Base:
    """Base of all classes"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initialized attributes for Base class

        Args:
            id (int): integer argument
        """
        self.id = id

    @property
    def id(self):
        """Getter for the id attribute"""
        return self.__id

    @id.setter
    def id(self, value):
        """setter for the id attribute"""
        if value is not None:
            self.__id = value
        else:
            Base.__nb_objects += 1
            self.__id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """a static method that returns the JSON string representation"""
        if list_dictionaries is not None or list_dictionaries is not []:
            return json.dumps(list_dictionaries)
        else:
            return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """a classmethod that writes the JSON string representation"""
        name = cls.__name__ + ".json"
        new_list = []
        if list_objs is None:
            return "[]"
        for obj in list_objs:
            new_list.append(obj.to_dictionary())
        with open(name, 'w', encoding="utf-8") as file:
            file.write(cls.to_json_string(new_list))
