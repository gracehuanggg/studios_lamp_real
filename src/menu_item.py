class MenuItem:
    def __init__(self, id: str, name: str, price: float, in_stock: bool = True):
        self.id = id
        self.name = name
        self.price = float(price)
        self.in_stock = bool(in_stock)

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "in_stock": self.in_stock,
        }

    def from_dict(d: dict) -> "MenuItem":
        return MenuItem(
            id=d["id"],
            name=d["name"],
            price=float(d["price"]),
            in_stock=bool(d.get("in_stock", True)),
        )
    
class OptionsMenu:
    def __init__(self):
        pass

    def handle_options(self, restaurant_data: dict):

        while True:
            print("\n--- Restaurant Menu Options ---")
            print("1. Show all menu items")
            print("2. Add a new menu item")
            print("3. Remove a menu item")
            print("4. Toggle in-stock status")
            print("5. Exit")

            choice = input("Enter option: ").strip()

            if choice == "1":
                self.show_menu(restaurant_data)
            elif choice == "2":
                self.add_item(restaurant_data)
            elif choice == "3":
                self.remove_item(restaurant_data)
            elif choice == "4":
                self.toggle_stock(restaurant_data)
            elif choice == "5":
                print("Exiting options menu.")
                break
            else:
                print("Invalid choice. Try again.")