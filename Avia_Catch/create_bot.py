from aiogram import Bot  
from aiogram.dispatcher import Dispatcher
from settings import *
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage() 

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storage)

 