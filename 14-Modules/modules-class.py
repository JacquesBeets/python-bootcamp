# ====================================
# OBJECTIVES
# ====================================

# Define what a module is
# Import code from built-in modules
# Import code from other files
# Import code from external modules using pip
# Describe common module patterns
# Describe the request/response cycle in HTTP
# Use the requests module to make requests to web apps

# ====================================
# BUILT IN MODULES
# ====================================

import random

random.choice(["apple", "banana", "cherry", "durian"])
random.shuffle(["apple", "banana", "cherry", "durian"])

# The "as" function allows you to rename the imports to anything you like.
import random as omg_so_random

omg_so_random.choice(["apple", "banana", "cherry", "durian"])
omg_so_random.shuffle(["apple", "banana", "cherry", "durian"])

import random as r

r.choice(["apple", "banana", "cherry", "durian"])
r.shuffle(["apple", "banana", "cherry", "durian"])

# Importing Parts of a Module

# The from keyword lets you import parts of a module
# Handy rule of thumb: only import what you need!
# If you still want to import everything, you can also use the from MODULE import * pattern

from random import choice, randint

choice(["apple", "banana", "cherry", "durian"])
shuffle(["apple", "banana", "cherry", "durian"])


# Different Ways to Import

# import random
# import random as omg_so_random
# from random import *
# from random import choice, shuffle
# from random import choice as gimme_one, shuffle as mix_up_fruit


# ====================================
# CUSTOM MODULES
# ====================================

# You can import from your own code too
# The syntax is the same as before
# import from the name of the Python file

# file1.py
def fn():
    return "do some stuff"


def other_fn():
    return "do some other stuff"


# ====================================
# EXTERNAL MODULES
# ====================================

# Built-in modules come with Python
# External modules are downloaded from the internet
# You can download external modules using pip

# Package management system for Python
# As of 3.4, comes with Python by default
# python -m pip install NAME_OF_PACKAGE
