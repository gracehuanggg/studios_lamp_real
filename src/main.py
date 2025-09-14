from restaurant import Restaurant

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # findpath to help run in Visual Studio Code properly
DATA_FILE_PATH = os.path.join(BASE_DIR, '..', 'data', 'restaurant_data.json')


def print_menu_items(items):#print a list of menu items
    if not items:
        print("No items to display.")
        return

    print("\n---------- Menu ----------")
    for item in items:
        if item.in_stock:
            status = "In Stock"
        else:
            status = "Out of Stock"
        print(f"ID: {item.id} | Name: {item.name} | Category: {item.category} | Price: ${item.price} | Status: {status}")
    print("--------------------------\n")


def print_menu_by_category(restaurant_obj):#print menu items grouped by category
    if not restaurant_obj.menu:
        print("No items to display.")
        return

    print("\n========== Menu by Category ==========")

    # Get all unique categories
    categories = list(set(item.category for item in restaurant_obj.menu))
    categories.sort()  # Sort categories alphabetically

    # Display items for each category
    for category in categories:
        print(f"\n--- {category} ---")
        for item in restaurant_obj.menu:
            if item.category == category:
                if item.in_stock:
                    status = "In Stock"
                else:
                    status = "Out of Stock"
                print(f"  ID: {item.id} | {item.name} | ${item.price} | {status}")

    print("\n====================================\n")


def handle_search_menu(restaurant_obj):  #Handles the user interaction for searching menu items.
    print("\n--- Search Menu ---")
    print("Search by: 1. Name  2. Category")
    choice = input("Enter your choice: ")

    if choice not in ['1', '2']:
        print("Invalid choice.")
        return

    term = input("Enter search term: ")
    search_by = 'name' if choice == '1' else 'category'

    results = restaurant_obj.search_items(term, search_by)

    if results:
        print(f"\nFound {len(results)} item(s):")
        print_menu_items(results)
    else:
        print("No items found matching your search.")


def main():
    # Create an instance of the Restaurant class. This object will manage everything.
    my_restaurant = Restaurant(DATA_FILE_PATH)
    print(f"Loaded {len(my_restaurant.menu)} items from file")

    while True:
        print("\n======= Restaurant Management System =======")
        print("  1. View Menu (All Items)")
        print("  2. View Menu by Category")
        print("  3. Search Menu")
        print("  4. Add New Item")
        print("  5. Update Item")
        print("  6. Delete Item")
        print("  0. Exit and Save")
        print("========================================")

        choice = input("Enter your choice (0-6): ")

        if choice == '1':
            print_menu_items(my_restaurant.menu)

        elif choice == '2':
            print_menu_by_category(my_restaurant)

        elif choice == '3':
            handle_search_menu(my_restaurant)

        elif choice == '4':
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

        elif choice == '5':
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

        elif choice == '6':
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
            print("Invalid choice. Please enter a number between 0 and 6.")


if __name__ == "__main__":
    main()
