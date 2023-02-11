from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp

# https://t.me/shamshod_shaxsiy_bot?start=kunuz
# @dp.message_handler(CommandStart(deep_link='kunuz'))
# async def bot_start(message: types.Message):
#     args = message.get_args()
#     await message.answer(f"Salom, {message.from_user.full_name}! Sizni {args} taklif qildi!")

# @dp.message_handler(command='boshla')  # /boshla
a = dict()
@dp.message_handler(commands='start')
@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    args = message.get_args()
    if message.from_user.id not in a:
        a[message.from_user.id] = 0
        a[int(args)] += 1
    print(a)
    await message.answer(f"Salom, {message.from_user.full_name}!")

