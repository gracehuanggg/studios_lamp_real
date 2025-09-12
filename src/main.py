import json
import time
from menu_item import MenuItem
from restaurant import load_data

FILE_PATH = "../data/restaurant_data.json"



def view_menu(menu):
    print("--- Menu ---")
    if not menu:
        print("No dishes yet.")
    else:
        for dish in menu:
            print(f"{dish['id']}: {dish['name']} - ${dish['price']}")

def add_item(menu):
    name = input("Dish name: ")
    price = float(input("Price: "))
    next_id = 0
    for d in menu:
        if d["id"] > next_id:
            next_id = d["id"]
    next_id += 1
    menu.append({"id": next_id, "name": name, "price": price})
    print(f"Added {name} with ID {next_id}.")

def update_item(menu):
    target = int(input("ID to update: "))
    for d in menu:
        if d["id"] == target:
            new_name = input("New name (blank to keep): ")
            new_price = input("New price (blank to keep): ")
            if new_name != "":
                d["name"] = new_name
            if new_price != "":
                d["price"] = float(new_price)
            print(f"Dish ID {target} updated.")
            return
    print("Dish not found.")

def delete_item(menu):
    target = int(input("You want to delete which dish ID? "))
    for i in range(len(menu)):
        if menu[i]["id"] == target:
            removed = menu[i]["name"]
            del menu[i]
            print(f"Deleted {removed} (ID {target}).")
            return
    print("Dish not found.")

def main():
    menu = load_data(FILE_PATH)
    while True:
        print("1. View menu")
        print("2. Add dish")
        print("3. Update dish")
        print("4. Delete dish")
        print("5. Save changes")
        print("0. Exit")
        choice = input("Choose: ")
        if choice == "1":
            view_menu(menu)
        elif choice == "2":
            add_item(menu)
        elif choice == "3":
            update_item(menu)
        elif choice == "4":
            delete_item(menu)
        elif choice == "5":
            save_data(FILE_PATH, menu)
            print("Changes saved.")
        elif choice == "0":
            save_data(FILE_PATH, menu)
            print("Goodbye. All changes saved.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()