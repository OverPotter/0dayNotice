import sqlite3
from config import DB_PATH


# todo annotations
class DataBaseClient:
    # todo repeat class methods
    def __init__(self):
        self.conn = sqlite3.connect(DB_PATH)
        self.cursor = self.conn.cursor()

    def create_table(self) -> None:
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS exploits_table (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        release_date VARCHAR(10),
        description VARCHAR,
        description_link VARCHAR,
        platform VARCHAR(25),
        risk VARCHAR(25),
        price VARCHAR(15)
        );
        """)

    # def _get_courses(self, bank_name: str) -> tuple:
    #     result = self.cursor.execute(
    #         "SELECT `buyUSD`, `saleUSD`, `buyEUR`, `saleEUR`, `buyRUB`, `saleRUB`"
    #         "FROM `MoneyCourse`"
    #         "WHERE `Bank` = (?)",
    #         (bank_name,))
    #     return result.fetchall()[0]

    def append_exploit(
            self, date: str, description: str, description_link: str, platform: str, risk: str, price: str
    ) -> None:
        # print(date, description, description_link, platform, risk, price)
        self.cursor.execute("""
        INSERT INTO exploits_table
        (`release_date`, `description`, `description_link`, `platform`, `risk`, `price`)
        VALUES((?), (?), (?), (?), (?), (?)
        );
        """, (date, description, description_link, platform, risk, price,))
        return self.conn.commit()
