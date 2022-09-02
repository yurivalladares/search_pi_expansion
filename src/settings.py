import logging
from datetime import datetime
import os

path = os.path.join("./", "logs")

if not os.path.isdir(path):
    os.mkdir(path)


logging.basicConfig(
    encoding="utf-8",
    level=logging.INFO,
    format="%(asctime)s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.FileHandler(
            datetime.now().strftime("./logs/search_log_%Y-%m-%d_%H-%M-%S.log")
        ),
        logging.StreamHandler(),
    ],
)
