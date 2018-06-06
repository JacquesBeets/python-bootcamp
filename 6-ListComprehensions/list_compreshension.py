# ===========================
# LIST COMPREHENSION
# ===========================

nums = list(range(1,7))
name = "jacques"
friends = ["harry", "mia", "johan"]

# comprehension = [x*10 for x in nums]
# comprehension = [x/2 for x in nums]
# comprehension = [char.upper() for char in name]
# comprehension = [friend.capitalize() for friend in friends]
# comprehension = [num*10 for num in range(1,6)]
# comprehension = [bool(friend) for friend in friends] #convert values to their boolean value
# comprehension = [str(number) for number in nums] #convert values to strings



# =========================================
# LIST COMPREHENSION WITH CONDITIONAL LOGIC
# =========================================

# comprehension = [num for num in nums if num % 2 == 0] # finds all even numbers
# comprehension = [num for num in nums if num % 2 != 0] # finds all odd numbers


# print(comprehension)


# ===========================
# EXCERSIZES
# ===========================

# nums1 = list(range(1,5))
# nums2 = list(range(3,7))

# answer = [num for num in nums1 if num in nums2]
# print(answer)

# names = ["Elie", "Tim", "Matt"]
# answer2 = [name[::-1].lower() for name in names]
# print(answer2)

# nums = list(range(1,101))
# answer = [num for num in nums if num % 12 == 0]
# print(answer)

# answer = [x for x in "amazing" if x not in "aeiou"]
# print(answer)


