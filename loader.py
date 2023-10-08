from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from data import config
from utils.db_api import BotDB, DbLearnInterface, MyNameInterface

bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
db_bot = BotDB(config.DB_FILE)
db_learn_interface = DbLearnInterface()
my_name_db_conn = MyNameInterface()