import pytest


@pytest.fixture(scope='session')
def base_url():
    return 'https://dog.ceo/api/'


@pytest.fixture(scope='function')
def random_image_url():
    return 'breeds/image/random/'


@pytest.fixture(scope='function')
def by_breed_url():
    return 'breed/hound/images'


@pytest.fixture(scope='function')
def list_all_breeds():
    return 'breeds/list/all'
