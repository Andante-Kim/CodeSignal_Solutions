# Grocery list
grocery_list = set()

# Adding items
grocery_list.add('Milk')
grocery_list.add('Cheese')
grocery_list.add('Bread')

# Checking existence
print('Milk' in grocery_list)  # Outputs: True
print('Butter' in grocery_list)  # Outputs: False

# Add a new item
grocery_list.add('Butter')
print('Butter' in grocery_list)  # Outputs: True

# Try removing an item
grocery_list.remove('Bread')
print('Bread' in grocery_list)  # Outputs: False
