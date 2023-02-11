from aiogram import types
from aiogram.dispatcher.filters import builtin

from loader import dp

@dp.message_handler(hashtags='money')
@dp.message_handler(cashtags=['eur', 'usd'])
@dp.message_handler(content_types=types.ContentTypes.PHOTO)
async def photohandler(message: types.Message):
    await message.answer("Yee akang kuchaydi!")

@dp.message_handler()
async def photohandler(message: types.Message):
    await message.answer("Yee akang kuchaydi!")
