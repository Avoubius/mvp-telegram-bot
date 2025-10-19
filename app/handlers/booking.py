from aiogram import Router, F
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from datetime import datetime, timedelta
from app.demo_store import STORE

router = Router()

class BookFlow(StatesGroup):
    resource = State()
    slot = State()

@router.message(F.text.contains("Бронирование"))
async def choose_resource(m: Message, state: FSMContext):
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=r, callback_data=f"res:{i}")]
        for i, r in enumerate(STORE.resources)
    ])
    await state.set_state(BookFlow.resource)
    await m.answer("Выбери площадку (демо):", reply_markup=kb)

@router.callback_query(F.data.startswith("res:"))
async def choose_slot(c: CallbackQuery, state: FSMContext):
    res_idx = int(c.data.split(":")[1])
    await state.update_data(resource=res_idx)
    now = datetime.now().replace(minute=0, second=0, microsecond=0)
    slots = [now + timedelta(hours=h) for h in (1, 2, 3)]
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=s.strftime("%d.%m %H:%M"), callback_data=f"slot:{s.isoformat()}")]
        for s in slots
    ])
    await state.set_state(BookFlow.slot)
    await c.message.edit_text("Выбери время (демо):", reply_markup=kb)

@router.callback_query(F.data.startswith("slot:"))
async def confirm(c: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    start = datetime.fromisoformat(c.data.split(":")[1])
    end = start + timedelta(hours=1)
    res_title = STORE.resources[data["resource"]]
    STORE.bookings.append({
        "user_id": c.from_user.id,
        "resource": res_title,
        "start": start,
        "end": end,
        "status": "confirmed (demo)"
    })
    await state.clear()
    await c.message.edit_text(f"✅ Бронь (демо): {res_title}\n{start:%d.%m %H:%M}–{end:%H:%M}\n"
                              "Это демонстрация — реальная бронь не создаётся.")
