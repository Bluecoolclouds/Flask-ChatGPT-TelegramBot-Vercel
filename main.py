# -*- coding: utf-8 -*-

import logging
import telegram
import os
from flask import Flask, request
from telegram.ext import Dispatcher, MessageHandler, Filters

telegram_bot_token = str(os.getenv("6556995841:AAE4ZccxFlpMzEtf1ZLGaDsbE13RYD-95D0"))

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


@bot.message_handler(commands=['start'])
def start_command(message):
  bot.send_message(message.chat.id, f"Цена на рублей")



if __name__ == "__main__":
    # Running server
    app.run(debug=True)
