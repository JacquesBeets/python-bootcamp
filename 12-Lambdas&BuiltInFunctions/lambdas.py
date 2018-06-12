# ======================================
# LAMBDAS
# ======================================

# LAMBDAS ARE UNNAMED FUNCTIONS
def square(num): return num * num # normal named function

square2 = lambda num: num * num
#print(square2(9))

cube = lambda num: num ** 3

#print(cube(3))

# ======================================
# map()
# ======================================

# A standard function that accepts at least two arguments, a function and an "iterable"

# iterable - something that can be iterated over (lists, strings, dictionaries, sets, tuples)

# runs the lambda for each value in the iterable and returns a map object which can be converted into another data structure

li = [1, 2, 3, 4]

doubles = list(map(lambda x: x * 2, li))

#evens # [2, 4, 6, 8]


names = [
    {'first':'Rusty', 'last': 'Steele'}, 
    {'first':'Colt', 'last': 'Steele', }, 
    {'first':'Blue', 'last': 'Steele', }
]

first_names = list(map(lambda x: x['first'], names))

first_names # ['Rusty', 'Colt', 'Blue']


# ======================================
# filter()
# ======================================

# There is a lambda for each value in the iterable.

# Returns filter object which can be converted into other iterables

# The object contains only the values that return true to the lambda

li = [1,2,3,4]

evens = list(filter(lambda x: x % 2 == 0, li))

#evens # [2,4]


# ======================================
# EXCERSIZES
# ======================================

def remove_negatives(li):
  return list(filter(lambda f: f >= 0, li))
