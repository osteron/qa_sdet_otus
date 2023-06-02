import json
import requests


def check_status_code(response: requests, status_code: int) -> None:
    assert response.status_code == 200, f'Статус код должен быть {status_code}'


def validate_json(response: requests) -> json:
    try:
        response_json = json.loads(response.content)
        return response_json
    except ValueError as e:
        print("JSON невалидный. Ошибка: ", e)
