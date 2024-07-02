from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Ob havo", callback_data='ob-havo'),
         InlineKeyboardButton(text="Dasturlash", callback_data='dasturlash')],
        [InlineKeyboardButton(text="ChatGpt", callback_data='chatgpt'),]
    ]
)
btn2 = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Tokyo", callback_data='tokyo'),
         InlineKeyboardButton(text="London", callback_data='london')],
        [InlineKeyboardButton(text="New-York", callback_data='new-york'),
         InlineKeyboardButton(text="Paris", callback_data='paris')],
        [InlineKeyboardButton(text="Madrid", callback_data='madrid'),
         InlineKeyboardButton(text="Dubai", callback_data='dubai')],
        [InlineKeyboardButton(text="Bosh menyuga qaytish⬅️", callback_data='back')],
   ]
)

btn3 = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Python", callback_data='python'),
         InlineKeyboardButton(text="Java", callback_data='java')],
        [InlineKeyboardButton(text="Ruby", callback_data='ruby'),
         InlineKeyboardButton(text="C++", callback_data='cpp')],
        [InlineKeyboardButton(text="Javascript", callback_data='javascript'),
         InlineKeyboardButton(text="Rust", callback_data='rust')],
        [InlineKeyboardButton(text="Bosh menyuga qaytish⬅️", callback_data='back')],
    ]
)
btn4 = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Bosh menyuga qaytish⬅️", callback_data='back')]
    ]
)