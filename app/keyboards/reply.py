from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📅 Бронирование (демо)")],
        [KeyboardButton(text="🛒 Каталог (демо)")],
        [KeyboardButton(text="📈 Отчёт (демо)")]
    ],
    resize_keyboard=True
)
