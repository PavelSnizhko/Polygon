from abc import ABCMeta, abstractmethod
from math import fabs, tan


class Command(metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def calculate(n, a):
        raise NotImplementedError()


class CalculateService(Command):

    def calculate(self, n, a):
        return n * a ** 2 / 4.0 * fabs(tan(180 / float(n)))
