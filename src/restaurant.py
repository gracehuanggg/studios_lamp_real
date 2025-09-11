class Restaurant:
    def view_all(self): 


# Use multiple source files:

# Restaurant class in restaurant.py
# MenuItem class in menu_item.py
# main.py imports and uses both
# Load data from a JSON file (restaurant_data.json).

# Provide a menu for the user to choose actions.

# Implement at least five different functions:

# View all menu items
# Search for a menu item by key (id, name, or category)
# Add a new menu item
# Update an existing menu item
# Delete a menu item
# Save changes back to the JSON file
# Validate input where possible (wrong menu choices, invalid ids).

import json
from menu_item import MenuItem

class Restaurant:
    def __init__(self, name, location, cuisine, categories):
        self.name = name
        self.location = location
        self.cuisine = cuisine
        self.categories = categories