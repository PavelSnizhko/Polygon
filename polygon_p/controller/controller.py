from polygon_p.controller.adapter_parser import AdapterPolygon
from polygon_p.controller.parser import Parser
# from polygon_p.interfaceCommand import Command
from polygon_p.controller.service import CalculateService, Meters
from polygon_p.model.polygon import Polygon
from polygon_p.model.polygon_factory import PolygonFactory
from polygon_p.view.view import View


class Controller():
    """use aggregation in execute method"""

    def __init__(self, view, str_):
        self.view = view
        self.model = AdapterPolygon(str_).get_polygon()


    @property
    def get_view(self):
        return self.view

    def update_model_data(self, _str):
        try:
            self.model = AdapterPolygon(_str).get_polygon()
            return self
        except Exception as ex:
            return self.view.show_error(ex)

    def show_service_square(self):
        try:
            self.view.show_value_of_square(Meters(CalculateService()).
                                           calculate(self.model.get_n, self.model.get_side))
        except Exception as ex:
            self.view.show_error(ex)



if __name__ == '__main__':
    controller = Controller(View(), "Triangle 10 30 40")
    controller.show_service_square()
