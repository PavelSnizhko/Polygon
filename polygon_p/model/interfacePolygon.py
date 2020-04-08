import abc

from polygon_p.model.annotaion import check_values


class PolygonInterface(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_n(self):
        raise NotImplementedError()

    @abc.abstractmethod
    def get_a(self):
        raise NotImplementedError()

    # @abc.abstractmethod
    # def calculate_square(self):
    #     raise NotImplementedError()


    @abc.abstractmethod
    @check_values
    def set_n(self, n: int):
        raise NotImplementedError()

    @abc.abstractmethod
    @check_values
    def set_a(self, a):
        raise NotImplementedError()



