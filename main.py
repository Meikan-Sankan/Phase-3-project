from cli.menu import display_main_menu, display_restaurant_menu, display_order_menu
from cli.restaurant_cli import create_restaurant, delete_restaurant, view_all_restaurants, find_restaurant_by_id, view_orders_for_restaurant
from cli.order_cli import create_order, delete_order, view_all_orders, find_order_by_id, update_order_status
from db.database import Database

def main():
    Database.create_tables()
    
    while True:
        display_main_menu()
        choice = input("Select an option: ")
        
        if choice == '1':
            manage_restaurants()
        elif choice == '2':
            manage_orders()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid option, please try again.")

def manage_restaurants():
    while True:
        display_restaurant_menu()
        choice = input("Select an option: ")
        
        if choice == '1':
            create_restaurant()
        elif choice == '2':
            delete_restaurant()
        elif choice == '3':
            view_all_restaurants()
        elif choice == '4':
            find_restaurant_by_id()
        elif choice == '5':
            view_orders_for_restaurant()
        elif choice == '6':
            break
        else:
            print("Invalid option, please try again.")


def manage_orders():
    while True:
        display_order_menu()
        choice = input("Select an option: ")
        
        if choice == '1':
            create_order()
        elif choice == '2':
            delete_order()
        elif choice == '3':
            view_all_orders()
        elif choice == '4':
            find_order_by_id()
        elif choice == '5':
            update_order_status()
        elif choice == '6':
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
