from __future__ import annotations
import re
from abc import ABC, abstractmethod
from math import fabs, tan
from typing import Optional
from polygon_p.controller.service import Command

class Service():

    def execute(self, name_service):
        if name_service == "Square":
            return Square()
        if name_service == "Perimeter":
            return Perimeter()

class Square(Service):

    def operation(self, n, a) -> float:
        if re.search("[a-zA-Z]", str(n)) or re.search("[a-zA-Z]", str(a)):
            raise Exception("Error incorrect input data")
        return n * a ** 2 / 4.0 * fabs(tan(180 / float(n)))


class Perimeter(Service):
    def operation(self, n, a) -> float:
        if re.search("[a-zA-Z]", str(n)) or re.search("[a-zA-Z]", str(a)):
            raise Exception("Error incorrect input data")
        return a * n

if __name__ == '__main__':
    print(Service().execute("Square").operation(10,50))
