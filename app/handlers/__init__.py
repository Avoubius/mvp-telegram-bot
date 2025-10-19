from aiogram import Dispatcher
from .start import router as start_router
from .booking import router as booking_router
from .catalog import router as catalog_router
from .sheets import router as sheets_router

def setup_routers(dp: Dispatcher):
    dp.include_router(start_router)
    dp.include_router(booking_router)
    dp.include_router(catalog_router)
    dp.include_router(sheets_router)
