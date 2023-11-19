import random

print('welcome to our restaurant')
print('__'*20)
print('the menu')
print('__'*20)

capp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
small = 'abcdefghijklmnopqrstuvwxyz'
num = '0123456789'

menu = {}

def uniqueId():
    characters = capp + small + num
    unique_id = ''
    for i in range(6):
        unique_id += random.choice(characters)
    while unique_id in menu:
        unique_id = ''
        for i in range(6):
            unique_id += random.choice(characters)
    return unique_id

def addMenuItem(name, description, price):
    unique_id = uniqueId()
    
    menu_item = {
        'name': name,
        'description': description,
        'price': price
    }
    menu[unique_id] = menu_item

addMenuItem('olive salad', 'green olive slices, parsley, tomatoes, carrots', 4.75)
addMenuItem('fatoosh salad', 'purslane leaves, tomatoes, cucumbers', 4.50)
addMenuItem('mixed grill', 'char grilled selection of kabab, meat and chicken cubes', 15.00)
addMenuItem('Burger', 'Delicious beef burger', 9.99)
addMenuItem('beef shawarma', 'char grilled marinated angus beef tenderloin', 13.99)
addMenuItem('Pizza', 'Classic Margherita pizza', 12.99)


print(menu)