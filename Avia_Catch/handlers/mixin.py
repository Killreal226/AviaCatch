from aiogram import types, Dispatcher
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext

from create_bot import bot, dp
from handlers import create_subscription
from data_base import users


class FSMId_User(StatesGroup):
    id_ = State()


async def user_id (message: types.Message, state:FSMContext):
    await message.answer (f'Проверяй свои данные, если что то неверно нажми ОТМЕНА')
    async with state.proxy() as data:
        data['user_id'] = int(message.text)
    await users.show_data_user(user_id=int(message.text), message=message)
    await message.answer ('Хорошо, теперь введи город прибытия')
    await create_subscription.FSMCreate_Subscription.destination_city.set()      

def register_handlers_mixin(dp : Dispatcher):
    dp.register_message_handler(user_id, state=FSMId_User.id_)


