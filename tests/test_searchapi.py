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

def test_search_pi_api_exception_data_greater_digits(requests_mock):
    requests_mock.get(
        "https://api.pi.delivery/v1/pi?start=1&numberOfDigits=10", 
        text='{"content":"1415926535"}')

    with pytest.raises(ValueError):
        src.searchapi.search_pi_api(
            start_position=-1,
            digits=9,
            condition_list=[is_palindrome],
            api_data_length=10
            )