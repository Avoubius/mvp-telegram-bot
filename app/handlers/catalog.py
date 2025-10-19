from aiogram import Router, F
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from app.demo_store import STORE

router = Router()

@router.message(F.text.contains("Каталог"))
async def show_catalog(m: Message):
    for p in STORE.catalog:
        kb = InlineKeyboardMarkup(inline_keyboard=[[
            InlineKeyboardButton(text="Добавить", callback_data=f"add:{p['sku']}")
        ]])
        await m.answer(f"• {p['title']} — {p['price']} CZK", reply_markup=kb)
    await m.answer("Напиши <b>оплатить</b> для оформления (демо).")

@router.callback_query(F.data.startswith("add:"))
async def add(c: CallbackQuery):
    sku = c.data.split(":")[1]
    p = next(x for x in STORE.catalog if x["sku"] == sku)
    STORE.cart[c.from_user.id].append({"title": p["title"], "price": p["price"], "qty": 1})
    await c.answer("Добавлено (демо)")

@router.message(F.text.lower() == "оплатить")
async def pay_demo(m: Message):
    items = STORE.cart[m.from_user.id]
    if not items:
        await m.answer("Корзина пуста (демо).")
        return
    amount = sum(i["price"] * i["qty"] for i in items)
    STORE.orders.append({"user_id": m.from_user.id, "amount": amount, "status": "paid (demo)"})
    STORE.cart[m.from_user.id].clear()
    await m.answer(f"✅ Оплата имитирована. Сумма: {amount} CZK\nСтатус: paid (demo)")
