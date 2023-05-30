import pytest
import requests
from pydantic import BaseModel, Field

POST_CREATING_RESOURCE = {
        'title': 'foo',
        'body': 'bar',
        'userId': 1,
}


class Resource(BaseModel):
    user_id: int = Field(alias='userId')
    id: int
    title: str
    body: str


class TestPositive:

    @pytest.mark.smoke
    @pytest.mark.parametrize('number', [1, 5, 10], ids=['id=1', 'id=5', 'id=10'])
    def test_get_resource(self, number: int) -> None:
        resource = Resource.parse_obj(requests.get(f'https://jsonplaceholder.typicode.com/posts/{number}').json())
        assert resource.id == number

    @pytest.mark.smoke
    def test_get_all_resources(self) -> None:
        data = requests.get('https://jsonplaceholder.typicode.com/posts').json()
        result = [Resource.parse_obj(item) for item in data]
        assert len(result) == len(data)

    @pytest.mark.smoke
    @pytest.mark.parametrize('data', [POST_CREATING_RESOURCE])
    def test_creating_course(self, data: object) -> None:
        resource = Resource.parse_obj(requests.post('https://jsonplaceholder.typicode.com/posts', json=data).json())
        assert resource.id == 101
