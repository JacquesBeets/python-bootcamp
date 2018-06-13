# import keyword


# def contains_keyword(*args):
#   for item in args:
#         if keyword.iskeyword(item): return True
#     return False

# print(contains_keyword("hello", "goodbye"))
# print(contains_keyword("def", "haha", "lol", "chicken", "alaska"))


# ====================================
# CUSTOM MODULES
# ====================================

#import bananas
import apples

#print(bananas.dip_in_chocolate())
print(apples.bake())

from bananas import dip_in_chocolate as dip

print(dip())