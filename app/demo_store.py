from collections import defaultdict

class DemoStore:
    def __init__(self):
        # демо-данные в памяти (RAM)
        self.bookings = []                 # [{user_id, resource, start, end, status}]
        self.cart = defaultdict(list)      # user_id -> [{title, price, qty}]
        self.orders = []                   # [{user_id, amount, status}]
        self.catalog = [
            {"sku":"PASS-1","title":"Разовое посещение","price":150},
            {"sku":"PASS-4","title":"Абонемент 4 тренировки","price":520},
            {"sku":"PASS-8","title":"Абонемент 8 тренировок","price":960},
            {"sku":"SHIRT-CLUB","title":"Футболка клуба","price":350},
            {"sku":"WATER-05","title":"Бутылка воды 0.5","price":25},
        ]
        self.resources = ["Корт A (Košutka)", "Корт B (Doubravka)"]

    def reset(self):
        self.bookings.clear()
        self.cart.clear()
        self.orders.clear()

STORE = DemoStore()
