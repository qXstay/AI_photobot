import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise EnvironmentError("❗ BOT_TOKEN не найден в переменных окружения. Используйте .env.example")