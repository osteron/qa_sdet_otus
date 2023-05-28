import pytest
import requests

ERROR_SUCCESS_STATUS = 'Статус должен быть success'


class TestPositive:

    @pytest.mark.smoke
    @pytest.mark.parametrize('extension, status', [('.jpg', 'success')], ids=['extension of photo'])
    def test_get_random_dog_image(self, base_url, random_image_url, extension, status):
        """
        Ответ должен содержать:
        'message': 'путь до фотографии с расширением .jpg'
        'status': 'success'
        """
        response = requests.get(base_url + random_image_url).json()
        assert extension in response['message'], 'В ответе должно присутствовать расширение .jpg'
        assert response['status'] == status, ERROR_SUCCESS_STATUS

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
    def test_get_multiply_random_image(self, base_url, random_image_url, number, status):
        """
        Граничные значения для запроса от 1 до 50 (включительно).
        Ответ должен содержать:
        'message': ['путь до фотографии с расширением .jpg'] - список из N фотографий
        'status': 'success'
        """
        response = requests.get(base_url + random_image_url + number).json()
        assert len(response['message']) == int(number), f'Возвращаемое количество должно быть равно {number}'
        assert response['status'] == status, ERROR_SUCCESS_STATUS

    @pytest.mark.smoke
    @pytest.mark.parametrize('number, status', [808, 'success'], ids=['count of images'])
    def test_get_images_by_breed(self, base_url, by_breed_url, number, status):
        """
        Запрос на получение всех фотографий.
        Ответ должен содержать:
        'message': ['путь до фотографии с расширением .jpg'] - список из 808 фотографий
        """
        response = requests.get(base_url + by_breed_url).json()
        assert len(response['message']) == number, f'Возвращаемое количество должно быть равно {number}'
        assert response['status'] == status, ERROR_SUCCESS_STATUS

    @pytest.mark.smoke
    @pytest.mark.parametrize('number, status', [(98, 'success')], ids=['count of breeds'])
    def test_get_list_all_breeds(self, base_url, list_all_breeds, number, status):
        """
        Запрос на получение списка всех пород собак.
        Ответ должен содержать:
        'message': {'порода':[]} - количество 98.
        'status': 'success'
        """
        response = requests.get(base_url + list_all_breeds).json()
        assert len(response['message']) == number, f'Возвращаемое количество должно быть равно {number}'
        assert response['status'] == status, ERROR_SUCCESS_STATUS

    # @pytest.mark.smoke
    # @pytest.mark.parametrize()
    # def test_list_all_sub_breeds(self):
    #     pass


class TestNegative:

    @pytest.mark.skip(reason='not fix problem with out of range')
    @pytest.mark.regress
    @pytest.mark.parametrize('number', ['-1', '0', '51'], ids=['negative number', 'zero', 'out of range'])
    def test_multiply_image_out_of_range(self, base_url, random_image_url, number):
        """
        Нарушение граничных значений запроса.
        Ответ не должен содержать:
        'status': 'success'
        """
        response = requests.get(base_url + random_image_url + number).json()
        assert response['status'] != 'success', 'Статус не должен быть success'
