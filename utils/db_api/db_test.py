from .db import BotDB

class MyNameInterface:
    def connect(self, db_base: BotDB):
        self.cursor = db_base.cursor
        self.conn = db_base.conn
    
    #Ваші методи