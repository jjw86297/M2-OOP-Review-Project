from abc import ABC, abstractmethod
import math

from BasicShape import BasicShape

class Circle(BasicShape):

    def __init__(self, x, y, r, n="Circle"):
        super().__init__()
        self._x_center = x
        self._y_center = y
        self._radius = r
        self._name = n
        self.calc_area()

    @property
    def x_center(self):
        return self._x_center

    @property
    def y_center(self):
        return self._y_center

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, r):
        self._radius = r
        self.calc_area()

    def calc_area(self):
        self._area = math.pi * (self._radius ** 2)



