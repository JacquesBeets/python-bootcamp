cat =  {
   "name": "Bol", 
   "age": 10, 
   "isVeryCute": True
   }

cat2 = dict(name="Simba", age=8, cute=True)

# print(cat["name"])

# =================================
# ITERATING DICTIONARIES WITH LOOPS
# =================================

# for value in cat2.values():
#   print(value)

# for key in cat2.keys():
#   print(key)

# for key, value in cat2.items():
#   print(F"{key}: {value}")

# =================================
# EXCERSIZE
# =================================

# donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5, stan=150.0, lisa=50.25, harrison=10.0)
# total_donations = 0

# for value in donations.values():
#   total_donations += value 

# print(total_donations)

# ===================================================
# ITERATING DICTIONARIES WITH LOOPS TESTING WITH "IN"
# ===================================================

# print("name" in cat2) #tests if there is a key with "name" and retun boolean in that dictionary
# print("Bol" in cat.values) #tests if there is a value with "bol" and retun boolean in that dictionary

# =================================
# DICTIONARY METHODS
# =================================

# cat.clear() # clears dictionary
# print(cat)

# cat_copy = cat.copy()
# print(cat_copy)

# new_user = {}.fromkeys(['name', 'score', 'email', 'profile bio'], 'unknown')
# print(new_user)

# .get
# print(cat.get('name')) # when using this method it will not throw an error if it does no exist as with cat['name']

# =================================
# EXCERSIZES
# =================================

# from random import choice
# food = choice(["cheese pizza", "quiche","morning bun","gummy bear","tea cake"])

# bakery_stock = {
#     "almond croissant" : 12,
#     "toffee cookie": 3,
#     "morning bun": 1,
#     "chocolate chunk cookie": 9,
#     "tea cake": 25
# }

# if food in bakery_stock:
#   print(str(bakery_stock[food]) + " left")
# else:
#   print("We don't make that")

# EXCERSIZE 2
# game_properties = ["current_score", "high_score", "number_of_lives", "items_in_inventory", "power_ups", "ammo", "enemies_on_screen", "enemy_kills", "enemy_kill_streaks", "minutes_played", "notications", "achievements"] 

# initial_game_state = {}.fromkeys(game_properties, 0)
# print(initial_game_state)

# =================================
# DICTIONARY METHODS - PART 2
# =================================

# cat.pop("age") # Removes the key value pair
# print(cat)

# cat.popitem() #removes item randomly from dictionary
# print(cat)

# cat3 = {"city": 'Pretoria'}
# cat3.update(cat) # adds all values from both cat and cat3 into cat3
# print(cat3)

# =================================
# EXCERSIZES
# =================================

# inventory = {'croissant': 19, 'bagel': 4, 'muffin': 8, 'cake': 1}


# stock_list = update(inventory)
# stock_list.update({"cookie": 18})
# stock_list.pop('cake')
# print(stock_list)

# # Another Way
# stock_list = inventory.copy()
# stock_list['cookie'] = 18
# stock_list.pop('cake')