from aiogram import Router, types
from aiogram.filters import Command
from keyboards import get_back_to_menu_keyboard

start_router = Router()

async def send_welcome(message: types.Message):
    welcome_text = (
        "Привет! 👋 Это демонстрационная версия бота.\n\n"
        "В полной версии можно загружать фото и улучшать их с помощью нейросети."
    )
    await message.answer(welcome_text, reply_markup=get_back_to_menu_keyboard())

@start_router.message(Command("start"))
async def cmd_start(message: types.Message):
    await send_welcome(message)

@start_router.message(Command("help"))
async def cmd_help(message: types.Message):
    await message.answer(
        "Это демо-бот. Полная версия включает обработку фото и интеграцию с PiAPI и ImgBB.",
        reply_markup=get_back_to_menu_keyboard()
    )