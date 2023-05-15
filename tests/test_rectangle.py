import pytest
from src.rectangle import Rectangle


@pytest.mark.parametrize('side_a, side_b, expected_area, expected_perimeter',
                         [
                             (2, 5, 10, 14),
                             (1.5, 3.4, 5.1, 9.8)
                         ]
                         )
def test_rectangle_create_positive(side_a, side_b, expected_area, expected_perimeter):
    rectangle = Rectangle(side_a, side_b)
    assert rectangle.name == "Rectangle", 'Expected name is "Rectangle"'
    assert rectangle.perimeter == expected_perimeter, 'Expected correct perimeter'
    assert rectangle.area == expected_area, 'Expected correct area'


@pytest.mark.parametrize('side_a, side_b', [(0, 2), (3, -1)], ids=['side is zero', 'side is negative'])
def test_rectangle_create_negative(side_a, side_b):
    with pytest.raises(ValueError):
        Rectangle(side_a, side_b)


def test_two_rectangle_areas_sum():
    rectangle_1 = Rectangle(2, 4)
    rectangle_2 = Rectangle(3, 6)
    expected_sum = 26
    assert rectangle_1.add_area(rectangle_2) == expected_sum, f'Expected sum is {expected_sum}'


@pytest.mark.parametrize('some_other_class', [10, 2.3, 'something'], ids=['integer', 'float', 'str'])
def test_two_rectangle_ares_sum_negative(some_other_class):
    rectangle_1 = Rectangle(3, 4)
    with pytest.raises(ValueError):
        rectangle_1.add_area(some_other_class)
