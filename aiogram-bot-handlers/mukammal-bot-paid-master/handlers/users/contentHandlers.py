from aiogram import types
from aiogram.dispatcher.filters import builtin

from loader import dp

@dp.message_handler(content_types=types.ContentType.all())
@dp.message_handler(content_types=types.ContentTypes.PHOTO)
async def photohandler(message: types.Message):
    await message.answer("Bu rasm")


@dp.message_handler(content_types='document')
async def photohandler(message: types.Message):
    await message.answer("Bu hujjat")

    @dp.message_handler(content_types='sticker')
    async def photohandler(message: types.Message):
        await message.answer("Bu sticker")

@dp.message_handler(content_types='video')
async def photohandler(message: types.Message):
    await message.answer("Bu video")

@dp.message_handler(content_types='text')
async def photohandler(message: types.Message):
    await message.answer("Bu matn")


@dp.message_handler(content_types='audio')
async def photohandler(message: types.Message):
    await message.answer("Bu audio")