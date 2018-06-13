# ====================================
# OBJECTIVES
# ====================================

# Explain common errors and how they occur in Python
# Use pdb to set breakpoints and step through code 
# Use try and except blocks to handle errors

# ============
# SyntaxError
# ============

# Occurs when Python encounters incorrect syntax (something it doesn't parse).
# Usually due to typos or not knowing Python well enough

#def first: # SyntaxError

#None = 1 # SyntaxError

#return # SyntaxError

# ============
# NameError
# ============

#This occurs when a variable is not defined, i.e. it hasn't been assigned
#test
# NameError: name 'test' is not defined


# ============
# TypeError
# ============

# An operation or function is applied to the wrong type
# Python cannot interpret an operation on two data types

#len(5)  
# TypeError: object of type 'int' has no len()

#"awesome" + []  
# TypeError: cannot concatenate 'str' and 'list' objects


# ============
# IndexError
# ============

#Occurs when you try to access an element in a list using an invalid index (i.e. one that is outside the range of the list or string):

#list = ["hello"]
#list[2]
# IndexError: list index out of range


# ============
# ValueError
# ============

#This occurs when a built-in operation or function receives an argument that has the right type but an inappropriate value:

#int("foo")
# ValueError: invalid literal for int() with base 10: 'foo'

# ============
# KeyError
# ============

#This occurs when a dictionary does not have a specific key:

#d = {}
#d["foo"]
# KeyError: 'foo'


# ==============
# AttributeError
# ==============

#This occurs when a variable does not have an attribute:

#"awesome".foo
# AttributeError: 'str' object has no attribute 'foo'


# ====================================
# RAISE YOUR OWN ERRORS/EXCEPTIONS
# ====================================

#In python we can also throw errors using the raise keyword. This is helpful when creating your own kinds of exception and error messages.

# raise ValueError('invalid value')



# =====================================
# HANDLE ERRORS - TRY AND EXCEPT BLOCKS
# =====================================

#In Python, it is strongly encouraged to use try/except blocks, to catch exceptions when we can do something about them. Let's see what that looks like.

try: 
    foobar
except NameError as err:
    print(err)


# ====================================
# EXCERSIZES
# ====================================

# Write a function called divide, which accepts two parameters (you can call them num1 and num2). The function should return the result of num1 divided by num2. If you do not pass the correct amount of arguments to the function, it should return the string "Please provide two integers or floats". If you pass as the second argument a 0, Python will raise a ZeroDivisionError, so if this function is invoked with a 0 as the value of num2, return the string "Please do not divide by zero"

    # Examples
    
    # divide(4,2)  2
    # divide([],"1")  "Please provide two integers or floats"
    # divide(1,0)  "Please do not divide by zero"

def divide(num1, num2):
    try:
        total = num1/num2
    except TypeError:
        return "Please provide two integers or floats"
    except ZeroDivisionError:
        return "Please do not divide by zero"
    return total