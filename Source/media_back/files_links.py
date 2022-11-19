#Раскоментировать для получения file_id
#from aiogram import types
#from loader import dp

branding = "AgACAgIAAxkBAAIBQWN4LujIrP4x2_s9C0WsO5DtFQq2AALJvzEb_SLBS7L_LDFmXGWpAQADAgADcwADKwQ"
brand_book = "BQACAgIAAxkBAAICPmN4OBmZ-XnFcmvimKL3fQgGnzkAA-MfAAKESMBL7p5NQq7VjZwrBA"


# Для определения ID видео при создании бота с новым адрессом
# @dp.message_handler(state = '*', content_types=["video"])
# async def handle_video(message):
#    video_id=message.video.file_id
#    print(video_id)
#    await bot.send_message(message.from_user.id, video_id)

# @dp.message_handler(content_types=['photo'])
# async def scan_message(msg: types.Message):
#    document_id = msg.photo[0].file_id
#    file_info = await bot.get_file(document_id)
#    print(f'file_id: {file_info.file_id}')

#@dp.message_handler(content_types=["document"])
#async def sticker_file_id(message: types.Message):
#    await message.answer(f"ID документа {message.document.file_id}")