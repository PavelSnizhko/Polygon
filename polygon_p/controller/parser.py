from __future__ import annotations
import re
from math import fabs, tan

from typing import Optional

class SingletonMeta(type):
    """
    The Singleton class can be implemented in different ways in Python. Some
    possible methods include: base class, decorator, metaclass. We will use the
    metaclass because it is best suited for this purpose.
    """

    _instance: Optional[Parser] = None

    def __call__(self,string) -> Parser:
        if self._instance is None:
            self._instance = super().__call__(string)
        return self._instance


class Parser(object, metaclass=SingletonMeta):
    def __init__(self, string):
        self.__input = string
        self.__is_parsed = False
        self.__was_error = False
        self.__error_message = ""
        self.__arguments = []

    def argument_parser(self):
        if re.search("[a-zA-Z]", self.__input):
            self.__was_error = True
        else:
            try:
                self.__arguments = [int(value) for value in self.__input.split(" ")]
                self.__is_parsed = True
            except:
                self.__was_error = True
                self.__error_message = "Error! Can't be parsed"
        return self

    def get_was_error(self):
        return self.__was_error

    def get_error_message(self):
        return self.__error_message

    def get_arguments(self):
        if self.__is_parsed:
            return self.__arguments[0], self.__arguments[1], \
                   self.__arguments[2], self.__arguments[3]
        raise Exception




# class SingletonMeta(type):
#     """
#     The Singleton class can be implemented in different ways in Python. Some
#     possible methods include: base class, decorator, metaclass. We will use the
#     metaclass because it is best suited for this purpose.
#     """
#
#     _instance: Optional[CalculateService] = None
#
#     def __call__(self) -> CalculateService:
#         if self._instance is None:
#             self._instance = super().__call__()
#         return self._instance
#
#
#
#
# class CalculateService(metaclass=SingletonMeta):
#
#
#
#     def calculate_square(self,n, a):
#         if re.search("[a-zA-Z]", str(n)) or re.search("[a-zA-Z]", str(a)):
#             raise Exception("Error incorrect input data")
#         return n * a ** 2 / 4.0 * fabs(tan(180 / float(n)))
#
#
#     def calculate_perimeter(self,n, a):
#         if re.search("[a-zA-Z]", str(n)) or re.search("[a-zA-Z]", str(a)):
#             raise Exception("Error incorrect input data")
#         return a * n
