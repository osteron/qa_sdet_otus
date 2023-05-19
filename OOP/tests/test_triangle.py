import pytest
from OOP.src.triangle import Triangle


class TestPositive:
    @pytest.mark.parametrize('side_a, side_b, side_c', [(5, 7, 4)])
    def test_triangle_creation(self, side_a, side_b, side_c):
        triangle = Triangle(side_a, side_b, side_c)
        assert triangle.name == 'Triangle', 'Expected name is "Triangle"'

    @pytest.mark.parametrize('side_a, side_b, side_c, expected_perimeter',
                             [
                                 (5, 7, 4, 16),
                                 (10, 10, 15, 35),
                                 (2, 4, 5, 11)
                             ]
                             )
    def test_triangle_perimeter_calculation(self, side_a, side_b, side_c, expected_perimeter):
        triangle = Triangle(side_a, side_b, side_c)
        assert triangle.perimeter == expected_perimeter, 'Expected correct perimeter'

    @pytest.mark.parametrize('side_a, side_b, side_c, expected_area',
                             [
                                 (5, 7, 4, 9.8),
                                 (10, 10, 15, 49.6),
                                 (2, 4, 5, 3.8)
                             ]
                             )
    def test_triangle_area_calculation(self, side_a, side_b, side_c, expected_area):
        triangle = Triangle(side_a, side_b, side_c)
        assert triangle.area == expected_area, 'Expected correct area'

    @pytest.mark.parametrize('side_a_1, side_b_1, side_c_1, side_a_2, side_b_2, side_c_2, expected_sum',
                             [(10, 6, 12, 5, 4, 6, 39.8)])
    def test_two_triangle_areas_sum(self, side_a_1, side_b_1, side_c_1, side_a_2, side_b_2, side_c_2, expected_sum):
        triangle_1 = Triangle(side_a_1, side_b_1, side_c_1)
        triangle_2 = Triangle(side_a_2, side_b_2, side_c_2)
        assert triangle_1.add_area(triangle_2) == expected_sum, f'Expected sum is {expected_sum}'


class TestNegative:
    @pytest.mark.parametrize('side_a, side_b, side_c',
                             [
                                 (0, 2, 3),
                                 (2, -1, 3),
                                 (15, 15, 50),
                             ],
                             ids=[
                                 'one side is zero',
                                 'one side is negative',
                                 'can not create triangle with these sides'
                             ]
                             )
    def test_triangle_create_error(self, side_a, side_b, side_c):
        with pytest.raises(ValueError):
            Triangle(side_a, side_b, side_c)

    @pytest.mark.parametrize('some_other_class', [10, 10.1, 'something'], ids=['integer', 'float', 'str'])
    def test_two_triangle_areas_sum_error(self, some_other_class):
        triangle_1 = Triangle(5, 5, 5)
        with pytest.raises(ValueError):
            triangle_1.add_area(some_other_class)
