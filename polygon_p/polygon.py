from math import fabs, tan

from polygon_p.annotaion import check_values
from polygon_p.basic_service import CalculateService
from polygon_p.interfacePolygon import PolygonInterface
from polygon_p.point import Point


class Polygon(Point, PolygonInterface):
    # __closure__ = None

    def __init__(self, x: int, y, n, a):
        super().__init__(x, y)
        self.__n = n
        self.__a = a

    def get_n(self):
        return self.__n

    def calculate_square(self):
        return self.get_service().calculate_square(self.__n, self.__a)

    def get_service(self):
        return CalculateService()

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

    def __str__(self):
        return "Square of polygon_p is " + str(self.get_service().calculate_square(10, 20))


if __name__ == '__main__':
    polygon = Polygon(2, 303, 4, 5)
    print(polygon)
