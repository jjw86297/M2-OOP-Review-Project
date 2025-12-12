from abc import ABC, abstractmethod
import math

from Rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, s, n="Square"):
        self._side = s
        super().__init__(s, s, n)
        self._name = n

    @property
    def side(self):
        return self._side

    @side.setter
    def side(self, s):
        self._side = s
        self.length = s
        self.width = s

