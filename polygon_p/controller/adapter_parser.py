from __future__ import annotations
import re
from math import fabs, tan
from typing import Optional
from abc import ABCMeta, abstractmethod

from polygon_p.controller.service import CalculateService
from polygon_p.model.polygon_factory import PolygonFactory
from polygon_p.controller.parser import Parser



class AdapterPolygon(PolygonFactory, CalculateService):
    def __init__(self, arg_string):
        super().__init__()
        self.parser = Parser(arg_string)


    def get_polygon(self):
        arguments = self.parser.argument_parser().get_arguments()
        polygon = PolygonFactory.get_polygon(arguments[0], arguments[1], arguments[2], arguments[3])
        return polygon


