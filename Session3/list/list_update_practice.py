menu = ['com', 'bun', 'pho', 'nem']

print('I want to change a dish in the menu')
print('We have', len(menu), 'dishes in the menu')
update_pos = int(input("Which position? "))
update_item = input("Which dish do u want to add? ")

menu[update_pos-1] = update_item
print(menu)
