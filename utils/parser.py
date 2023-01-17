import requests
from bs4 import BeautifulSoup
from config import URL
from utils.handler import DataHandler
from utils.notice import Notification


class ExploitParser(DataHandler):
    def __init__(self):
        super().__init__()
        self.__session = requests.session()
        self.__counter: int = 0
        self._page_content = None

    def __get_tables(self) -> None:
        self.__session.post(URL, data={"agree": "Yes%2C+I+agree"})
        self.__session.get(f"{URL}/back")
        page_response = self.__session.get(URL)
        if page_response.status_code == 200:
            self._page_content = BeautifulSoup(page_response.content, "html.parser")
        else:
            self.__counter += 1
            if self.__counter > 5:
                Notification().call_notification(text="Network TimeOut error")
                raise Exception('Network TimeOut error')
            self.__get_tables()

    def create_and_fill_database(self) -> None:
        self.__get_tables()
        self.formatting_tables(self._page_content)
