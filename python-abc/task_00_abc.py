#!/usr/bin/python3
from abc import ABC, abstractmethod


class Animal(ABC):
    """abstract class for animals"""
    
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    """dog class"""

    def sound(self):
        """

        Returns: dog sounds
        """
        return "Bark"

class Cat(Animal):
    """A concrete class representing cat."""

    def sound(self):
        """

        Returns: cat sounds
        """
        return "Meow"
