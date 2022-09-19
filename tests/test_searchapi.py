from unittest import mock
import src.searchapi
import requests_mock

def test_get_pi_api(requests_mock):
    requests_mock.get(
        "https://api.pi.delivery/v1/pi?start=1&numberOfDigits=10", 
        text='{"content":"1415926535"}')
    data = src.searchapi.get_pi_api(start_position=1, api_data_length=10)
    assert data == '1415926535'
