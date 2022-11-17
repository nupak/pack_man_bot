from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

after_promo_video = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Перейти в меню")]
    ],
    resize_keyboard=True
)


utochenie = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Уточнить информацию ℹ️"),
            KeyboardButton(text="Связаться с менеджером 👩🏼‍💻")
        ],
    ],
    resize_keyboard=True
)

questions = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Стоимость 🧾"),
            KeyboardButton(text="Оплата 💳"),
            KeyboardButton(text="Доставка 📦")
        ],
    ],
    resize_keyboard=True
)

go_back_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Назад ◀")]
    ],
    resize_keyboard=True
)