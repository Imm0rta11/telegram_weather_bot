from aiogram.types import(
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Find out the weather'),
            KeyboardButton(text='Credits'),
        ]
    ],
    one_time_keyboard=False,
    resize_keyboard=True,
)

cred_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Github', url='https://github.com/Imm0rta11')
        ]
    ]
)
