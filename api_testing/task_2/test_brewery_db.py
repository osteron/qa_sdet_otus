import pytest
import requests

BASE_URL = 'https://api.openbrewerydb.org/v1/breweries/'


class TestPositive:

    @pytest.mark.smoke
    @pytest.mark.parametrize('params, number',
                             [('', 50), ('per_page=1', 1), ('per_page=5', 5), ('per_page=0', 0)],
                             ids=['full list = 50', '1 per page', '5 per page', 'zero'])
    def test_get_list_breweries(self, params, number):
        """
        Запрос на получение списка пивоваренных заводов.
        В параметре указывается количество отображаемых заводов.
        """
        response = requests.get(BASE_URL, params=params).json()
        assert len(response) == number

    @pytest.mark.smoke
    @pytest.mark.parametrize('params, number', [
        ('by_city=san_diego', 50),
        ('by_city=norman', 3),
        ('by_city=austin&per_page=15', 15)
    ], ids=[
        'city is San Diego mentioned 50 times',
        'city is Norman mentioned 3 times',
        'city is Austin and per page is 15'
    ])
    def test_get_list_breweries_by_city(self, params, number):
        response = requests.get(BASE_URL, params=params).json()
        assert len(response) == number

    @pytest.mark.smoke
    @pytest.mark.parametrize('id, number', [('b54b16e1-ac3b-4bff-a11f-f7ae9ddc27e0', 16)], ids=['some brewery'])
    def test_get_single_brewery(self, id, number):
        response = requests.get(BASE_URL + id).json()
        assert len(response) == number
        assert response['id'] == id


