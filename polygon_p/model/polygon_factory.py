from abc import ABCMeta, abstractmethod, ABC

from polygon_p.controller.observer import Observable
from polygon_p.model.point import Point


class IPolygon(Point, metaclass=ABCMeta):
    def __init__(self, x, y, side, n):
        super().__init__(x, y)
        self.__side = side
        self.__n = n

    @abstractmethod
    def get_type_polygon(self):
        """The Polygon interface """

    @property
    def get_side(self):
        return self.__side

    @property
    def get_n(self):
        return self.__n

    def set_side(self, side):
        self.__side = side


class Triangle(IPolygon):

    def get_type_polygon(self):
        return "Triangle " + " side: " + str(self.get_side)


class Pentagon(IPolygon):

    def get_type_polygon(self):
        return "Pentagon," + " side: " + str(self.get_side)


class PolygonFactory(Observable):

    def get_polygon(self, polygon_type, x, y, side, n):
        print(side)
        if polygon_type == "Triangle":
            polygon_ = Triangle(x, y, side, n)
            self.notify_observer(polygon_)
            return polygon_
        elif polygon_type == "Pentagon":
            polygon_ = Pentagon(x, y, side, n)
            self.notify_observer(polygon_)
            return polygon_


if __name__ == '__main__':
    polygon = PolygonFactory().get_polygon("Triangle", 10, 30, 30, 40)
    print(polygon.get_type_polygon())
