from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext

from create_bot import bot, dp
from keyboards import main_keyboard


async def command_start (message: types.Message):
    await message.answer('Начали', reply_markup=main_keyboard)

async def cancel_handlers (message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.answer ('Я все закрыл, не переживай')

def register_handlers_main_menu(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start','help'])
    dp.register_message_handler(cancel_handlers, state= "*", commands=['отмена'])
    dp.register_message_handler(cancel_handlers, Text(equals='отмена', ignore_case=True), state="*")
 