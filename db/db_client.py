import sqlite3
from config import DB_PATH


class DataBaseClient:
    def __init__(self):
        self.conn = sqlite3.connect(DB_PATH)
        self.cursor = self.conn.cursor()

    def __create_table(self) -> None:
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS ExploitsTable (
        id INTEGER NOT NULL UNIQUE PRIMARY KEY AUTOINCREMENT,
        release_date VARCHAR(10) NOT NULL,
        description TEXT NOT NULL UNIQUE,
        description_link VARCHAR NOT NULL,
        platform VARCHAR(25) NOT NULL,
        risk VARCHAR(25) NOT NULL,
        price VARCHAR(15) NOT NULL
        );
        """)

    def get_release_date(self) -> list:
        result = self.cursor.execute("""
        SELECT `id`, `release_date` from ExploitsTable
        """)
        return result.fetchall()

    def get_exploit_info(self, exploit_id: str, date: str) -> list:
        result = self.cursor.execute("""
        SELECT * from ExploitsTable WHERE `id` = (?) AND `release_date` = (?)
                """, (exploit_id, date,))
        return result.fetchall()

    def append_exploit(
            self, date: str, description: str, description_link: str, platform: str, risk: str, price: str
    ) -> None:
        self.__create_table()
        self.cursor.execute("""
        INSERT OR IGNORE INTO ExploitsTable
        (`release_date`, `description`, `description_link`, `platform`, `risk`, `price`)
        VALUES((?), (?), (?), (?), (?), (?));
        """, (date, description, description_link, platform, risk, price,))
        return self.conn.commit()
