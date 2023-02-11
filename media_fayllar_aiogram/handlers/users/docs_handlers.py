from loader import dp, bot
from aiogram.types import ContentTypes, Message, ContentType
from pathlib import Path

downloads_path = Path().joinpath("downloads", "categories")
downloads_path.mkdir(parents=True, exist_ok=True)

@dp.message_handler(content_types=ContentTypes.DOCUMENT)
async def doc_handler(message: Message):
    await message.document.download(destination=downloads_path)
    doc_id = message.document.file_id
    await message.answer(f"Siz fayl yubordingiz.\nID: {doc_id}")

@dp.message_handler(content_types=ContentTypes.VIDEO)
async def doc_handler(message: Message):
    await message.video.download(destination=downloads_path)
    doc_id = message.video.file_id
    await message.answer(f"Siz video yubordingiz.\nID: {doc_id}")

@dp.message_handler(content_types=ContentTypes.PHOTO)
async def doc_handler(message: Message):
    await message.photo[-1].download(destination=downloads_path)
    doc_id = message.photo[-1].file_id
    await message.answer(f"Siz rasm yubordingiz.\nID: {doc_id}")

@dp.message_handler(content_types=ContentType.ANY)
async def doc_handler(message: Message):
    await message.answer(f"Siz {message.content_type} yubordingiz.")
