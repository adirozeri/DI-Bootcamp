import json

class MenuManager:
        def __init__(self):
            self.json_file = 'C:\DI_Bootcamp\Week3\day4\restaurant_menu.json'
            with open(self.json_file, 'r') as file:
                self.menu = json.load(file) 
            
        
        def add_item(self, name, price):
            self.menu['items'].append({"name": name, "price": price})
        
        def remove_item(self, name):
             for item in self.menu['items']:
                  if item['name'] == name:
                       self.menu['items'].remove(item)

        def save_to_file(self):
            with open(self.json_file, 'w') as file_obj:
                json.dump(self.menu, file_obj, indent = 2, sort_keys=True)
                