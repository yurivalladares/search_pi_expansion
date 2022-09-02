import requests
from requests.adapters import HTTPAdapter, Retry
import logging
from src.conditions import *

def get_pi_api(start: int, lenght: int) -> str:

    session = requests.Session()
    retry = Retry(connect=10, backoff_factor=1)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)

    url = f"https://api.pi.delivery/v1/pi?start={start}&numberOfDigits={lenght}"

    response = session.get(url)
    data = response.json()['content']
    return data

def search_pi_api(start: int, digits: int, condition_list: list) -> dict[str, int]:
    
    logging.info(f'Digits: {digits}')
    logging.info(f'Conditions: {[condition.__name__ for condition in condition_list]}')

    logging.info('Search started')

    verifier = True
    start = start
    while verifier:
        logging.info(f'Looking at position... {start}')
        data = get_pi_api(start, 1000)
        for i in range(0, len(data) - digits):

            if data[i] == '0':
                continue

            number = int(data[i: i + digits])

            if all(condition_wraper(condition_list, number)):
                
                result = {
                    'number': number,
                    'position': start+i
                }
                logging.info('###### FOUND ######')
                logging.info(result)
                verifier = False
                break
        else:
            start += i

    return result