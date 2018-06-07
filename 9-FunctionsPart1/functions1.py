# =================================
# FUNCTIONS PART 1
# =================================

# def say_hi(): #define your function
#   return 'Hi there!' # return exits the function. Anything after will not run

# greeting = say_hi() #call your function

# print(greeting)


# =================================
# EXCERSIZES
# =================================

# def generate_evens():
#   li = list(range(1, 50))
#   return li[1:50:2]

# print(generate_evens())


# EXCERSIZE 2
# def yell(string):
#   return string.upper() + "!"

# print(yell("hello"))

# =================================
# FUNCTIONS PART - DEFAULT PARAMS
# =================================

# def exponent(num, power=2):
#   return num ** power

# print(exponent(9))


# =================================
# EXCERSIZES
# =================================

# def speak(animal="dog"):
#   if animal == "dog":
#     return "woof"
#   elif animal == "pig":
#     return "oink"
#   elif animal == "duck":
#     return "quack"
#   elif animal == "cat":
#     return "meow"
#   return "?"

# print(speak())
# print(speak("pig"))
# print(speak("duck"))
# print(speak("cat"))
# print(speak("banana"))

# # SHORTER SOLUTION

# def speak(animal="dog"):
#     noises = {"dog": "woof", "pig": "oink", "duck": "quack", "cat": "meow"}
#     noise = noises.get(animal)
#     if noise:
#         return noise
#     return "?"

# # EVEN SHORTER SOLUTION

# def speak(animal='dog'):
#     noises = {'pig':'oink', 'duck':'quack', 'cat':'meow', 'dog':'woof'}
#     return noises.get(animal, '?')

# print(speak())
# print(speak("pig"))
# print(speak("duck"))
# print(speak("cat"))
# print(speak("banana"))

# ==================================
# FUNCTIONS PART - KEYWORD ARGUMENTS
# ==================================

# When you define a function and use an = you are setting a default parameter

# When you invoke a function and use an = you are making a keyword argument

# def exponent(num, power=2):
# 	return num ** power

# # Order doesn't matter anymore, if we use key word arguments:
# print(exponent(num=2,power=3)) #8
# print(exponent(power=3, num=2)) #8

# # Without keywords args, order still matters:
# print(exponent(3,4)) #81
# print(exponent(4,3)) #64


# def full_name(first="Colt", last="Steele"):
#     return "Your name is {first} {last}"

# full_name() # Your name is Colt Steele

# full_name(last='Enthusiast', first='Python') # Your name is Python Enthusiast

# ==================================
# FUNCTIONS PART - SCOPE
# ==================================

#Variables created in functions are scoped in that function!
# instructor = 'Colt'

# def say_hello():
#     return f'Hello {instructor}'

# say_hello() 'Hello Colt'


# def say_hello():
#     instructor = 'Colt'
#     return f'Hello {instructor}'

# say_hello()

# print(instructor) # NameError

# ==================================
# FUNCTIONS PART - GLOBAL SCOPE
# ==================================

# NOT A GOOD IDEA
# total = 0

# def increment():
#     total += 1
#     return total

# increment() # Error!

# total = 0

# def increment():
#     global total
#     total += 1
#     return total

# increment() # 1

# ==================================
# FUNCTIONS PART1 - NONLOCAL SCOPE
# ==================================

# def outer():
#     count = 0
#     def inner():
#         nonlocal count
#         count += 1
#         return count
#     return inner()

# ====================================
# FUNCTIONS PART1 - DOCUMENT FUNCTIONS
# ====================================

# Use """ """

# Essential when writing complex functions

def say_hello():
    """A simple function that returns the string hello"""
    return "Hello!"

print(say_hello.__doc__) # 'A simple function that returns the string hello'