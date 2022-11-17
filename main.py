import logging

from aiogram.utils import executor

from config import ADMIN_ID
from loader import dp

logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.INFO)


async def on_startup(dispatcher):
    await dp.bot.send_message(ADMIN_ID, "Бот Запущен")

if __name__ == '__main__':
    import Source.handlers
    executor.start_polling(dp, on_startup=on_startup,skip_updates=True)



