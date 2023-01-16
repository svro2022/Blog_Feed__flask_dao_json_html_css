import pytest
from app import app

'''Корректные ключи'''
keys_should_be = {
    "poster_name",
    "poster_avatar",
    "pic",
    "content",
    "views_count",
    "likes_count",
    "pk",
}

'''Проверка ответа пользователя - получаем список, проверяем по первому [0] значению'''
def test_api_all_posts():
    response = app.test_client().get('/api/posts/')
    assert response.status_code == 200
    api_response = response.json
    assert type(api_response) == list
    assert set(api_response[0].keys()) == keys_should_be
    print(response.status_code)
    print(type(api_response))
    print(api_response[0].keys())


'''Проверка ответа пользователя - получаем словарь, проверяем в нем наличие корректных ключей'''
def test_api_post():
    response = app.test_client().get('/api/posts/1')
    assert response.status_code == 200
    api_response = response.json
    assert type(api_response) == dict
    assert set(api_response.keys()) == keys_should_be
