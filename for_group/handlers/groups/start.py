from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from filters import IsGroup
from loader import dp, bot


@dp.message_handler(IsGroup(), CommandStart())
async def bot_start(message: types.Message):
    print(type(message.chat.id), message.chat.id)
    await bot.send_message(chat_id=-1001664238263, text="Good morning!")
    await message.answer(f"Salom, {message.from_user.full_name}! Siz guruhdasiz!")
