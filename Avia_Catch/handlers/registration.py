from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher

from handlers import create_subscription
from data_base import users

class FSMRegistrationUser(StatesGroup):
    name = State()
    surname = State()
    name_father = State()
    passport = State()
    birthday = State()
    sex = State()
    mail = State()
    phone_number = State()

async def load_name (message : types.Message, state : FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMRegistrationUser.next()
    await message.answer ('Твоя ФАМИЛИЯ')

async def load_surname (message : types.Message, state : FSMContext):
    async with state.proxy() as data:
        data['surname'] = message.text
    await FSMRegistrationUser.next()
    await message.answer ('Твое ОТЧЕСТВО')

async def load_name_father (message : types.Message, state : FSMContext):
    async with state.proxy() as data:
        data['name_father'] = message.text
    await FSMRegistrationUser.next()
    await message.answer ('СЕРИЮ И НОМЕР ПАСПОРТА ')

async def load_passport (message : types.Message, state : FSMContext):
    async with state.proxy() as data:
        data['passport'] = message.text
    await FSMRegistrationUser.next()
    await message.answer ('ДАТА РОЖДЕНИЯ')

async def load_birthday (message : types.Message, state : FSMContext):
    async with state.proxy() as data:
        data['birthday'] = message.text
    await FSMRegistrationUser.next()
    await message.answer ('Твой ПОЛ? Ответ:м/ж')

async def load_sex (message : types.Message, state : FSMContext):
    async with state.proxy() as data:
        if message.text == 'м':
            data['sex'] = 'муж'
        elif message.text == 'ж':
            data['sex'] = 'жен'
    await FSMRegistrationUser.next()
    await message.answer ('ПОЧТУ на которую тебе если что придет билет')

async def load_mail (message : types.Message, state : FSMContext):
    async with state.proxy() as data:
        data['mail'] = message.text
    await FSMRegistrationUser.next()
    await message.answer ('И последнее: твой НОМЕР ТЕЛЕФОНА (через +7)')

async def load_phone_number (message : types.Message, state : FSMContext):
    async with state.proxy() as data:
        data['phone_number'] = message.text
    
    await users.add_command(state) 
    user_id = await users.show_last(message)

    await state.finish()

    async with state.proxy() as data:
        data['user_id'] = user_id
    await message.answer ('Если все верно, то давай займемся  самой подпиской на рейс. Введи ГОРОД ПРИБЫТИЯ, если где то была допущена ошибка напиши ОТМЕНА')
    await create_subscription.FSMCreate_Subscription.destination_city.set()

def register_handlers_regisration(dp : Dispatcher):
    dp.register_message_handler(load_name, state=FSMRegistrationUser.name)
    dp.register_message_handler(load_surname, state=FSMRegistrationUser.surname)
    dp.register_message_handler(load_name_father, state=FSMRegistrationUser.name_father)
    dp.register_message_handler(load_passport, state=FSMRegistrationUser.passport)
    dp.register_message_handler(load_birthday, state=FSMRegistrationUser.birthday)
    dp.register_message_handler(load_sex, state=FSMRegistrationUser.sex)
    dp.register_message_handler(load_mail, state=FSMRegistrationUser.mail)
    dp.register_message_handler(load_phone_number, state=FSMRegistrationUser.phone_number)
    