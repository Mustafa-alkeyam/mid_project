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
            name = input("Enter the name of the menu item: ")

            description = input("Enter the description of the item: ")
            
            while True:
                try:
                    price = float(input("Enter the price of the item: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid price.")

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
                # print(f"unique Id:{unique_id} ")
                print(f"name: {menu[i]['name']}")
                print(f"description: {menu[i]['description']}")
                print(f"price: {menu[i]['price']}")


        if isExisted:
            print(menu[i])
        else:
            print('this item is not existed')

        
    elif choice == '3':
        pass
    elif choice == '4':
        pass
    elif choice == '5':
        pass
    elif choice == '6':
        pass
    elif choice == '7':
        pass
    else:
        print('wrong choice')





























