import logging

from aiogram import types
from aiogram.utils.exceptions import CantParseEntities

from loader import dp, db_learn_interface


@dp.message_handler(commands=['get_user_by_id'])
async def get_user_info(msg: types.Message):
    try:
        user_id = int(msg.text.split()[1])
        user_info = db_learn_interface.get_user_by_id(user_id)
        await msg.reply(user_info)
    except (IndexError, ValueError):
        await msg.reply("Веддіть команду у такому форматі:\n/get_user_by_id user_id")

@dp.message_handler(commands=['get_user_by_name'])
async def get_user_info(msg: types.Message):
    user_name = msg.get_args()
    if user_name:
        user_info = db_learn_interface.get_user_by_name(user_name)
        await msg.reply(user_info)
    else:
        await msg.reply("Веддіть команду у такому форматі:\n/get_user_by_name user_name")

@dp.message_handler(commands=['add_me'])
async def add_user(msg: types.Message):
    user_id = msg.from_user.id
    first_name = msg.from_user.first_name
    last_name = msg.from_user.last_name
    user_name = msg.from_user.username

    if not db_learn_interface.user_exists(user_id):
        db_learn_interface.add_user_to_db(user_id, first_name, last_name, user_name)
        await msg.reply("Користувача було успішно додано")
    else:
        await msg.reply("Такий користувач вже існує")

@dp.message_handler(commands=['remove_me'])
async def remove_user(msg: types.Message):
    user_id = msg.from_user.id

    if db_learn_interface.user_exists(user_id):
        db_learn_interface.remove_user_from_db(user_id)
        await msg.reply("Користувача успішно видалено")
    else:
        await msg.reply("Такого користувача не існує")


@dp.message_handler(commands=['start'])
async def get_user_info(msg: types.Message):
    await msg.reply("Hello")
