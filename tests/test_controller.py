from unittest import TestCase
from unittest.mock import Mock

from polygon_p import polygon
from polygon_p import basic_service
from polygon_p.basic_service import Parse
from polygon_p.controller import Controller
from mock import call, patch


class TestController(TestCase):
    def setUp(self) -> None:
        self.patchers = [patch('polygon_p.polygon.Polygon'), patch("polygon_p.view.View"),
                         patch("polygon_p.basic_service.Parse")]
        self.model = self.patchers[0].start()
        self.view = self.patchers[1].start()
        self.parser = self.patchers[2].start()
        self.controller = Controller(self.model, self.view, self.parser)

    def tearDown(self) -> None:
        for patcher in self.patchers:
            patcher.stop()

    def test_execute(self):
        self.controller.parser.get_was_error.return_value = True
        self.controller.view.show_error.return_value = True

        input_string = "10 20 30 50"
        self.assertTrue(self.controller.execute(input_string))

        self.controller.parser.get_was_error.return_value = False
        self.assertEqual(self.controller.execute(input_string), self.controller)

    def test_update_model_data(self):
        self.controller.view.show_error.return_value = "Error"
        self.controller.parser.get_arguments.return_value = [1, 2, 3]
        self.assertEqual(self.controller.update_model_data(), "Error")

        self.controller.parser.get_arguments.return_value = [1, 2, 3, 5]
        self.assertEqual(self.controller.update_model_data(), self.controller)

    def test_show_square_service(self):
        input_string = "2 20 30 50"
        self.controller.model.calculate_square.return_value = 50
        self.controller.view.show_value_of_square.return_value = True
        self.assertTrue(self.controller.show_square_service())
        self.controller.view.show_value_of_square.return_value = False
        self.assertFalse(self.controller.show_square_service())
