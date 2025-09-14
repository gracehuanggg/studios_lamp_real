# Restaurant Menu Management System

## Project Description

This is a command-line menu management application designed for the "Miga House" restaurant. It allows the user to conveniently view, search, add, update, and delete menu items through simple menu options. All data is saved to a JSON file to ensure data persistence.

This project was completed as a collaborative course assignment, aimed at practicing programming in python, using JSON files/data structure,and teamwork skills.

## Key Features

* **View Full Menu**: Displays all items on the menu in a clear, formatted list.
* **View Menu by Category**: Groups and displays items by their category, such as "Appetizer" or "Entree".
* **Search Items**: Allows for fuzzy searching of menu items by either **name** or **category** or **ID**.
* **Add New Item**: Adds a new dish to the menu, and the program automatically assigns a unique ID.
* **Update Item Information**: Modifies the name, category, or price of an existing item.
* **Delete Item**: Removes a specified item from the menu.
* **Exit and Auto-Save**: When exiting the program, all changes are automatically saved to the `restaurant.json` file.

## Project Structure

Our project follows a clean, multi-file layout with each part serving a clear purpose:

```
|-- restaurant_manager/
|   |-- data/
|   |   |-- restaurant.json     # The JSON file that stores all menu item data
|   |
|   |-- src/
|       |-- main.py             # Main entry point, handles user interaction and menu display
|       |-- restaurant.py       # Core logic, defines the Restaurant class for menu management
|       |-- menu_item.py        # Data model, defines the MenuItem class for a single dish
|
|   |-- README.md                # The file you are reading right now :)
```
## How to Run

1.  Ensure you have a Python environment installed on your computer.
2.  Open the entire `restaurant_manager` project folder in a code editor like VSCode.
3.  Locate and run the `src/main.py` file directly (usually by clicking the "Run" button in the editor).
4.  Follow the menu options displayed in the terminal or console window below to operate the application.

## Examples
```text
======= Restaurant Management System =======
1. View Menu (All Items)
2. View Menu by Category
3. Search Menu
4. Add New Item
5. Update Item
6. Delete Item
0. Exit and Save
===========================================

Enter your choice (0–6): 4
Enter item name: Korean BBQ Wings
Enter item category: Entree
Enter item price: 16.99
Successfully added 'Korean BBQ Wings' with ID 24.

===========================================

Enter your choice (0–6): 5
Enter the ID of the item to update: 1
Updating item: Kimchi Pancake. Press Enter to skip.
New name (current: Kimchi Pancake): Kimchi Fried Rice
New category (current: Appetizer): Entree
New price (current: 5.99): 16.99
Item updated successfully.

## Team Collaboration and Roles

This project was completed through the collaboration of two students: Grace and Mia. We efficiently completed the project through clear role assignments and timely communication.

* **Grace (Partner A - Backend Architect)**
    * Owner of the branch `main`
    * Mia and Grace designed and wrote the `main.py` file, responsible for calling the backend functions created by Grace to display data to the user, ensuring the application is both user-friendly and stable.
* Grace also wrote the `Restaurant` class in the `restaurant.py` file, implementing all backend functionalities, including loading/saving the JSON file, and adding, deleting, updating, and searching for items.

* **Mia (Partner B - User Experience Officer)**
   * Owner of the branch `Mia`
* Responsible for the project's user interface and interaction flow. Mia and Grace designed and wrote the main.py file, creating the main menu and all the prompts that the user sees. 
* Responsible for the project's core data structure and logic. Mia wrote the menu_item.py file, defining the data model for a single menu item.
