item_list = ['T-Shirt', 'Sweater', 'Jeans']
user_choice = list("CRUD")
print("Welcome to our shop")

while True:
    user_command = input("What do you want (C, R, U, D)? ")
    if user_command.upper() not in (user_choice):
        print("Wrong input! Please type C to create item, type R to Read items, type U to Update item or type D to Delete item")

    if user_command.upper() in (user_choice):
        user_command = user_command.upper()
        if user_command == 'C':
            user_c = input("Enter new item: ")
            item_list.append(user_c)
            print("New item list:",item_list)
        elif user_command == 'R':
            print("Current item list:",item_list)
        elif user_command == 'U':
            update_pos = int(input("Update position? "))
            if 0 <= update_pos and update_pos <= len(item_list):
                update_item = input("New item? ")
                item_list[update_pos - 1] = update_item
                print("Item list after update:",item_list)
            else:
                print("We do not have that many item")
        elif user_command == 'D':
            delete_pos = int(input("Delete position? "))
            if 0 < delete_pos and delete_pos <= len(item_list):
                item_list.remove(item_list[delete_pos - 1])
                print("Item list after delete:",item_list)
            else:
                print("We do not have that many item")
    user_command_2 = input("Anything else (Yes or no)? ")
    if user_command_2.lower() in ['yes', 'of course', 'ok']:
        print("OK")
    else:
        print("I got it. See you later.")
        break
