import pytest
from src.circle import Circle


class TestPositive:
    @pytest.mark.parametrize('radius', [10, 6.3, 30])
    def test_circle_creation(self, radius):
        circle = Circle(radius)
        assert circle.name == 'Circle', 'Expected name is "Circle"'

    @pytest.mark.parametrize('radius, expected_perimeter', [(10, 62.83), (6.3, 39.58)])
    def test_circle_perimeter_calculation(self, radius, expected_perimeter):
        circle = Circle(radius)
        assert circle.perimeter == expected_perimeter, 'Expected correct perimeter'

    @pytest.mark.parametrize('radius, expected_area', [(10, 314.16), (6.3, 124.69)])
    def test_circle_area_calculation(self, radius, expected_area):
        circle = Circle(radius)
        assert circle.area == expected_area, 'Expected correct area'

    @pytest.mark.parametrize('radius_1, radius_2, expected_sum', [(5, 2.5, 98.17)])
    def test_two_circle_areas_sum(self, radius_1, radius_2, expected_sum):
        circle_1 = Circle(radius_1)
        circle_2 = Circle(radius_2)
        assert circle_1.add_area(circle_2) == expected_sum, f'Expected sum is {expected_sum}'


class TestNegative:
    @pytest.mark.parametrize('radius', [0, -1], ids=['radius is zero', 'radius is negative'])
    def test_circle_create_error(self, radius):
        with pytest.raises(ValueError):
            Circle(radius)

    @pytest.mark.parametrize('some_other_class', [10, 5.2, 'something'], ids=['integer', 'float', 'str'])
    def test_two_circle_areas_sum_error(self, some_other_class):
        circle_1 = Circle(4)
        with pytest.raises(ValueError):
            circle_1.add_area(some_other_class)
