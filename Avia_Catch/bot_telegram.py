from aiogram import Bot  
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from create_bot import *
from handlers import main_handlers, create_subscription, delete_subscription, subscriptions
from data_base import users, subscribtions

class TelegramBot:

    def __init__(self) -> None:
        self.bot = bot
        self.dp = dp
        users.create()
        subscribtions.create()
        
    def show_main_menu(self):
        main_handlers.register_handlers_main_menu(self.dp)
    
    def create_subs(self):
        create_subscription.register_handlers_create_subscriptions(self.dp)
 
    def delete_subs(self):
        delete_subscription.register_handlers_delete_subscription(self.dp)

    def active_subs(self):
        subscriptions.register_handlers_subscriptions(self.dp)
        

bot_1 = TelegramBot()
bot_1.show_main_menu()
bot_1.create_subs()
bot_1.delete_subs()
bot_1.active_subs()

executor.start_polling (bot_1.dp, skip_updates=True)

