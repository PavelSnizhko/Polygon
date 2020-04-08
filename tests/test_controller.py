from unittest import TestCase

from polygon_p.controller.parser import CalculateService
from polygon_p.controller import Controller
from mock import patch


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


    def test_service_perimeter(self):
        self.controller.model.get_n.return_value = 10
        self.controller.model.get_a.return_value = 5

        self.assertEqual(CalculateService.calculate_perimeter(self.controller.model.get_n(),
                                                              self.controller.model.get_a()), 50)
        self.controller.model.get_n.return_value = "d"
        self.controller.model.get_a.return_value = "S"

        with self.assertRaises(Exception) as context:
            CalculateService.calculate_perimeter(self.controller.model.get_n(),
                                                 self.controller.model.get_a())
        self.assertTrue("Error incorrect input data" in str(context.exception))


    def test_service_square(self):
        self.controller.model.get_n.return_value = 10
        self.controller.model.get_a.return_value = 5

        self.assertEqual(CalculateService.calculate_square(self.controller.model.get_n(),
                                                              self.controller.model.get_a()), 71.08210702110543)

        self.controller.model.get_n.return_value = "d"

        with self.assertRaises(Exception) as context:
            CalculateService.calculate_square(self.controller.model.get_n(),
                                                 self.controller.model.get_a())
        self.assertTrue("Error incorrect input data" in str(context.exception))