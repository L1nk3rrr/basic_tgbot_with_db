from aiogram import types

async def set_defautl_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "запустити бота")
        ]
    )