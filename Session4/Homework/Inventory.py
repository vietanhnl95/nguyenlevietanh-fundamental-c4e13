inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}
inventory['key'] = ['seashell', 'strange berry', 'lint']
inventory['backpack'].remove('dagger')
inventory['gold'] += 50
print("INVENTORY: ")
print("-" * 10)
for i in inventory:
    print("{0}: {1}".format(i, inventory[i]))
