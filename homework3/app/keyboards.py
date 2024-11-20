from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

buttons = [
     [KeyboardButton(text='Серьги'), KeyboardButton(text='Косметика')],
     [KeyboardButton(text='Подарки')]
]

keyboard = ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True, input_field_placeholder='Выберите кнопку')

ear_keyboard=ReplyKeyboardMarkup(keyboard=[
     [KeyboardButton(text='Сердечки'), KeyboardButton(text='Звездочки'), KeyboardButton(text='Облачко')],
     [KeyboardButton(text='Каффы'), KeyboardButton(text='Ягодки')],
], input_field_placeholder='Выберите кнопку')

cosm_keyboard = ReplyKeyboardMarkup(keyboard=[
     [KeyboardButton(text='Тающие блески'), KeyboardButton(text='Тени')],
     [KeyboardButton(text='Подводки'), KeyboardButton(text='Румяна')],
], input_field_placeholder='Выберите кнопку')

gift_keyboard = ReplyKeyboardMarkup(keyboard=[
     [KeyboardButton(text='Мягкие игрушки'), KeyboardButton(text='Кружки с милым принтом')],
     [KeyboardButton(text='Картины по номерам'), KeyboardButton(text='Лего наборы')],
],  input_field_placeholder='Выберите кнопку')