from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.filters.callback_data import CallbackData

start_kb = InlineKeyboardMarkup(
    inline_keyboard = [
        [InlineKeyboardButton(text='Новый счёт', callback_data='new'),] 
        
    ], resize_keyboard=True
)

# InlineKeyboardButton(text='Новая группа', callback_data='new_group')],
        # [InlineKeyboardButton(text='Мои финансы', callback_data='my_bills')]