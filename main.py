import random
menu = {}
print("welcome to uor app")
while True:
    print('__'*20)
    print('1 - add a menu item')
    print('2 - search a menu item')
    print('3 - delete a menu item')
    print('4 - list all menu item')
    print('5 - place an order')
    print('6 - view order')
    print('7 - exit')
    choice = input('enter your choice')
    if choice == '1':

        capp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        small = 'abcdefghijklmnopqrstuvwxyz'
        num = '0123456789'

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

        def addMenuItem():
            name = input('enter the name of the menu item: ')

            description = input('enter the description of the item: ')
            
            while True:
                try:
                    price = float(input('enter the price of the item: '))
                    break
                except ValueError:
                    print('invalid input. please enter a valid price.')

            unique_id = uniqueId()
            
            menu_item = {
                'name': name,
                'description': description,
                'price': price
            }
            menu[unique_id] = menu_item

        addMenuItem()
        print(menu)
                    

        
    elif choice == '2':


        nameSearch = input("Enter the name of the menu item: ")
        isExisted = False
        for i in menu:
            if nameSearch == menu[i]['name']:
                isExisted = True
                print('the search result for ',nameSearch, ':')
                print('_'*20)
                print(f"id: {i} ")
                print(f"name: {menu[i]['name']}")
                print(f"description: {menu[i]['description']}")
                print(f"price: {menu[i]['price']}")


        if isExisted:
            print(menu[i])
        else:
            print('this item is not existed')

        
    elif choice == '3':
        while True:
             print('__'*20)
             print('1 - delete 1 item')
             print('2 - delete all item')
             choice = input('enter your choice')
             if choice == '1':
                 itemId = input('enter the id of the menu item to delete: ')
                 if itemId in menu:
                     del menu[itemId]
                     print('deleted successflly.')
                 else:
                     print('item id not found.')

             elif choice == '2':
                 if not menu:
                     print('menu is already empty.')
                 else:
                     menu.clear()
                     print('all menu item deleted successflly.')
                 
                 
                 
        
    elif choice == '4':
        if not menu:
            print('menu items is already empty.')
        else:
            print('list of all menu items:')
            for itemId, itemDetails in menu.items():
                print('_'*20)
                print(f"iD: {itemId}")
                print(f"name: {itemDetails['name']}")
                print(f"description: {itemDetails['description']}")
                print(f"price: {itemDetails['price']}")
        


    elif choice == '5':
        if not menu:
            print('The menu is empty. Cannot place an order.')
        else:
            customerName = input('Enter your name: ')
            phoneNumber = input('Enter your phone number: ')

        # Ask for the number of items the customer wants to order
        while True:
            try:
                numOrders = int(input('Enter the number of items you want to order: '))
                if numOrders > 0:
                    break
                else:
                    print('Please enter a valid number greater than 0.')
            except ValueError:
                print('Invalid input. Please enter a valid number.')

        orderItems = []
        for _ in range(numOrders):
            itemId = input('Enter the ID of the item: ')

            if itemId in menu:
                orderItems.append({
                    'id': itemId,
                    'name': menu[itemId]['name'],
                    'price': menu[itemId]['price']
                })
                print(f'{menu[itemId]["name"]} added to your order.')
            else:
                print(f'Item with ID {itemId} not found in the menu.')

        if orderItems:
            order = {
                'customer name': customerName,
                'phone number': phoneNumber,
                'items': orderItems
            }
            print('Order placed successfully!')
        else:
            print('No items added to the order.')
    

    elif choice == '6':
        pass
    elif choice == '7':
        pass
    else:
        print('wrong choice')





























