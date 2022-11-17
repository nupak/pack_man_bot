from time import sleep

from aiogram.types import ReplyKeyboardRemove

from loader import bot


async def send_text_separately(text, user_id, keyboard_dlt_status=False, keyboard_to_send=None):
    separate_text = text.split("||")
    status_for_delete = keyboard_dlt_status
    last_element = len(separate_text)-1
    for i in range(len(separate_text)):
        if status_for_delete is True:
            await bot.send_message(user_id, separate_text[i], reply_markup=ReplyKeyboardRemove())
            status_for_delete = False
        elif keyboard_to_send and i == last_element:
            await bot.send_message(user_id, separate_text[i], reply_markup=keyboard_to_send)
        else:
            await bot.send_message(user_id, separate_text[i])
        sleep(0.3)