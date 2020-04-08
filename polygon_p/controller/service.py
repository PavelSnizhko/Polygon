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



class Decorator(Command, metaclass=ABCMeta):

    def __init__(self, decorated_result)-> None:
        self.decorated_result = decorated_result

    @abstractmethod
    def calculate(self, n, a):
        pass

class Meters(Decorator):

    def __init__(self, decorated_result):
        super().__init__(decorated_result)

    def calculate(self, n, a):
        return self.decorated_result.calculate(n, a)*0.01


if __name__ == '__main__':
    calc = Meters(CalculateService()).calculate(10, 20)
    print(calc)