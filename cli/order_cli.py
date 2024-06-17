from models.order import Order

def create_order():
    restaurant_id = int(input("Enter restaurant ID: "))
    customer_name = input("Enter customer name: ")
    items = input("Enter order items: ")
    total_price = float(input("Enter total price: "))
    status = input("Enter order status (default is Pending): ") or 'Pending'

    order = Order(restaurant_id, customer_name, items, total_price, status)
    order.save()
    print("Order created successfully.")

def delete_order():
    order_id = int(input("Enter order ID to delete: "))
    order = Order.find_by_id(order_id)
    if order:
        order.delete()
        print("Order deleted successfully.")
    else:
        print("Order not found.")

def view_all_orders():
    orders = Order.get_all()
    if orders:
        for order in orders:
            print(order.__dict__)  
    else:
        print("No orders found.")

def find_order_by_id():
    order_id = int(input("Enter order ID: "))
    order = Order.find_by_id(order_id)
    if order:
        print(order.__dict__)
    else:
        print("Order not found.")

def update_order_status():
    order_id = int(input("Enter order ID to update: "))
    order = Order.find_by_id(order_id)
    if order:
        new_status = input("Enter new status: ")
        order.update_status(new_status)
        print("Order status updated successfully.")
    else:
        print("Order not found.")

def main():
    while True:
        print("\n=== Order Management Menu ===")
        print("1. Create Order")
        print("2. Delete Order")
        print("3. View All Orders")
        print("4. Find Order by ID")
        print("5. Update Order Status")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

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
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
