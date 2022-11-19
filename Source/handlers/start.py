from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton

from config import ADMIN_ID, VIP_LIST
from loader import dp, bot

from Source.keyboards import after_promo_video, utochenie, questions, go_back_button
from Source.states import MenuStates
from Source import text_of_message
from Source.utils import send_text_separately
from Source.media_back import files_links



@dp.message_handler(text='/start', state = ['*'])
async def start(message: types.Message):
    await message.answer(text_of_message.greeting_text, reply_markup=after_promo_video)
    await bot.send_document(message.from_user.id, files_links.brand_book)
    await MenuStates.what_do_you_want.set()

@dp.message_handler(text='/statistics', state = ['*'])
async def get_statistics(message: types.Message):
    ID = message.from_user.id
    if ID == int(ADMIN_ID) or ID in VIP_LIST:
        await message.answer("Очень скоро здесь будет статистика использования кнопок👌", reply_markup=ReplyKeyboardRemove())



@dp.message_handler(text='Назад ◀', state=[MenuStates.go_back, MenuStates.go_to_manager])
async def roll_back(message, state):
    await what_you_want(message, state)


@dp.message_handler(state=MenuStates.what_do_you_want)
async def what_you_want(message: types.Message, state: FSMContext):
    await message.answer(text_of_message.question1, reply_markup=utochenie)
    await MenuStates.state_navigator.set()


@dp.message_handler(state=MenuStates.state_navigator)
async def state_navigator(message, state):
    if message.text == "Уточнить информацию ℹ️":
        await ask_question(message,state)
    elif message.text == "Связаться с менеджером 👩🏼‍💻":
        await manager(message, state)
    else:
        await message.answer(text_of_message.error_text)


@dp.message_handler(state=MenuStates.go_to_manager)
async def manager(message: types.Message, state: FSMContext):
    await message.answer(text_of_message.go_to_manager_text, reply_markup=ReplyKeyboardRemove())
    await message.answer("Менеджер Мария проконсультирует Вас!",
                         reply_markup=InlineKeyboardMarkup().
                         add(InlineKeyboardButton('Оформить заказ ✅',
                                                 url='https://t.me/packman_maria')))
    await way_to_back(message, state)


@dp.message_handler(state=MenuStates.ask_question)
async def ask_question(message, state):
    await message.answer(text_of_message.witch_question, reply_markup=questions)
    await MenuStates.questons.set()


@dp.message_handler(state=MenuStates.questons)
async def question(message: types.Message, state: FSMContext):
    if message.text == "Стоимость 🧾":
        await prise(message,state)
    elif message.text == "Доставка 📦":
        await delivering(message,state)
    elif message.text == "Оплата 💳":
        await payment(message,state)
    elif message.text == "Брендирование пакетов 🔥":
        await branding(message, state)
    else:
        await message.answer(text_of_message.error_text)


async def prise(message: types.Message, state: FSMContext):
    await send_text_separately(text_of_message.prise, message.from_user.id,  keyboard_dlt_status=True)
    with open(f"Source/media_back/images/prise.PNG", 'rb') as photo:
        await bot.send_photo(message.from_user.id, photo)
    await way_to_back(message, state )


async def delivering(message: types.Message, state: FSMContext):
    await send_text_separately(text_of_message.delivering, message.from_user.id, keyboard_dlt_status=True)
    await way_to_back(message, state )


async def payment(message: types.Message, state: FSMContext):
    await send_text_separately(text_of_message.payment, message.from_user.id, keyboard_dlt_status=True)
    await way_to_back(message, state)


async def branding(message: types.Message, state: FSMContext):
    await send_text_separately(text_of_message.branding, message.from_user.id, keyboard_dlt_status=True)
    await bot.send_photo(message.from_user.id, files_links.branding)
    await way_to_back(message, state)


async def way_to_back(message: types.Message, state:FSMContext):
    await message.answer(text_of_message.click_back_button, reply_markup=go_back_button)
    await MenuStates.go_back.set()

