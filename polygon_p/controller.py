from polygon_p.basic_service import Parse
from polygon_p.basic_service import CalculateService
# from polygon_p.interfaceCommand import Command
from polygon_p.interfaceCommand import Command
from polygon_p.polygon import Polygon
from polygon_p.view import View


class Controller(Command):
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

    def show_square_service(self):
        try:
            return self.view.show_value_of_square(self.model.calculate_square())
        except Exception as ex:
            return self.view.show_error(ex)


if __name__ == '__main__':
    controller = Controller(Polygon(10, 30, 60, 70), View())
    controller.execute("40 50F 70 100").update_model_data().show_square_service()
