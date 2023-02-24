from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from filters import IsPrivate
from loader import dp, bot


@dp.message_handler(IsPrivate(), CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!")
    await bot.send_message(chat_id="@groupForsBots", text="Good morning!")
    member = await bot.get_chat_member(chat_id=-1001664238263, user_id=message.from_user.id)
    print(member.user)
