from aiogram import types
from aiogram.dispatcher.filters.builtin import Command

from loader import dp

superusers = [1019133305, 1111111111]

# @dp.message_handler(chat_id=superusers, text='secret')
@dp.message_handler(chat_id=superusers, commands='start')
async def photohandler(msg: types.Message):
    await msg.answer("Xush kelibsiz SuperUser!")