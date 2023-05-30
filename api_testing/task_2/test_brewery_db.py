import pytest
import requests

BASE_URL = 'https://api.openbrewerydb.org/v1/breweries/'


class TestPositive:

    @pytest.mark.smoke
    @pytest.mark.parametrize('params, number',
                             [('', 50), ('per_page=1', 1), ('per_page=5', 5), ('per_page=0', 0)],
                             ids=['full list = 50', '1 per page', '5 per page', 'zero'])
    def test_get_list_breweries(self, params: str, number: int) -> None:
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
    def test_get_list_breweries_by_city(self, params: str, number: int) -> None:
        """
        Запрос на получение списка пивоваренных заводов с выборкой по городам и опционально с выбором количества
        запрашиваемого количества заводов.
        В параметре указывается город и опционально количество отображаемых заводов.
        """
        response = requests.get(BASE_URL, params=params).json()
        assert len(response) == number

    @pytest.mark.smoke
    @pytest.mark.parametrize('id_num, number', [('b54b16e1-ac3b-4bff-a11f-f7ae9ddc27e0', 16)], ids=['some brewery'])
    def test_get_single_brewery(self, id_num: str, number: int) -> None:
        """
        Запрос на получение информации о пивоваренном заводе по его id.
        Ответ содержит 16 значений.
        """
        response = requests.get(BASE_URL + id_num).json()
        assert len(response) == number
        assert response['id'] == id_num

    @pytest.mark.smoke
    @pytest.mark.parametrize('params, number', [('size=3', 3), ('size=10', 10), ('', 1), ('size=50', 50)],
                             ids=['3 breweries', '10 breweries', '1 brewery - query without params', '50 is max'])
    def test_get_random_brewery_with_size(self, params: str, number: int) -> None:
        """
        Запрос на получение информации о случайных пивоваренных заводах.
        В параметре указывается опционально количество отображаемых заводов.
        """
        response = requests.get(BASE_URL + 'random', params=params).json()
        assert len(response) == number


class TestNegative:

    @pytest.mark.skip(reason='dont fix bug')
    @pytest.mark.regress
    @pytest.mark.parametrize('params', ['-1', 'one', '!@##%#^%^@(*%&%@#_!'],
                             ids=['negative number', 'string', 'some symbols'])
    def test_error_get_list_brewery(self, params):
        """
        Отображение ошибки при невалидном значении параметра во время запроса списка всех
        пивоваренных заводов.
        """
        response = requests.get(BASE_URL, params=params).json()
        assert 'Couldn\'t find Brewery' in response['message']
