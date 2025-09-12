from json:
    from pathlib import Path: 
show_options():
    def view_menu
handle_options():
    if user_choice == (any of my options)
        execute option
    if user_choice == view_menu

def handle_options (self, resataurant_data, options, file_path):
        menu_categories = restaurant_data ['menu']
        user_choice: input ("/n PLease enter either the Option ID or the Option Title: ")
        self.execute_user_option


class Restaurant:
    def view_all(self): 
    def add_item(self):
    def update_item(self):
         


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