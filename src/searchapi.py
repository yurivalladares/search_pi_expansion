import requests
from requests.adapters import HTTPAdapter, Retry
import logging
from src.conditions import *


def get_pi_api(start_position: int, api_data_length: int) -> str:

    session = requests.Session()
    retry = Retry(connect=10, backoff_factor=1)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount("http://", adapter)
    session.mount("https://", adapter)

    url = f"https://api.pi.delivery/v1/pi?start={start_position}&numberOfDigits={api_data_length}"

    response = session.get(url)
    data = response.json()["content"]
    return data


def search_pi_api(
    start_position: int,
    digits: int,
    condition_list: list,
    reverse=False,
    api_data_length=1000,
) -> dict[str, int]:
    if api_data_length < digits:
        raise ValueError("digits must be smaller than api_data_length")

    logging.info(f"Digits: {digits}")
    logging.info(f"Reverse search: {reverse}")
    logging.info(f"Conditions: {[i.__name__ for i in condition_list]}")
    logging.info("Search started")
    result = {}
    verifier = True
    position = start_position
    while verifier:
        logging.info(f"Looking at position... {position}")
        data = get_pi_api(position, api_data_length)
        for i in range(0, len(data) - digits):

            if data[i] == "0":
                continue

            number = int(data[i : i + digits])

            if all(condition_wraper(condition_list, number)):

                result = {"number": number, "position": position + i}
                logging.info("###### FOUND ######")
                logging.info(result)
                verifier = False
                break
        else:
            if not reverse:
                position += i
            else:
                if position == 1:
                    verifier = False
                elif (position - i) > 1:
                    position -= i
                else:
                    position = 1
    if not result:
        logging.info("###### NOT FOUND ######")
    return result
