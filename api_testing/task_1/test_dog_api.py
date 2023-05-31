import pytest
import requests

from .urls import Urls

ERROR_SUCCESS_STATUS = 'Статус должен быть success'
ERROR_STATUS_CODE_200 = 'Статус код должен быть 200'


def get_status_code(url: str):
    return requests.get(url).status_code


def json_return(url: str):
    return requests.get(url).json()


class TestPositive:

    @pytest.mark.smoke
    @pytest.mark.parametrize('extension, status', [('.jpg', 'success')], ids=['extension .jpg and status "success"'])
    def test_get_random_dog_image(self, extension, status):
        """
        Тест проверяет запрос на получение случайного изображения собаки.
        Шаги проверки:
        1. Проверка статус кода 200
        2. Проверка наличия расширения файла в ответе.
        3. Проверка статуса в ответе.
        """
        url = Urls.RANDOM_IMAGE_URL
        assert get_status_code(url) == 200, ERROR_STATUS_CODE_200
        json_response = json_return(url)
        assert extension in json_response['message'], f'Расширение файла должно быть {extension}'
        assert status in json_response['status'], ERROR_SUCCESS_STATUS

    @pytest.mark.smoke
    @pytest.mark.parametrize('number, status', [
        ('1', 'success'),
        ('25', 'success'),
        ('49', 'success'),
        ('50', 'success')
    ], ids=[
        'one image',
        'middle of the range',
        'end of range minus one',
        'end of range'
    ])
    def test_get_multiply_random_image(self, number, status):
        """
        Тест проверяет запрос на получение нескольких случайных фотографий собак.
        Граничные значения для запроса от 1 до 50 (включительно).
        Шаги проверки:
        1. Проверка статус кода 200.
        2. Проверка количества возвращаемых фотографий собак.
        3. Проверка статуса в ответе.
        """
        url = f'{Urls.RANDOM_IMAGE_URL}{number}'
        assert get_status_code(url) == 200, ERROR_STATUS_CODE_200
        json_response = json_return(url)
        assert len(json_response['message']) == int(number), f'Возвращаемое количество должно быть равно {number}'
        assert status in json_response['status'], ERROR_SUCCESS_STATUS

    @pytest.mark.smoke
    @pytest.mark.parametrize('number, status', [(808, 'success')], ids=['count of images'])
    def test_get_images_by_breed(self, number, status):
        """
        Тест проверяет запрос на получение всех фотографий собак породы hound.
        Шаги проверки:
        1. Проверка статус кода 200.
        2. Проверка количества возвращаемых фотографий собак.
        3. Проверка статуса в ответе.
        """
        url = Urls.BY_BREED_URL
        assert get_status_code(url) == 200, ERROR_STATUS_CODE_200
        json_response = json_return(url)
        assert len(json_response['message']) == number, f'Возвращаемое количество должно быть равно {number}'
        assert status in json_response['status'], ERROR_SUCCESS_STATUS

    @pytest.mark.smoke
    @pytest.mark.parametrize('number, status', [(98, 'success')], ids=['count of breeds'])
    def test_get_list_all_breeds(self, number, status):
        """
        Тест проверяет запрос на получение списка всех пород собак.
        Шаги проверки:
        1. Проверка статус кода 200.
        2. Проверка количества возвращаемых фотографий собак.
        3. Проверка статуса в ответе.
        """
        url = Urls.LIST_ALL_BREEDS_URL
        assert get_status_code(url) == 200, ERROR_STATUS_CODE_200
        json_response = json_return(url)
        assert len(json_response['message']) == number, f'Возвращаемое количество должно быть равно {number}'
        assert status in json_response['status'], ERROR_SUCCESS_STATUS

    @pytest.mark.smoke
    @pytest.mark.parametrize('extension, status', [('.jpg', 'success')], ids=['extension .jpg and status "success"'])
    def test_get_random_image_from_breed_collection(self, extension, status):
        """
        Тест проверяет запрос на получение случайной фотографии собаки породы hound
        Шаги проверки:
        1. Проверка статус кода 200.
        2. Проверка наличия расширения файла в ответе.
        3. Проверка статуса в ответе.
        """
        url = Urls.RANDOM_IMAGE_FROM_BREED_URL
        assert get_status_code(url) == 200, ERROR_STATUS_CODE_200
        json_response = json_return(url)
        assert extension in json_response['message'], f'Расширение файла должно быть {extension}'
        assert status in json_response['status'], ERROR_SUCCESS_STATUS

    @pytest.mark.smoke
    @pytest.mark.parametrize('number, status', [(1, 'success'), (2, 'success'), (3, 'success')],
                             ids=['one image', 'two images', 'three images'])
    def test_get_multiple_images_from_breed_collection(self, number, status):
        """
        Тест проверяет запрос на получение нескольких фотографий собак с породой hound.
        Шаги проверки:
        1. Проверка статус кода 200.
        2. Проверка количества возвращаемых фотографий собак.
        3. Проверка наличия статуса в ответе.
        """
        url = f'{Urls.MULTIPLE_IMAGES_FROM_BREED_URL}{number}'
        assert get_status_code(url) == 200, ERROR_STATUS_CODE_200
        json_response = json_return(url)
        assert len(json_response['message']) == number, f'Возвращаемое количество должно быть равно {number}'
        assert status in json_response['status'], ERROR_SUCCESS_STATUS
