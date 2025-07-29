from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

start_menu=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🧑‍💻 Admin 1"),
            KeyboardButton(text="👨‍💻 Admin 2"),

        ],
        [
            KeyboardButton("60 UC"),
            KeyboardButton("325 UC"),
            KeyboardButton("660 UC"),
            KeyboardButton("1800 UC")

        ],


    ],
    resize_keyboard=True
)
