import pytest
from src.circle import Circle


@pytest.mark.parametrize('radius, expected_area, expected_perimeter',
                         [
                             (10, 314.16, 62.83),
                             (6.3, 124.69, 39.58),
                             (30, 2827.43, 188.5)
                         ]
                         )
def test_circle_creation_positive(radius, expected_area, expected_perimeter):
    circle = Circle(radius)
    assert circle.name == 'Circle', 'Expected name is "Circle"'
    assert circle.perimeter == expected_perimeter, 'Expected correct perimeter'
    assert circle.area == expected_area, 'Expected correct area'


@pytest.mark.parametrize('radius', [0, -1], ids=['radius is zero', 'radius is negative'])
def test_circle_creation_negative(radius):
    with pytest.raises(ValueError):
        Circle(radius)


def test_two_circle_areas_sum():
    circle_1 = Circle(5)
    circle_2 = Circle(2.5)
    expected_sum = 98.17
    assert circle_1.add_area(circle_2) == expected_sum, f'Expected sum is {expected_sum}'


@pytest.mark.parametrize('some_other_class', [10, 5.2, 'something'], ids=['integer', 'float', 'str'])
def test_two_circle_areas_sum_negative(some_other_class):
    circle_1 = Circle(4)
    with pytest.raises(ValueError):
        circle_1.add_area(some_other_class)
