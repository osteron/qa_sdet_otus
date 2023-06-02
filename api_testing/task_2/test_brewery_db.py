import pytest
import requests
from .urls import Url
from .models import GetResponseBreweryModel, GetResponseListBreweryModel, GetResponseListAutocompleteModel
from ..api_functions import validate_json, check_status_code


class TestBreweryApi:

    @pytest.mark.smoke
    @pytest.mark.parametrize('params, count_brewery', [
        ('', 50),
        ('per_page=1', 1),
        ('per_page=5', 5),
        ('per_page=0', 0)
    ])
    def test_get_list_breweries(self, params: str, count_brewery: int) -> None:
        response = requests.get(Url.BASE_URL, params=params)
        check_status_code(response, 200)
        response_json = response.json()
        brewery_list = GetResponseListBreweryModel(__root__=response_json)
        assert len(brewery_list.__root__) == count_brewery

    @pytest.mark.smoke
    @pytest.mark.parametrize('params, count_brewery', [
        ('by_city=san_diego&per_page=50', 50),
        ('by_city=norman&per_page=3', 3),
        ('by_city=austin&per_page=15', 15)
    ])
    def test_get_list_breweries_by_city(self, params: str, count_brewery: int) -> None:
        response = requests.get(Url.BASE_URL, params=params)
        check_status_code(response, 200)
        response_json = validate_json(response)
        brewery_list = GetResponseListBreweryModel(__root__=response_json)
        assert len(brewery_list.__root__) == count_brewery

    @pytest.mark.smoke
    @pytest.mark.parametrize('id_brewery', ['b54b16e1-ac3b-4bff-a11f-f7ae9ddc27e0'])
    def test_get_single_brewery(self, id_brewery: str) -> None:
        response = requests.get(f'{Url.BASE_URL}{id_brewery}')
        check_status_code(response, 200)
        response_json = validate_json(response)
        GetResponseBreweryModel(**response_json)

    @pytest.mark.smoke
    @pytest.mark.parametrize('params, count_brewery', [('size=3', 3), ('size=10', 10), ('', 1), ('size=50', 50)])
    def test_get_random_brewery_with_size(self, params: str, count_brewery: int) -> None:
        response = requests.get(f'{Url.RANDOM_BREWERY_URL}', params=params)
        check_status_code(response, 200)
        response_json = validate_json(response)
        brewery_list = GetResponseListBreweryModel(__root__=response_json)
        assert len(brewery_list.__root__) == count_brewery

    @pytest.mark.smoke
    @pytest.mark.parametrize('params, count_brewery', [('query=dog', 39), ('query=diego', 91)])
    def test_get_autocomplete_with_query(self, params: str, count_brewery: int) -> None:
        response = requests.get(Url.AUTOCOMPLETE_URL, params=params)
        check_status_code(response, 200)
        response_json = validate_json(response)
        query_list = GetResponseListAutocompleteModel(__root__=response_json)
        assert (len(query_list.__root__)) == count_brewery