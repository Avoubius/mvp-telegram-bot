import asyncio
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

# НОВОЕ: импорт свойств бота и перечисления ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from app.config import BOT_TOKEN
from app.handlers import setup_routers

def run():
    asyncio.run(_main())

async def _main():
    if not BOT_TOKEN:
        raise RuntimeError("BOT_TOKEN пуст. Заполни его в .env")

    # БЫЛО:
    # bot = Bot(token=BOT_TOKEN, parse_mode="HTML")

    # СТАЛО: задаём parse_mode через default
    bot = Bot(
        token=BOT_TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )

    dp = Dispatcher(storage=MemoryStorage())
    setup_routers(dp)
    print("✅ Bot started. Press Ctrl+C to stop.")
    await dp.start_polling(bot)
