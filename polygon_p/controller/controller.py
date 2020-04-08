from polygon_p.controller.parser import Parser
from polygon_p.controller.parser import CalculateService
# from polygon_p.interfaceCommand import Command
from polygon_p.controller.service import Service
from polygon_p.model.polygon import Polygon
from polygon_p.view.view import View


class Controller(Service):
    """use aggregation in execute method"""

    def __init__(self, model, view, parse):
        self.model = model
        self.view = view
        self.parser = parse

    def execute(self, string_arguments):
        self.parser.argument_parser(input_string=string_arguments)
        if self.parser.get_was_error():
            return self.view.show_error(self.parser.get_error_message())
        else:
            return self

    def update_model_data(self):
        try:
            x, y, number_sides, side_length = self.parser.get_arguments()
            self.model.update(x, y, number_sides, side_length)
            return self
        except Exception as ex:
            return self.view.show_error(ex)

    def show_service_square(self):
        try:
            return self.view.show_value_of_square(CalculateService.calculate_square(self.model.get_n(),
                                                                                    self.model.get_a()))
        except Exception as ex:
            self.view.show_error(ex)

    def show_service_perimeter(self):
        try:
            self.view.show_value_of_perimeter(CalculateService.calculate_perimeter(self.model.get_n(),
                                                                                  self.model.get_a()))
        except Exception as ex:
            return self.view.show_error(ex)


if __name__ == '__main__':
    controller = Controller(Polygon(10, 30, 60, 70), View(), Parser())
    controller.execute("40 50 70 100").update_model_data().show_service_square()
