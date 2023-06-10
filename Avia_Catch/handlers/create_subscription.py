from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text

from create_bot import bot, dp
from handlers import mixin, registration
from data_base import users, subscribtions

class FSMCreate_Subscription(StatesGroup):
    user_in_database = State()
    destination_city = State()
    departure_city = State()
    date = State()
    limit_price = State()
    baggage = State()
    booking_payment = State()

#@dp.message_handler(commands='Создать новую подписку', state=None)
async def start_create (message: types.Message):
    await FSMCreate_Subscription.user_in_database.set()
    
    await message.answer('Проверь, есть ли твои данные в моей базе данных (Ответ: Да/Нет)')
    await users.show_all(message)

#dp.message_handler(state=FSMCreate_Subscription.user_in_database)
async def check_user(message: types.Message, state: FSMContext):
    if message.text == 'Да':
        await message.answer('Хорошо, тогда напиши мне свой ID')
        await mixin.FSMId_User.id_.set()
    elif message.text == 'Нет':
        await message.answer('Давай тогда зарегистрируемся. Введи свое ИМЯ')
        await registration.FSMRegistrationUser.name.set()
        #await message.answer ('Проверяй свои данные, если нет, начинай заново. Твои Данные') 


#dp.message_handler(state=FSMCreate_Subscription.destination_city)
async def load_destination (message : types.Message, state : FSMContext):
    async with state.proxy() as data:
        data['destination'] = message.text
    await FSMCreate_Subscription.next()
    await message.answer ('Теперь ГОРОД отправления')

#dp.message_handler(state=FSMCreate_Subscription.departure_city)
async def load_departure (message : types.Message, state : FSMContext):
    async with state.proxy() as data:
        data['departure'] = message.text
    await FSMCreate_Subscription.next()
    await message.answer ('В какие ДАТЫ намерен вылетать? Ответ должен быть или одна дата или даты через тире Ответ(чч.мм.гггг) или  (чч.мм.гггг-чч.мм.гггг)')

#dp.message_handler(state=FSMCreate_Subscription.date)
async def load_data (message : types.Message, state : FSMContext):
    async with state.proxy() as data:
        data['data'] = message.text
    await FSMCreate_Subscription.next()
    await message.answer ('Какую МАКСИМАЛЬНУЮ СТОИМОСТЬ ты готов был бы отдать?')

#dp.message_handler(state=FSMCreate_Subscription.limit_price)
async def load_limit_price (message : types.Message, state : FSMContext):
    async with state.proxy() as data:
        data['limit_price'] = float (message.text)
    await FSMCreate_Subscription.next()
    await message.answer ('Будет ли у тебя БАГАЖ? Ответ:(Да/Нет)')

#dp.message_handler(state=FSMCreate_Subscription.baggage)
async def load_baggage (message : types.Message, state : FSMContext):
    async with state.proxy() as data:
        if message.text == 'Да':
            data['baggage'] = 1
        elif message.text == 'Нет':
            data['baggage'] = 0
    await FSMCreate_Subscription.next()
    await message.answer ('Что мне для тебя сделать: Просто ЗАБРОНИРОВАТЬ или сразу КУПИТЬ? Ожидаю ответ: Забронировать/Купить')

#dp.message_handler(state=FSMCreate_Subscription.booking_payment)
async def load_booking_payment (message : types.Message, state : FSMContext):
    async with state.proxy() as data:
        if message.text == 'Купить':
            data['booking_payment'] = 1
        elif message.text == 'Забронировать':
            data['booking_payment'] = 0
    
    await subscribtions.add_command(state) 
    await message.answer ('Итак, подписка оформлена')
    async with state.proxy() as data:
        await subscribtions.show_last_data_id (data['user_id'],message)
    await message.answer ('Когда что то изменится я тебе напишу, отдыхай')
    await state.finish()


def register_handlers_create_subscriptions(dp : Dispatcher):
    dp.register_message_handler(start_create, commands=['Создать_новую_подписку'], state=None)
    dp.register_message_handler(check_user, state=FSMCreate_Subscription.user_in_database)
    dp.register_message_handler(load_destination, state=FSMCreate_Subscription.destination_city)
    dp.register_message_handler(load_departure, state=FSMCreate_Subscription.departure_city)
    dp.register_message_handler(load_data, state=FSMCreate_Subscription.date)
    dp.register_message_handler(load_limit_price, state=FSMCreate_Subscription.limit_price)
    dp.register_message_handler(load_baggage, state=FSMCreate_Subscription.baggage)
    dp.register_message_handler(load_booking_payment, state=FSMCreate_Subscription.booking_payment)

    mixin.register_handlers_mixin(dp)
    registration.register_handlers_regisration(dp)



