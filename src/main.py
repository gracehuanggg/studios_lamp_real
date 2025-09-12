from restaurant import Restaurant

DATA_FILE_PATH = '../data/restaurant_data.json'


def print_menu_items(items):#print a list of menu items
    if not items:
        print("No items to display.")
        return

    print("\n---------- Menu ----------")
    for item in items:
        status = "In Stock" if item.in_stock else "Out of Stock"
        print(
            f"ID: {item.id:<3} | Name: {item.name:<28} | Category: {item.category:<12} | Price: ${item.price:.2f} | Status: {status}")
    print("--------------------------\n")

def main():
    # Create an instance of the Restaurant class. This object will manage everything.
    my_restaurant = Restaurant(DATA_FILE_PATH)

    while True:
        print("\n======= Restaurant Management System =======")
        print("  1. View Menu")
        print("  2. Search Menu")
        print("  3. Add New Item")
        print("  4. Update Item")
        print("  5. Delete Item")
        print("  0. Exit and Save")
        print("========================================")

        choice = input("Enter your choice (0-5): ")

        if choice == '1':
            print_menu_items(my_restaurant.menu)

        elif choice == '2':
            handle_search_menu(my_restaurant)

        elif choice == '3':
            try:
                name = input("Enter item name: ")
                category = input("Enter item category: ")
                price = float(input("Enter item price: "))
                if not name or not category:
                    raise ValueError("Name and category cannot be empty.")

                added_item = my_restaurant.add_item(name, category, price)
                print(f"Successfully added '{added_item.name}' with ID {added_item.id}.")
            except ValueError as e:
                print(f"Invalid input: {e}")

        elif choice == '4':
            try:
                item_id = int(input("Enter the ID of the item to update: "))
                item = my_restaurant.find_item_by_id(item_id)

                if not item:
                    print("Item not found.")
                    continue

                print(f"Updating item: {item.name}. Press Enter to skip.")
                new_data = {}

                new_name = input(f"New name (current: {item.name}): ")
                if new_name: new_data['name'] = new_name

                new_category = input(f"New category (current: {item.category}): ")
                if new_category: new_data['category'] = new_category

                new_price_str = input(f"New price (current: {item.price}): ")
                if new_price_str: new_data['price'] = float(new_price_str)

                my_restaurant.update_item(item_id, new_data)
                print("Item updated successfully.")

            except ValueError:
                print("Invalid input: ID and price must be numbers.")

        elif choice == '5':
            try:
                item_id = int(input("Enter the ID of the item to delete: "))
                if my_restaurant.delete_item(item_id):
                    print(f"Item with ID {item_id} has been deleted.")
                else:
                    print(f"Item with ID {item_id} not found.")
            except ValueError:
                print("Invalid input: ID must be a number.")

        elif choice == '0':
            my_restaurant.save_menu()
            print("Data saved. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 0 and 5.")


if __name__ == "__main__":
    main()