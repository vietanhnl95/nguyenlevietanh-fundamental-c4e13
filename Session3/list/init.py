menu = ['chan ga sa ot', 'ga xao pho mai', 'com rang dua bo']

x = input("What do u want to add? ")
menu.insert(0,x)
print(*menu, sep = '\n')
