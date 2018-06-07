# =============================
# TUPLES
# =============================

# Tuples once defined can not be changed or values deleted
# Can not add values to tuples
# Faster than list
# Good For protecting Data

alphabet = ('a', 'b', 'c', 'd')
# print(alphabet)
# print(type(alphabet))

names = ('Jacques', 'Bol', 'Mia', 'Simba', 'Google')

# for name in names:
#   print(name)

# i = len(names) - 1

# while i >= 0: #prints backwards
#   print(names[i])
#   i -= 1

# =============================
# TUPLES METHODS
# =============================

x = (1,2,3,4,5,6,7,5,5,5,7,3,3,3,3)

# print(x.count(3)) #counts how many time the number 3 occurs in tuple x
# print(names.index('Mia')) #return the index of the value specified


# =============================
# SETS
# =============================

# Does not have duplicate values  (all unique values)
# Elements in side a set are not ordered

alphabet_set = set({'a', 'b', 'c', 'd'})

# print(alphabet_set)
# print('b' in alphabet_set) #check if a value exists in a set
# print('e' in alphabet_set) #check if a value exists in a set

# for v in alphabet_set:
#   print(v)


# =============================
# SETS METHODS
# =============================

# alphabet_set.add('e')
# print(alphabet_set)
# alphabet_set.remove('a')
# alphabet_set.discard('a') #will remove but will not throw error if value does not exist in set
# print(alphabet_set)

# alphabet_set_copy = alphabet_set.copy()
# print(alphabet_set_copy)
# alphabet_set_copy.clear()
# print(alphabet_set_copy)


# =============================
# SETS MATH
# =============================

math_students = {"Wilhelmine", "Aaron", "Aurore", "Shea", "Noe", "Roger", "Estefania", "Mathilde", "Danial", "Zelma"}
biology_students = {"Shea", "Noe", "Danial", "Zelma", "Henri", "Dillan", "Dax", "Jaclyn", "Hershel"}

#Union
# print(math_students | biology_students) #gives you a complete set without the duplicates

# print(math_students & biology_students) #gives you a set of names that exists in both sets


# =============================
# EXCERCISZES
# =============================

# values = [10,20,30]

# static_value = tuple(values)
# print(static_value)

# stuff = [1,3,1,5,2,5,1,2,5]
# unique_stuff = set(stuff)
# print(unique_stuff)

# =============================
# SET COMPREHENSION
# =============================

print({x**2 for x in range(10)})
print({char.upper() for char in 'hello'})