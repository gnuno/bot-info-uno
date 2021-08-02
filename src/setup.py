import telebot
import logging
import os

# Configurar logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)

MODE = os.environ.get("MODE")
API_TOKEN = os.environ.get(
    'TOKEN') or ''  # Aquí ponés el token de prueba
bot = telebot.TeleBot(API_TOKEN, parse_mode='HTML')
