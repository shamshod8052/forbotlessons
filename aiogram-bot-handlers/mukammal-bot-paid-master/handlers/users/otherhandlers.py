from aiogram import types
from aiogram.dispatcher import filters

from loader import dp

#IsRepyFilter
@dp.message_handler(is_reply=True, commands='user_id')
async def reply_filter_example(msg: types.Message):
    await msg.answer(msg.reply_to_message.from_user.id)
#IsSenderContact
@dp.message_handler(content_types='contact', is_sender_contact=True)
# @dp.message_handler(filters.IsSenderContact(True), content_types='contact')
async def reply_filter_example(msg: types.Message):
    await msg.answer('Rahmat contactingiz qabul qilindi')


#ForwardedMessageFilter
@dp.message_handler(is_forwarded=True)
async def reply_filter_example(msg: types.Message):
    await msg.answer('Birovning xabarini menga yuboryapsizmi?')

#ChatTypeFilter
# @dp.message_handler(chat_type='group', commands='is_pm')
@dp.message_handler(filters.ChatTypeFilter(types.ChatType.PRIVATE), commands='shaxsiy')
async def reply_filter_example(msg: types.Message):
    await msg.answer('Bu shaxsiy bot!')