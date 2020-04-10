from polygon_p.controller.adapter_parser import AdapterPolygon
from polygon_p.controller.service import CalculateService, Meters
from polygon_p.model.polygon_factory import PolygonFactory
from polygon_p.view.view import View


class Controller:
    """use aggregation in execute method"""

    def __init__(self, view, str_):
        self.view = view
        self.calculate_service = CalculateService()
        self.polygon_factory = PolygonFactory()
        self.polygon_factory.add_observer(self.calculate_service)
        self.model = AdapterPolygon(self.polygon_factory, str_).get_polygon()

    @property
    def get_view(self):
        return self.view

    def update_model_data(self, model, _str):
        try:
            self.model = AdapterPolygon(model, _str, ).get_polygon()
            return self
        except Exception as ex:
            return self.view.show_error(ex)

    def show_service_square(self):
        try:
            self.view.show_value_of_square(Meters(self.calculate_service).calculate())
        except Exception as ex:
            self.view.show_error(ex)


if __name__ == '__main__':
    controller = Controller(View(), "Triangle 10 30 40 50")
    controller.show_service_square()
