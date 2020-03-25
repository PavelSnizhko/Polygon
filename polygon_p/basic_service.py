import re
from math import fabs, tan


class Parse(object):
    def __init__(self):
        self.__input = ""
        self.__is_parsed = False
        self.__was_error = False
        self.__error_message = ""
        self.__arguments = []

    def argument_parser(self, input_string):
        self.__input = input_string
        if re.search("[a-zA-Z]", self.__input):
            self.__was_error = True
            self.__error_message = "Error! Letters  a-z  didn't allow!"
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


class CalculateService(object):

    @staticmethod
    def calculate_square(n, a):
        return n * a ** 2 / 4.0 * fabs(tan(180 / float(n)))

    @staticmethod
    def calculate_perimeter(n, a):
        return a * n

