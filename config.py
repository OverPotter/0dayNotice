import datetime
import os


TIMEOUT = 7200

LAST_WEEK_DATE = datetime.datetime.now() - datetime.timedelta(weeks=1)

URL = "https://0day.today"

DB_NAME = os.path.join("db", "exploits.db")
BASE_DIR = os.path.dirname(os.path.realpath(__file__))
DB_PATH = os.path.join(BASE_DIR, DB_NAME)

PROJ_TEMP_DIR = os.path.join(BASE_DIR, "temp")

PYTHON_VENV_PATH = os.path.join("venv", "Scripts", "python.exe")

MAIN_FILE_NAME = "main.py"
AUTORUN_NAME = "ExploitsNotice"
BAT_FILENAME = "project_launcher.bat"
RUN_FILENAME = "bat_launcher.vbs"
