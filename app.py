import logging
from aiogram import executor

import handlers
from loader import dp, db_bot, db_learn_interface, my_name_db_conn
from utils.commands import set_defautl_commands


async def on_startup(dispatcher):
    db_bot.open()
    
    db_learn_interface.connect(db_bot)
    db_learn_interface.create_default_table()

    my_name_db_conn.connect(db_bot)
    logging.info("Db has opened connection")
    await set_defautl_commands(dispatcher)

async def on_shutdown(dispatcher):
    db_bot.close()
    logging.info("Db has closed connection")


if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown)