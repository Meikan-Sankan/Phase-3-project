from db.database import Database

class Restaurant:
    def __init__(self, name, location, cuisine_type):
        self.id = None
        self.name = name
        self.location = location
        self.cuisine_type = cuisine_type

    def save(self):
        if self.id is None:
            self.id = Database.insert('restaurants', {
                'name': self.name,
                'location': self.location,
                'cuisine_type': self.cuisine_type
            })
        else:
            Database.update('restaurants', self.id, {
                'name': self.name,
                'location': self.location,
                'cuisine_type': self.cuisine_type
            })

    @classmethod
    def delete(cls, restaurant_id):
        Database.delete('restaurants', restaurant_id)

    @classmethod
    def get_all(cls):
        return Database.select_all('restaurants')

    @classmethod
    def find_by_id(cls, restaurant_id):
        return Database.select_one('restaurants', restaurant_id)

    def get_orders(self):
        return Database.select_where('orders', 'restaurant_id', self.id)
