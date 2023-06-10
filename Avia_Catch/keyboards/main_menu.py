from aiogram.types import ReplyKeyboardMarkup,KeyboardButton, ReplyKeyboardRemove

button1 = KeyboardButton('/Список_активных_подписок')
button2 = KeyboardButton('/Создать_новую_подписку')
button3 = KeyboardButton('/Отменить_последнюю_подписку')

main_keyboard =  ReplyKeyboardMarkup(resize_keyboard=True)
main_keyboard.row(button1,button2).add(button3)