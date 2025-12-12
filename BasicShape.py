from abc import ABC, abstractmethod
import math

class BasicShape(ABC):
    def __init__(self):
        self._area = 0.0
        self._name = ""

    @property
    def area(self):
        return self._area

    @area.setter
    def area(self, value):
        self._area = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @abstractmethod
    def calc_area(self):
        pass