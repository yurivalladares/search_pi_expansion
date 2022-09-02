import logging
from datetime import datetime

logging.basicConfig(
        encoding='utf-8',
        level=logging.INFO,
        format='%(asctime)s %(message)s',
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=[
        logging.FileHandler(datetime.now().strftime("./logs/search_log_%Y-%m-%d_%H-%M-%S.log")),
        logging.StreamHandler()
    ])