from polygon.interfacePolygon import PolygonInterface
from polygon.polygon import Polygon



class Proxy(PolygonInterface):
    def __init__(self, x: int, y, n, a):
        self.polygon = Polygon(x, y, n, a)

    def get_n(self):
        return self.polygon.get_n()

    def get_a(self):
        return self.polygon.get_a()

    def calculate_square(self):
        return self.polygon.calculate_square()

    def set_n(self, n: int):
        raise Exception("You can't use a setter function")

    def set_a(self, a):
        raise Exception("You can't use a setter function")

if __name__ == '__main__':
    proxy = Proxy(10, 30, 30, 50)

