from abc import ABCMeta, abstractmethod, ABC

from polygon_p.model.point import Point


class IPolygon(metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def get_type_polygon():
        """The Polygon interface """


class Triangle(IPolygon, Point):
    def __init__(self, x, y, side, n=3):
        super().__init__(x, y)
        self.__side = side
        self.__n = n

    @property
    def get_side(self):
        return self.__side

    @property
    def get_n(self):
        return self.__n

    def get_type_polygon(self):
        return "Triangle " + " side: " + str(self.__n)


class Pentagon(IPolygon, Point):
    def __init__(self, x, y, side, n=5):
        super().__init__(x, y)
        self.__side = side
        self.__n = n

    def get_type_polygon(self):
        return "Pentagon," + " side: " + str(self.__n)

    @property
    def get_side(self):
        return self.__side

    @property
    def get_n(self):
        return self.__n


class PolygonFactory():

    @staticmethod
    def get_polygon(polygon_type, x, y, side):
        if polygon_type == "Triangle":
            return Triangle(x, y, side)
        if polygon_type == "Pentagon":
            return Pentagon(x, y, side)


if __name__ == '__main__':
    polygon = PolygonFactory.get_polygon("Triangle", 10, 30, 30)
    print(polygon.get_type_polygon())
