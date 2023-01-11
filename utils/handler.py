import re
import bs4
from config import URL
from db import DataBaseClient


class DataHandler(DataBaseClient):
    def __init__(self):
        super().__init__()
        self.__exploit_dict: dict = {}

    def formatting_tables(self, page_content: bs4.BeautifulSoup) -> None:
        exploit_tables_html = page_content.find_all(class_='ExploitTableContent')
        for table in exploit_tables_html:
            self.__parse_and_formatting_date(table)
            self.__parse_and_formatting_description(table)
            self.__parse_and_formatting_platform(table)
            self.__parse_and_formatting_risk(table)
            self.__parse_and_formatting_price(table)
            self.append_exploit(**self.__exploit_dict)

    def __parse_and_formatting_date(self, table: bs4.element.Tag) -> None:
        exploit_date = re.findall(r'\d\d-\d\d-\d\d\d\d', str(table))
        if exploit_date:
            self.__exploit_dict.update(date=exploit_date[-1])
        else:
            self.__exploit_dict.update(date="Date not found")

    def __parse_and_formatting_description(self, table: bs4.element.Tag) -> None:
        exploit_description = table.find("h3")
        if exploit_description:
            description = re.findall(r'/exploit/description.* </a>', str(exploit_description))[0]
            description = description[:-5].split('>')[-1]
            link = re.findall(r'href=".*">', str(exploit_description))[0].split('"')[1]
            link = f"{URL}{link}"
            self.__exploit_dict.update(description=description, description_link=link)
        else:
            self.__exploit_dict.update(description="Description not found",
                                       description_link="Description link not found")

    def __parse_and_formatting_platform(self, table: bs4.element.Tag) -> None:
        exploit_platform = re.findall(r'platforms.*</a>', str(table))
        if not exploit_platform:
            exploit_platform = re.findall(r'shellcode.*</a>', str(table))
            if not exploit_platform:
                self.__exploit_dict.update(platform="Platform not found")
        exploit_platform = exploit_platform[0][:-4].split('>')[-1]
        self.__exploit_dict.update(platform=exploit_platform)

    def __parse_and_formatting_risk(self, table: bs4.element.Tag) -> None:
        exploit_risk = re.findall(r'Security Risk .*<', str(table))[0][:-1]
        if exploit_risk:
            self.__exploit_dict.update(risk=exploit_risk)
        else:
            self.__exploit_dict.update(risk="Risk not found")

    def __parse_and_formatting_price(self, table: bs4.element.Tag) -> None:
        exploit_btc = table.find(class_="tips_price_btc")
        if exploit_btc:
            exploit_btc = re.findall(r'\d.*BTC', str(exploit_btc))[0]
            if "</span>" in exploit_btc:
                exploit_btc = exploit_btc.split("</span>")[-1]
            self.__exploit_dict.update(price=exploit_btc)
        else:
            self.__exploit_dict.update(price="Free")
