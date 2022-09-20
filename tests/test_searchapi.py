import src.searchapi
from src.conditions import is_prime, is_palindrome
import requests_mock
import pytest

def test_get_pi_api(requests_mock):
    requests_mock.get(
        "https://api.pi.delivery/v1/pi?start=1&numberOfDigits=10", 
        text='{"content":"1415926535"}')
    data = src.searchapi.get_pi_api(start_position=1, api_data_length=10)
    assert data == '1415926535'

def test_get_pi_api_negative_start_exception():
    with pytest.raises(ValueError):
        src.searchapi.get_pi_api(-1, 1000)

def test_search_pi_api_exception_data_greater_digits(requests_mock):

    with pytest.raises(ValueError):
        src.searchapi.search_pi_api(
            start_position=1,
            digits=9,
            condition_list=[is_palindrome],
            api_data_length=8
            )

def test_search_pi_api_valid(requests_mock):
    requests_mock.get(
        "https://api.pi.delivery/v1/pi?start=1&numberOfDigits=30", 
        text='{"content":"141592653589793238462643383279"}')
    assert src.searchapi.search_pi_api(
        start_position=1, 
        digits=3,
        reverse=False,
        condition_list=[is_palindrome, is_prime],
        api_data_length=30
        ) == {'number': 383, 'position': 25}