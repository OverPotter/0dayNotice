import time
import utils
from config import TIMEOUT


if __name__ == '__main__':
    while True:
        if utils.RegEdit().create_autorun():
            utils.ExploitParser().create_and_fill_database()
            utils.Notification().launch_notice()
        else:
            utils.Notification().call_notification(text="Registry create_autorun() error")
        time.sleep(TIMEOUT)
