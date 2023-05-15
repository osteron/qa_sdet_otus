import pytest
from src.square import Square


@pytest.mark.parametrize('side_a, expected_area, expected_perimeter',
                         [
                             (5, 25, 20),
                             (2.3, 5.29, 9.2)
                         ]
                         )
def test_square_creation_positive(side_a, expected_area, expected_perimeter):
    square = Square(side_a)
    assert square.name == 'Square', 'Expected name is "Square"'
    assert square.perimeter == expected_perimeter, 'Expected correct perimeter'
    assert square.area == expected_area, 'Expected correct area'


@pytest.mark.parametrize('side_a', [0, -1], ids=['side is zero', 'side is negative'])
def test_square_creation_negative(side_a):
    with pytest.raises(ValueError):
        Square(side_a)


def test_two_square_areas_sum():
    square_1 = Square(5)
    square_2 = Square(1.5)
    expected_sum = 27.25
    assert square_1.add_area(square_2) == expected_sum, f'Expected sum is {expected_sum}'


@pytest.mark.parametrize('some_other_class', [5, 2.5, 'something'], ids=['integer', 'float', 'str'])
def test_two_square_areas_sum_negative(some_other_class):
    square_1 = Square(5)
    with pytest.raises(ValueError):
        square_1.add_area(some_other_class)
