from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text

from data_base import users, subscribtions
from handlers import cheap_flights

class FSMsubscriptions (StatesGroup):
    id_= State()
    subs_id = State()

async def subs_start (message: types.Message):
    await message.answer ('Напиши свой id, чтобы я вывел все твои подписки')
    await users.show_all(message)
    await FSMsubscriptions.id_.set()

async def load_id (message: types.Message):
    await message.answer ('Все твои активные подписки')
    await subscribtions.show_all_subs_id (int(message.text), message)
    await message.answer ('Чтобы отменить какую то подпску напиши ее id и через ":" exit\nПример: 1:exit')
    await message.answer ('Чтобы посмотреть самые дешевые рейсы на данный момент по какой то подписке напиши ее id и через ":" info\nПример: 1:info')
    await FSMsubscriptions.next()

async def load_subs_id (message: types.Message, state: FSMContext):
    id_action = message.text.split(":")
    if len(id_action) == 2:
        if id_action[1] == 'exit':
            await subscribtions.delete_last_data_id (int(id_action[0]))
            await message.answer ('Все хорошо, подписка отменена')
        elif id_action[1] == 'info':
            await message.answer ('Самые дешевые рейсы по твоей подписке:')
            #Запуск cheap_flights
        await state.finish()

def register_handlers_subscriptions (dp:Dispatcher):
    dp.register_message_handler(subs_start, commands=['Список_активных_подписок'], state=None)
    dp.register_message_handler(load_id, state=FSMsubscriptions.id_)
    dp.register_message_handler(load_subs_id, state=FSMsubscriptions.subs_id)

