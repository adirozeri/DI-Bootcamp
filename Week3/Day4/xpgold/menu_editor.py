from menu_manager import MenuManager


def load_manager():
    manger = MenuManager()
    return manger
    #- this function should create a new MenuManager instance.

def show_user_menu():
    items = self.menu['items']
    
    # - this function should display the program menu (not the restaurant menu!), 
    #and ask the user to choose an item. Call the appropriate function that matches the user’s input.

add_item_to_menu() - this will ask the user to input the item’s name and price. It will not interact with the menu itself, but simply call the appropriate function from the MenuManager object.
If the item was added successfully print a message which states: item was added successfully.

remove_item_from_menu()- this function should ask the user to input the name of the item they want to remove from the restaurant’s menu. The function should not interact with the menu itself, but simply call the appropriate function from the MenuManager object.
If the item was deleted successfully – print a message to let the user know this was completed.
If not – print a message which states that there was an error.

show_restaurant_menu() 