# ==========================================
# EXCERSISE 1
# ==========================================

def product(a, b):
  return a * b 

# print(product(2,-2))

# ==========================================
# EXCERSISE 2
# ==========================================


def return_day(num):
  days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
  days_dict = {day + 1:days[day] for day in range(len(days))}
  if num < 1 or num > 7:
    return None
  return days_dict[num]


# ===========
# OTHER WAYS
# ===========

def return_day(num):
    days = ["Sunday","Monday", "Tuesday","Wednesday","Thursday","Friday","Saturday"]
    # Check to see if num valid
    if num > 0 and num <= len(days):
        # use num - 1 because lists start at 0 
        return days[num-1]
    return None

  
def return_day(num): #With error handeling
    try:
        return ["Sunday","Monday", "Tuesday","Wednesday","Thursday","Friday","Saturday"][num-1]
    except IndexError as e:
        return None

# ==========================================
# EXCERSISE 3
# ==========================================

def last_element(li=None):
  if li:
    return li[-1]
  return None
  
# print(last_element())
# print(last_element([1,2,3]))
#print(last_element(list(range(3))))

# ==========================================
# EXCERSISE 4
# ==========================================

def number_compare(num1, num2):
  if num1 == num2:
    return "Numbers are equal"
  elif num1 > num2:
    return "First is greater"
  return "Second is greater"

# print(number_compare(8,6))

# ==========================================
# EXCERSISE 5
# ==========================================

def single_letter_count(a, b=0):
  return tuple(a.lower()).count(b.lower())


# print(single_letter_count("HELLO world", "L"))

# ===========
# OTHER WAYS
# ===========

def single_letter_count(string,letter):
    return string.lower().count(letter.lower())


# ==========================================
# EXCERSISE 5
# ==========================================

def multiple_letter_count(string):
  return {letter : string.count(letter) for letter in string}

# print(multiple_letter_count("awesome"))

# ===========
# OTHER WAYS
# ===========

def multiple_letter_count(word):
    return {l: word.count(l) for l in set(word)}

# ==========================================
# EXCERSISE 6
# ==========================================

def list_manipulation(li, command, location, val_input=None):
  if command == 'remove' and location == 'end':
    return li.pop(-1)
  elif command == 'remove' and location == 'beginning':
    return li.pop(0)
  elif command == 'add' and location == 'beginning':
    li.insert(0, val_input)
    return li
  elif command == 'add' and location == 'end':
    li.append(val_input)
    return li
    
# print(list_manipulation([1,2,3], "remove", "end"))
# print(list_manipulation([1,2,3], "remove", "beginning"))
# print(list_manipulation([1,2,3], "add", "beginning", 20))
# print(list_manipulation([1,2,3], "add", "end", 30))

# ==========================================
# EXCERSISE 7
# ==========================================

def is_palindrome(words):
  val = words.replace(' ', '').lower()
  val_rev = val[::-1]
  if val == val_rev:
    return True
  return False
  
#print(is_palindrome('a man a plan a canal Panama'))
# print(is_palindrome('testing'))

# ===========
# OTHER WAYS
# ===========

def is_palindrome(words):
  val = words.replace(' ', '').lower()
  val_rev = val[::-1]
  return val == val_rev

# print(is_palindrome('a man a plan a canal Panama'))
# print(is_palindrome('testing'))

# ==========================================
# EXCERSISE 7
# ==========================================

def frequency(li, search):
  return li.count(search)

# print(frequency([1,2,3,4,4,4], 4))
# print(frequency([True, False, True, True], False))


# ==========================================
# EXCERSISE 8
# ==========================================

# comprehension = [num for num in nums if num % 2 == 0] # finds all even numbers

def multiply_even_numbers(li):
  i = 1
  for val in li:
    if val % 2 == 0:
      i = i * val
  return i
  

#print(multiply_even_numbers([2,3,4,5,6]))

# ==========================================
# EXCERSISE 9
# ==========================================

def capitalize(string):
  return string.capitalize()

#print(capitalize("matt"))

# ===========
# OTHER WAYS
# ===========

def capitalize(string):
    return string[:1].upper() + string[1:]

# ==========================================
# EXCERSISE 10
# ==========================================    

def compact(li):
  return [val for val in li if val]

#print(compact([0,1,2,"",[], False, {}, None, "All done"]))

# ===========
# OTHER WAYS
# ===========

def compact(l):
    truthy_vals = []
    for val in l:
        if val: truthy_vals.append(val)
    return truthy_vals

# ==========================================
# EXCERSISE 11
# ========================================== 

def intersection(li1, li2):
  return [val for val in li1 if val in li2]
          

#print(intersection(['a','b','z'], ['x','y','z']))

# ===========
# OTHER WAYS
# ===========

#Sets Solution
def intersection(list1, list2):
    return [val for val in set(list1) & set(list2)]

#Long way
def intersection(l1, l2):
    in_common = []
    for val in l1:
        if val in l2:
            in_common.append(val)
    return in_common

# ==========================================
# EXCERSISE 12
# ========================================== 

def isEven(num): #Callback Function
    return num % 2 == 0

def partition(li, cf):  
  tr = []
  fs = []
  for val in li:
    if cf(val):
      tr.append(val)
    else: 
      fs.append(val)
  return [tr, fs]

print(partition([1,2,3,4], isEven))

# ===========
# OTHER WAYS
# ===========

#List Comprehension Version
def partition(lst, fn):
    return [[val for val in lst if fn(val)], [val for val in lst if not fn(val)]]