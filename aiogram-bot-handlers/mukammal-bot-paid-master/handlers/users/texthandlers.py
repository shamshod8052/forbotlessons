from aiogram import types
from aiogram.dispatcher.filters import Text

from loader import dp

@dp.message_handler(Text(equals='assalomu alaykum', ignore_case=True))
async def text_example(msg: types.Message):
    await msg.reply('Vaaleykum assalom')

@dp.message_handler(Text(contains='assalomu', ignore_case=True))
async def text_example(msg: types.Message):
    await msg.reply('Vaaleykum assalom')

@dp.message_handler(Text(contains='ahmoq', ignore_case=True))
async def text_example(msg: types.Message):
    await msg.reply("o'zing ahmoq")

@dp.message_handler(Text(startswith='man', ignore_case=True))
async def text_example(msg: types.Message):
    await msg.reply("Sanmi???\nMen deb ayt ukam!")

@dp.message_handler(Text(endswith="bordim"))
async def text_example(msg: types.Message):
    await msg.reply("bordingmi")
