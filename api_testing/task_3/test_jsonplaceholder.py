import pytest
import requests
from pydantic import BaseModel, Field
from typing import List
from .urls import Urls
from ..api_functions import validate_json, check_status_code

POST_CREATING_RESOURCE = {
    'title': 'foo',
    'body': 'bar',
    'userId': 1,
}

PUT_UPDATING_RESOURCE = {
    'id': 1,
    'title': 'some_title',
    'body': 'some_body',
    'userId': 1,
}


class GetResponseResourceModel(BaseModel):
    user_id: int = Field(alias='userId')
    id: int
    title: str
    body: str


class ResourceList(BaseModel):
    __root__: List[GetResponseResourceModel]


class TestPositive:

    @pytest.mark.smoke
    @pytest.mark.parametrize('resourse_id', [1, 5, 10])
    def test_get_resource(self, resourse_id: int) -> None:
        response = requests.get(f'{Urls.BASE_URL}{resourse_id}')
        check_status_code(response, 200)
        response_json = validate_json(response)
        resource = GetResponseResourceModel(**response_json)
        assert resource.id == resourse_id

    @pytest.mark.smoke
    def test_get_all_resources(self) -> None:
        response = requests.get(Urls.BASE_URL)
        check_status_code(response, 200)
        response_json = validate_json(response)
        all_resources = ResourceList(__root__=response_json)
        assert len(all_resources.__root__) == 100

    @pytest.mark.smoke
    @pytest.mark.parametrize('post_data', [POST_CREATING_RESOURCE])
    def test_post_creating_resourse(self, post_data: dict) -> None:
        response = requests.post(Urls.BASE_URL, json=post_data)
        check_status_code(response, 201)
        response_json = validate_json(response)
        resource = GetResponseResourceModel(**response_json)
        assert resource.id == 101

    @pytest.mark.smoke
    @pytest.mark.parametrize('put_data, resource_id', [(PUT_UPDATING_RESOURCE, 1)])
    def test_put_updating_resource(self, put_data: dict, resource_id: int) -> None:
        response = requests.put(f'{Urls.BASE_URL}{resource_id}', json=put_data)
        check_status_code(response, 200)
        response_json = validate_json(response)
        assert response_json == PUT_UPDATING_RESOURCE

    @pytest.mark.smoke
    @pytest.mark.parametrize('patch_data, resource_title, resource_id',
                             [
                                 ({'title': 'qwerty'}, 'qwerty', 1),
                                 ({'title': '!@#%$^'}, '!@#%$^', 2)],
                             ids=['string title', 'symbolic title'])
    def test_patch_update_resource(self, patch_data: dict, resource_title: str, resource_id: int) -> None:
        response = requests.patch(f'{Urls.BASE_URL}{resource_id}', json=patch_data)
        check_status_code(response, 200)
        response_json = validate_json(response)
        resource = GetResponseResourceModel(**response_json)
        assert resource.title in resource_title
        assert resource.id == resource_id
