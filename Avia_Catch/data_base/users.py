import sqlite3 as sq
from aiogram import types

def create (): 
    global con, cur
    with sq.connect ('users.db') as con:
            cur = con.cursor()
            cur.execute("""CREATE TABLE IF NOT EXISTS users_data(
                user_id INTEGER PRIMARY KEY,
                name TEXT, 
                surname TEXT, 
                name_father TEXT, 
                passport TEXT,
                birthday TEXT,
                sex TEXT,
                mail TEXT,
                phone_number TEXT
                )"""
            )
            
async def add_command (state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO users_data (name, surname, name_father, passport, birthday, sex, mail, phone_number) VALUES (?, ?, ?, ?, ?, ?, ?, ?)', 
        tuple(data.values())) 
        con.commit()

async def show_last (message: types.Message):
    cur.execute ('SELECT * FROM users_data ORDER BY user_id DESC LIMIT 1')
    last = cur.fetchone()
    await message.answer(f"""Проверяй внимательно свои данные\n
        id: {last[0]}\n
        Имя: {last[1]}\n
        Фамилия: {last[2]}\n
        Отчество: {last[3]}\n
        Серия и номер паспорта: {last[4]}\n
        Дата рождения: {last[5]}\n
        Пол: {last[6]}\n
        Почта: {last[7]}\n
        Номер телефона: {last[8]}\n
    """
    )
    return last[0]

async def show_all (message: types.Message):
    for data in cur.execute ('SELECT * FROM users_data').fetchall():
        await message.answer (f"""Пользователь:\n
            id: {data[0]}\n
            Имя: {data[1]}\n
            Фамилия: {data[2]}\n
    """)

async def show_data_user (user_id: int, message: types.Message):
    data = cur.execute (f'SELECT * FROM users_data WHERE user_id == {user_id}').fetchone()
    await message.answer(f"""Твои данные:\n
        id: {data[0]}\n
        Имя: {data[1]}\n
        Фамилия: {data[2]}\n
        Отчество: {data[3]}\n
        Серия и номер паспорта: {data[4]}\n
        Дата рождения: {data[5]}\n
        Пол: {data[6]}\n
        Почта: {data[7]}\n
        Номер телефона: {data[8]}\n
    """
    )