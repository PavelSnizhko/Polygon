from __future__ import annotations
import re
from math import fabs, tan
from typing import Optional
from abc import ABCMeta, abstractmethod

from polygon_p.controller.service import CalculateService
from polygon_p.model.polygon_factory import PolygonFactory



class SingletonMeta(type):
    """
    The Singleton class can be implemented in different ways in Python. Some
    possible methods include: base class, decorator, metaclass. We will use the
    metaclass because it is best suited for this purpose.
    """

    _instance: Optional[Parser] = None

    def __call__(self, string) -> Parser:
        if self._instance is None:
            self._instance = super().__call__(string)
        return self._instance


class AdapterPolygon(PolygonFactory):
    def __init__(self, arg_string):
        super().__init__()
        self.parser = Parser(arg_string)


    def get_polygon(self):
        arguments = self.parser.argument_parser().get_arguments()
        polygon = PolygonFactory.get_polygon(arguments[0], arguments[1], arguments[2], arguments[3])
        return polygon

class Parser(object, metaclass=SingletonMeta):
    def __init__(self, string):
        self.st = string
        self.__input = string
        self.__is_parsed = False
        self.__was_error = False
        self.__error_message = ""
        self.__arguments = []
        self.__name_polygon = ""

    def argument_parser(self):
        try:
            arguments_ = [val for val in self.__input.split(" ")]
            self.__name_polygon = arguments_.pop(0)
            self.__arguments = [int(val) for val in arguments_]
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
            return self.__name_polygon, self.__arguments[0], self.__arguments[1], \
                   self.__arguments[2]
        raise Exception

