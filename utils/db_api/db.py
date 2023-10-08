import sqlite3


class BotDB:
    def __init__(self, db_file_name) -> None:
        self.db_file_name = db_file_name
    
    def open(self):
        self.conn = sqlite3.connect(self.db_file_name)
        self.cursor = self.conn.cursor()

    def close(self):
        if hasattr(self, 'conn'):
            self.conn.close()