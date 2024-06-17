from models.restaurant import Restaurant

def create_restaurant():
    name = input("Enter restaurant name: ")
    location = input("Enter restaurant location: ")
    cuisine_type = input("Enter cuisine type: ")
    restaurant = Restaurant(name, location, cuisine_type)
    restaurant.save()
    print("Restaurant created successfully.")

def delete_restaurant():
    restaurant_id = input("Enter restaurant ID to delete: ")
    Restaurant.delete(restaurant_id)
    print("Restaurant deleted successfully.")

def view_all_restaurants():
    restaurants = Restaurant.get_all()
    for restaurant in restaurants:
        print(restaurant)

def find_restaurant_by_id():
    restaurant_id = input("Enter restaurant ID: ")
    restaurant = Restaurant.find_by_id(restaurant_id)
    print(restaurant)

def view_orders_for_restaurant():
    restaurant_id = input("Enter restaurant ID to view orders: ")
    restaurant = Restaurant.find_by_id(restaurant_id)
    if restaurant:
        orders = restaurant.get_orders()
        for order in orders:
            print(order)
    else:
        print("Restaurant not found.")
