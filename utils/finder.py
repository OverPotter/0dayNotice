import datetime
from db import DataBaseClient
from config import LAST_WEEK_DATE


class Finder(DataBaseClient):
    def __init__(self):
        super().__init__()
        self.__selection_data: list = []
        self.selection_exploits: list = []

    def __exploit_selection(self) -> None:
        release_date_list = self.get_release_date()
        for exploit_id, date in release_date_list:
            if LAST_WEEK_DATE < datetime.datetime.strptime(date, "%d-%m-%Y"):
                self.__selection_data.append((exploit_id, date))

    def receive_exploit(self) -> None:
        self.__exploit_selection()
        for exploit_id, date in self.__selection_data:
            exploit = self.get_exploit_info(exploit_id=exploit_id, date=date)
            self.selection_exploits.append(exploit[0])
