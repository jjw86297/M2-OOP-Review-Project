from abc import ABC, abstractmethod
import math

from BasicShape import BasicShape

class Rectangle(BasicShape):
    def __init__(self, l, w, n="Rectangle"):
        super().__init__()
        self._length = l
        self._width = w
        self._name = n
        self.calc_area()

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, l):
        self._length = l
        self.calc_area()

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, w):
        self._width = w
        self.calc_area()

    def calc_area(self):
        self._area = self._length * self._width



