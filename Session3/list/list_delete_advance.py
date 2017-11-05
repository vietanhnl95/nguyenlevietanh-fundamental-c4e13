menu = ['bun bo', 'bun ca', 'pho bo', 'pho ga']
print(menu)
menu_2 = list(menu)
print(menu_2)

import ratio
menu_del = input("What do u want to remove from menu? ")
for i in range(len(menu)):
    if (menu_del, menu[i]).ratio() > 0.1:
        menu.remove(menu_del)
        print("new menu: ", menu)
    else:
        print("we dont have that dish in the menu.")
