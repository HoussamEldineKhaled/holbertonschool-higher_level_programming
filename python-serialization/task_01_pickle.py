#!/usr/bin/python3
"""custom classes"""


import pickle


class CustomObject:

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))
    
    def serlialize(self, filename):

        try:
            with open(filename, "wb") as file:
                pickle.dump(self, filename)
        except (pickle.PickleError, IOError, Exception) as e:
            return None

    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename, "rb") as file:
                return pickle.load(cls)
        except (pickle.PickleError, IOError, Exception) as e:
            return None
