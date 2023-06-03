import pytest
import requests
from .urls import Url
from .models import GetResponseDogModel, GetResponseListDogModel, GetResponseListBreedsModel
from ..api_functions import validate_json, check_status_code


class TestDogsApi:

    @pytest.mark.smoke
    def test_get_random_dog_image(self):
        """
        Тест проверяет запрос на получение случайного изображения собаки.
        Шаги проверки:
        1. GET запрос на получение объекта с изображением собаки
        2. Проверка статус кода 200
        3. Валидность json
        4. Валидность контента json с определенной моделью
        """
        response = requests.get(Url.RANDOM_IMAGE_URL)
        check_status_code(response, 200)
        response_json = validate_json(response)
        GetResponseDogModel(**response_json)

    @pytest.mark.smoke
    @pytest.mark.parametrize('count_image', [1, 25, 49, 50])
    def test_get_multiply_random_image(self, count_image: int):
        """
        Тест проверяет запрос на получение нескольких случайных фотографий собак.
        Граничные значения для запроса от 1 до 50 (включительно).
        Шаги проверки:
        1. GET запрос на получение объекта со случайным изображением собаки
        2. Проверка статус кода 200
        3. Валидность json
        4. Валидность контента json с определенной моделью
        5. Количество возвращаемых объектов
        """
        response = requests.get(f'{Url.RANDOM_IMAGE_URL}{count_image}')
        check_status_code(response, 200)
        response_json = validate_json(response)
        dog_list = GetResponseListDogModel(**response_json)
        assert len(dog_list.message) == count_image

    @pytest.mark.smoke
    def test_get_images_by_breed(self):
        """
        Тест проверяет запрос на получение всех фотографий собак породы hound.
        Шаги проверки:
        1. GET запрос на получение всех фотографий собак породы hound
        2. Проверка статус кода 200
        3. Валидность json
        4. Валидность контента json с определенной моделью
        5. Количество возвращаемых объектов
        """
        response = requests.get(Url.BY_BREED_URL)
        check_status_code(response, 200)
        response_json = validate_json(response)
        dog_list = GetResponseListDogModel(**response_json)
        assert len(dog_list.message) == 808

    @pytest.mark.smoke
    def test_get_list_all_breeds(self):
        """
        Тест проверяет запрос на получение списка всех пород собак.
        Шаги проверки:
        1. GET запрос на получение списка всех пород собак
        2. Проверка статус кода 200
        3. Валидность json
        4. Валидность контента json с определенной моделью
        5. Количество возвращаемых объектов
        """
        response = requests.get(Url.LIST_ALL_BREEDS_URL)
        check_status_code(response, 200)
        response_json = validate_json(response)
        dog_list = GetResponseListBreedsModel(**response_json)
        assert len(list(dog_list.message)) == 98

    @pytest.mark.smoke
    def test_get_random_image_from_breed_collection(self):
        """
        Тест проверяет запрос на получение случайной фотографии собаки породы hound
        Шаги проверки:
        1. GET запрос на получение случайной фотографии собаки породы hound
        2. Проверка статус кода 200
        3. Валидность json
        4. Валидность контента json с определенной моделью
        """
        response = requests.get(Url.RANDOM_IMAGE_FROM_BREED_URL)
        check_status_code(response, 200)
        response_json = validate_json(response)
        GetResponseDogModel(**response_json)

    @pytest.mark.smoke
    @pytest.mark.parametrize('count_image', [1, 2, 3],)
    def test_get_multiple_images_from_breed_collection(self, count_image):
        """
        Тест проверяет запрос на получение нескольких фотографий собак с породой hound.
        Шаги проверки:
        1. GET запрос на получение нескольких фотографий собак с породой hound
        2. Проверка статус кода 200
        3. Валидность json
        4. Валидность контента json с определенной моделью
        5. Количество возвращаемых объектов
        """
        response = requests.get(f'{Url.MULTIPLE_IMAGES_FROM_BREED_URL}{count_image}')
        check_status_code(response, 200)
        response_json = validate_json(response)
        dog_list = GetResponseListDogModel(**response_json)
        assert len(dog_list.message) == count_image
