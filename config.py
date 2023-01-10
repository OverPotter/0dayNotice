import os

# todo last week
DATE = "01-12-2022"

URL = "https://0day.today"

DB_NAME = os.path.join("db", "exploits.db")
BASE_DIR = os.path.dirname(os.path.realpath(__file__))
DB_PATH = os.path.join(BASE_DIR, DB_NAME)
