from aiogram import Router, F
from aiogram.types import Message
from app.keyboards.reply import main_kb
from app.demo_store import STORE

router = Router()

@router.message(F.text == "/start")
async def start_cmd(m: Message):
    await m.answer(
        "Привет! Это демо-бот для портфолио.\n"
        "🧪 Ничего реально не бронирует/не платит.\n"
        "Команда /reset — очистить демо-данные.",
        reply_markup=main_kb
    )

@router.message(F.text == "/reset")
async def reset_cmd(m: Message):
    STORE.reset()
    await m.answer("✅ Демо-данные сброшены.")
