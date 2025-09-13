import json
from menu_item import MenuItem


class Restaurant: #Manages the collection of menu items and handles data persistence.
    def __init__(self, filepath):
        self.filepath = filepath
        # The menu is now a list of MenuItem objects, not dictionaries.
        self.menu = self._load_menu()

    def _load_menu(self): #Loads the menu from a JSON file and converts each item into a MenuItem object.
        try:
            with open(self.filepath, 'r') as file:
                data = json.load(file)  # data is a list of dictionaries
                # Use a list comprehension and the from_dict classmethod for a clean conversion
                return [MenuItem.from_dict(item_dict) for item_dict in data]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_menu(self): #Saves the current menu (list of objects) back to the JSON file.
        # Convert each MenuItem object back to a dictionary before saving
        data_to_save = [item.to_dict() for item in self.menu]
        with open(self.filepath, 'w') as file:
            json.dump(data_to_save, file, indent=4)

    def add_item(self, name, category, price): #
        if self.menu:
            new_id = max(item.id for item in self.menu) + 1
        else:
            new_id = 1

        new_item = MenuItem(id=new_id, name=name, category=category, price=price)
        self.menu.append(new_item)
        return new_item
    
    def add_item(self, name, category, price): #
        if self.menu:
            new_id = max(item.id for item in self.menu) + 1
        else:
            new_id = 1

        new_item = MenuItem(id=new_id, name=name, category=category, price=price)
        self.menu.append(new_item)
        return new_item

    def find_item_by_id(self, item_id):#Finds and returns a MenuItem object by its ID.
        for item in self.menu:
            if item.id == item_id:
                return item
        return None

    def search_items(self, term, search_by='name'):#Searches for items by name or category.
        term = term.lower()
        results = []
        for item in self.menu:
            if search_by == 'name' and term in item.name.lower():
                results.append(item)
            elif search_by == 'category' and term in item.category.lower():
                results.append(item)
        return results

    def update_item(self, item_id, new_data): #Updates an existing MenuItem object's attributes.
        item_to_update = self.find_item_by_id(item_id)
        if item_to_update:
            if new_data.get('name'):
                item_to_update.name = new_data['name']
            if new_data.get('category'):
                item_to_update.category = new_data['category']
            if new_data.get('price') is not None:
                item_to_update.price = float(new_data['price'])
            return True
        return False

    def delete_item(self, item_id): #Deletes a MenuItem object from the menu by its ID.
        item_to_delete = self.find_item_by_id(item_id)
        if item_to_delete:
            self.menu.remove(item_to_delete)
            return True
        return False