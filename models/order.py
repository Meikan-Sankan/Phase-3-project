# models/order.py

class Order:
    orders = []
    next_id = 1

    def __init__(self, restaurant_id, customer_name, items, total_price, status='Pending'):
        self.id = Order.next_id
        Order.next_id += 1
        self.restaurant_id = restaurant_id
        self.customer_name = customer_name
        self.items = items
        self.total_price = total_price
        self.status = status

    @classmethod
    def find_by_id(cls, order_id):
        for order in cls.orders:
            if order.id == order_id:
                return order
        return None

    def update_status(self, new_status):
        self.status = new_status

    def save(self):
        Order.orders.append(self)

    def delete(self):
        Order.orders = [order for order in Order.orders if order.id != self.id]

    @classmethod
    def get_all(cls):
        return cls.orders
