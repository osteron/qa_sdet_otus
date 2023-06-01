import pytest
import requests


@pytest.mark.smoke
def test_get_valid_status_code(base_url: str, status_code: str) -> None:
    response = requests.get(url=base_url)
    assert str(response.status_code) == status_code, f'The status code is expected {status_code}'
