import json
from menu_item import MenuItem


class Restaurant: #Manages the collection of menu items and handles data persistence.
    def __init__(self, filepath):
        self.filepath = filepath
        # Store restaurant info and original data structure
        self.restaurant_info = {}
        self.original_format = 'simple'  # 'simple' or 'nested'
        # The menu is now a list of MenuItem objects, not dictionaries.
        self.menu = self.load_menu()

    def load_menu(self): #Loads the menu from a JSON file and converts each item into a MenuItem object.
        try:
            with open(self.filepath, 'r') as file:
                data = json.load(file)

                # Check if data is a simple list (old format) or nested structure (new format)
                if isinstance(data, list):
                    # Old format: data is a list of dictionaries
                    self.original_format = 'simple'
                    return [MenuItem.from_dict(item_dict) for item_dict in data]
                elif isinstance(data, dict) and 'menu' in data:
                    # New format: data is a dictionary with nested menu structure
                    self.original_format = 'nested'
                    # Store restaurant info
                    self.restaurant_info = {
                        'name': data.get('name', ''),
                        'location': data.get('location', ''),
                        'cusine': data.get('cusine', '')
                    }

                    menu_items = []
                    for category_group in data['menu']:
                        if 'items' in category_group:
                            for item_dict in category_group['items']:
                                # Add category to item_dict if not present
                                if 'category' not in item_dict:
                                    item_dict['category'] = category_group['category']
                                menu_items.append(MenuItem.from_dict(item_dict))
                    return menu_items
                else:
                    return []
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_menu(self): #Saves the current menu (list of objects) back to the JSON file.
        if self.original_format == 'simple':
            # Save in simple list format
            data_to_save = [item.to_dict() for item in self.menu]
        else:
            # Save in nested format
            # Group items by category
            categories = {}
            for item in self.menu:
                if item.category not in categories:
                    categories[item.category] = []
                categories[item.category].append(item.to_dict())

            # Create the nested structure
            menu_structure = []
            category_id = 1
            for category_name, items in categories.items():
                menu_structure.append({
                    "category": category_name,
                    "id": category_id,
                    "items": items
                })
                category_id += 1

            data_to_save = {
                "name": self.restaurant_info.get('name', ''),
                "location": self.restaurant_info.get('location', ''),
                "cusine": self.restaurant_info.get('cusine', ''),
                "menu": menu_structure
            }

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
