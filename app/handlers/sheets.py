from aiogram import Router, F
from aiogram.types import Message
from app.demo_store import STORE
import csv, os
from datetime import datetime

router = Router()

@router.message(F.text.contains("Отчёт"))
async def export_demo(m: Message):
    path = "report_demo.csv"
    orders = [o for o in STORE.orders if o["user_id"] == m.from_user.id]
    row = [datetime.now().strftime("%Y-%m-%d"), len(orders), sum(o["amount"] for o in orders)]
    write_header = not os.path.exists(path)
    with open(path, "a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if write_header:
            w.writerow(["Date", "Orders", "Revenue"])
        w.writerow(row)
    await m.answer(f"📄 Экспортировано (демо) → {path}")
