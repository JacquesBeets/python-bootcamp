# ======================================
# BUILT-IN FUNCTIONS
# ======================================


# ======================================
# all()
# ======================================

# Return True if all elements of the iterable are truthy (or if the iterable is empty)

all([0,1,2,3]) # False

all([char for char in 'eio' if char in 'aeiou'])

all([num for num in [4,2,10,6,8] if num % 2 == 0]) # True

# ======================================
# any()
# ======================================

# Return True if any element of the iterable is truthy. If the iterable is empty, return False.

any([0, 1, 2, 3]) # True

any([val for val in [1,2,3] if val > 2]) # True

any([val for val in [1,2,3] if val > 5]) # False

# ======================================
# EXCERSIZES
# ======================================

def is_all_strings(li):
    return all(type(l) == str for l in li)

# ======================================
# sorted()
# ======================================

# Returns a new sorted list from the items in iterable - Can accepst tuple or a list

# sorted (works on anything that is iterable)

more_numbers = [6,1,8,2]
sorted(more_numbers) # [1, 2, 6, 8]
sorted(more_numbers, reverse=True) # [1, 2, 6, 8]
#print(more_numbers) # [6, 1, 8, 2]


users = [
	{"username": "samuel", "tweets": ["I love cake", "I love pie", "hello world!"]},
	{"username": "katie", "tweets": ["I love my cat"]},
	{"username": "jeff", "tweets": []},
	{"username": "bob123", "tweets": []},
	{"username": "doggo_luvr", "tweets": ["dogs are the best", "I'm hungry"]},
	{"username": "guitar_gal", "tweets": []}
]

sorted(users, key=lambda user: user['username']) #sorts by username alphabetically
sorted(users, key=lambda user: len(user['tweets'])) #sorts by most tweets
# Return a reverse iterator.

more_numbers = [6, 1, 8, 2]
reversed(more_numbers) # <list_reverseiterator at 0x1049f7da0>
#print(list(reversed(more_numbers))) # [2, 8, 1, 6]


# ======================================
# min() & max()
# ======================================

# Return the largest item in an iterable or the largest of two or more arguments.

# max (strings, dicts with same keys)

max([3,4,1,2]) # 4
max((1,2,3,4)) # 4
max('awesome') # 'w'
max({1:'a', 3:'c', 2:'b'}) # 3

# Return the smallest item in an iterable or the smallest of two or more arguments.

# min (strings, dicts with same keys)

min([3,4,1,2]) # 1
min((1,2,3,4)) # 1
min('awesome') # 'a'
min({1:'a', 3:'c', 2:'b'}) # 1


# ======================================
# EXCERSIZES
# ======================================

def extremes(li):
  mi = min(li)
  ma = max(li)
  return (mi, ma)

# EASIER WAY
def extremes(nums):
    return(min(nums), max(nums))

# ======================================
# reversed()
# ======================================

# reverse string or items but returns a iterable object/list

for char in reversed("Hello World"):
  print(char)

# ======================================
# abs(), sum(), round() - MATHY
# ======================================

#abs()
# Return the absolute value of a number. The argument may be an integer or a floating point number.'

abs(-5) # 5
abs(5)  # 5
abs(3.4444) #3.4444



#sum()
# Takes an iterable and an optional start.
# Returns the sum of start and the items of an iterable from left to right and returns the total.
# start defaults to 0

sum([1,2,3,4]) # 10
sum([1,2,3,4], -10) # 0


#round()
# Return number rounded to ndigits precision after the decimal point. If ndigits is omitted or is None, it returns the nearest integer to its input.

round(10.2) # 10
round(1.212121, 2) # 1.21

# ======================================
# EXCERSIZES
# ======================================

def max_magnitude(nums):
    return max(abs(num) for num in nums)

#print(max_magnitude([300,20,900]))


def sum_even_values(*args):
    return sum(arg for arg in args if arg % 2 == 0)
  
# sum_even_values(1,2,3,4,5,6) # 12
# sum_even_values(4,2,1,10) # 16
# sum_even_values(1) # 0


def sum_floats(*args):
    return sum(arg for arg in args if type(arg) == float)

# sum_floats(1.5, 2.4, 'awesome', [], 1) # 3.9
# sum_floats(1,2,3,4,5) # 0

# ======================================
# zip()
# ======================================

# Make an iterator that aggregates elements from each of the iterables.

# Returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the argument sequences or iterables.

# The iterator stops when the shortest input iterable is exhausted.

first_zip = zip([1,2,3], [4,5,6])

list(first_zip) # [(1, 4), (2, 5), (3, 6)]

dict(first_zip) # {1: 4, 2: 5, 3: 6}

five_by_two = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]

list(zip(*five_by_two))

#[(0, 1, 2, 3, 4), (1, 2, 3, 4, 5)]