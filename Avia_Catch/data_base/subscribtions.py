import sqlite3 as sq
from aiogram import types

def create ():
    global cur, con
    with sq.connect('subscriptions.db') as con:
        cur = con.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS subs_data(
            id INTEGER PRIMARY KEY,
            user_id INTEGER ,
            destination TEXT,
            departure TEXT, 
            data TEXT,
            limit_price FLOAT,
            baggage INTEGER,
            booking_payment INTEGER
        )"""
        )

async def add_command(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO subs_data(user_id, destination, departure, data, limit_price, baggage, booking_payment) VALUES (?, ?, ?, ?, ?, ?, ?)',
        tuple(data.values()))
        con.commit()

async def show_last_data_id (user_id: int, message: types.Message):
    data = cur.execute (f'SELECT * FROM (SELECT * FROM subs_data WHERE user_id == {user_id}) ORDER BY id  DESC LIMIT 1').fetchone()
    await message.answer(f"""Твоя подписка, проверяй:\n
        id: {data[1]}\n
        Город прибытия: {data[2]}\n
        Город отправления: {data[3]}\n
        Дата: {data[4]}\n
        Максимальная стоимость: {data[5]}\n
        Наличия багажа (1/0): {data[6]}\n
        Купить_1/Забронировать_0: {data[7]}\n\n
    """
    )
    return data[0]

async def delete_last_data_id (id_: int):
    cur.execute (f'DELETE FROM subs_data WHERE id == {id_}')
    con.commit()

async def show_all_subs_id (user_id: int, message: types.Message):
    for data in cur.execute(f'SELECT * FROM subs_data WHERE user_id == {user_id}').fetchall():
        await message.answer (f"""Твоя подписка:\n
            id подписки: {data[0]}\n
            Город прибытия: {data[2]}\n
            Город отправления: {data[3]}\n
            Дата: {data[4]}\n
            Максимальная стоимость: {data[5]}\n
            Наличия багажа (1/0): {data[6]}\n
            Купить_1/Забронировать_0: {data[7]}\n\n
        """)