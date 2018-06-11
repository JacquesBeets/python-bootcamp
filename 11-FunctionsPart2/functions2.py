#===========================
# INTRODUCTIONS TO *args
#===========================

#*args gets stored in tuple

def sum_all_nums(*nums):
	total = 0
	for num in nums:
		total += num
	return total
	
# print(sum_all_nums(4,6,9,4,10))
# print(sum_all_nums(4,6))
	

def ensure_correct_info(*args):
	if "Jacques" in args and "Beets" in args:
		return "Welcome back Jacques!"
	return "Not sure who you are"

# print(ensure_correct_info("hello", False, 78)) # Not sure who you are...

# print(ensure_correct_info(1, True, "Jacques", "Beets"))

#===========================
# EXCERSIZE *args
#===========================

def contains_purple(*args):
  return  'purple' in args

# print(contains_purple('green', 'purple'))
# print(contains_purple('green', 'blue'))



#===========================
# INTRODUCTIONS TO **kwargs
#===========================

#**kwargs get stored in a dictionary with key value pairs - Key Word Arguments

def fav_colors(**kwargs):
	for person, color in kwargs.items():
		print(f"{person}'s favorite color is {color}")

# fav_colors(colt="purple", ruby="red", ethel="teal")
# fav_colors(colt="purple", ruby="red", ethel="teal", ted="blue")
# fav_colors(colt="royal deep amazing purple")


def special_greeting(**kwargs):
    if "David" in kwargs and kwargs["David"] == "special":
        return "You get a special greeting David!"
    elif "David" in kwargs:
        return f"{kwargs['David']} David!"

    return "Not sure who this is..."

#print(special_greeting(David='Hello')) # Hello David!
# print(special_greeting(Bob='hello')) # Not sure who this is...
# print(special_greeting(David='special')) # You get a special greeting David!

#print(special_greeting(Heather="hello", David="special"))


#===========================
# EXCERSIZE **kwargs
#===========================

def combine_words(name, **kwargs):
  if kwargs:
    if 'prefix' in kwargs:
      return kwargs['prefix'] + name
    return name + kwargs['suffix']
  return name
 
# print(combine_words('child', prefix='man'))
# print(combine_words('child', suffix='ish'))


#===========================
# ORDERING PARAMETERS
#===========================

# ORDER GOES AS FOLLOWS:
# 1. parameters
# 2. *args
# 3. default parameters
# 4. **kwargs


def display_info(a, b, *args, instructor="Colt", **kwargs):
  # return [a, b, args, instructor, kwargs]
  print(type(args))

# print(display_info(1, 2, 3, last_name="Steele", job="Instructor"))

# a - 1
# b - 2
# args (3)
# instructor - "Colt"
# kwargs - {'last_name': "Steele", "job": "Instructor"}

# [1, 2, (3,), 'Colt', {'last_name': 'Steele', 'job': 'Instructor'}]


#===========================
# TUPLE UNPACKING
#===========================

def sum_all_values(*args):
	print(args)
	total = 0
	for num in args:
		total += num
	print(total)

# sum_all_values(1,30,2,5,6)

#nums = [1,2,3,4,5,6]
#sum_all_values(*nums) #unpacks everything in nums variable


#===========================
# EXCERSIZE UNPACKING
#===========================

def count_sevens(*args):
    return args.count(7)

nums = [90,1,35,67,89,20,3,1,2,3,4,5,6,9,34,46,57,68,79,12,23,34,55,1,90,54,34,76,8,23,34,45,56,67,78,12,23,34,45,56,67,768,23,4,5,6,7,8,9,12,34,14,15,16,17,11,7,11,8,4,6,2,5,8,7,10,12,13,14,15,7,8,7,7,345,23,34,45,56,67,1,7,3,6,7,2,3,4,5,6,7,8,9,8,7,6,5,4,2,1,2,3,4,5,6,7,8,9,0,9,8,7,8,7,6,5,4,3,2,1,7]


# Write your code below:

# result1 = count_sevens(1,4,7)

# result2 = count_sevens(*nums)



#===========================
# DICTIONARY UNPACKING
#===========================

def display_names(first, second):
    print(f"{first} says hello to {second}")

names = {"first": "Colt", "second": "Rusty"}

#display_names(names) # will give error
#display_names(**names)  # yup!



def add_and_multiply_numbers(a,b,c,**kwargs):
    print(a + b * c)
    print("OTHER STUFF....")
    print(kwargs)

data = dict(a=1,b=2,c=3,d=55,name="Tony")

#add_and_multiply_numbers(**data) # 7

#===========================
# EXCERSIZE UNPACKING DICT
#===========================

def calculate(**kwargs):
    operation_lookup = {
        'add': kwargs.get('first', 0) + kwargs.get('second', 0),
        'subtract': kwargs.get('first', 0) - kwargs.get('second', 0),
        'divide': kwargs.get('first', 0) / kwargs.get('second', 0),
        'multiply': kwargs.get('first', 0) * kwargs.get('second', 0)
    }
    is_float = kwargs.get('make_float', False)
    operation_value = operation_lookup[kwargs.get('operation', '')]
    if is_float:
        final = "{} {}".format(kwargs.get('message','The result is'), float(operation_value))
    else:
        final = "{} {}".format(kwargs.get('message','The result is'), int(operation_value))
    return final