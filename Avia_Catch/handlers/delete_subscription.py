from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text

from data_base import users, subscribtions

class FSMDelete (StatesGroup):
    id_ = State ()
    Yes_Now = State()

async def delete_start (message: types.Message):
    await message.answer ('Напиши свой id, чтобы я мог отменить последнюю подписку')
    await users.show_all(message)
    await FSMDelete.id_.set()

async def delete_question (message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['id'] = await subscribtions.show_last_data_id (int(message.text), message)
    await message.answer ('Уверен, удаляю? (Да/Нет)')
    await FSMDelete.next ()

async def delete_data (message: types.Message, state:FSMContext):
    if message.text == 'Да':
        async with state.proxy() as data:
            #await message.answer(data['id'])
            await subscribtions.delete_last_data_id (data['id'])
        await message.answer ('Подписка отменена')
    elif message.text == 'Нет':
        await message.answer ('Хорошо, не буду')
    await state.finish()

def register_handlers_delete_subscription (dp : Dispatcher):
    dp.register_message_handler(delete_start, commands=['Отменить_последнюю_подписку'], state=None)
    dp.register_message_handler(delete_question, state=FSMDelete.id_)
    dp.register_message_handler(delete_data, state=FSMDelete.Yes_Now)