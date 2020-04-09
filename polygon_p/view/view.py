import re


class View:

    @staticmethod
    def input_data(arg_string):
        return arg_string

    @staticmethod
    def show_number_side(number_of_side):
        print("--------The polygon_p has  {} sides".
              format(number_of_side))

    @staticmethod
    def show_length_side(length_of_side):
        print("---------A length of polygon_p is  {}".
              format(length_of_side))

    @staticmethod
    def show_value_of_square(square):
        print("---------Square is a {}".format(square))

    @staticmethod
    def show_value_of_perimeter(perimeter):
        if re.search("[a-zA-Z]", perimeter):
            raise Exception("Error! Don't allow using letter in perimeter")
        else:
            print("Perimeter is a {}".format(perimeter))

    @staticmethod
    def show_error(message):
        print(message)
