from polygon_p.model.interfacePolygon import PolygonInterface
from polygon_p.model.point import Point


class Polygon(Point, PolygonInterface):
    # __closure__ = None

    def __init__(self, x: int, y, n, a):
        super().__init__(x, y)
        self.__n = n
        self.__a = a

    def get_n(self):
        return self.__n

    def set_n(self, n: int):
        self.__n = n

    def get_a(self):
        return self.__a

    def set_a(self, a):
        self.__a = a

    def update(self, x, y, n, a):
        self.set_x(x)
        self.set_y(y)
        self.set_a(a)
        self.set_n(n)




