# ================================
# DICTIONARY COMPREHENSIONS
# ================================

numbers = dict(first=1, second=2, third=3)
squared_numbers = {key: value ** 2 for key, value in numbers.items()}
print(squared_numbers)

squared_numbers2 = {num: num**2 for num in [1,2,3,4,5]}
print(squared_numbers2)


str1 = "ABC"
str2 = "123"
combo = {str1[i]: str2[i] for i in range(0, len(str1))}
print(combo)

# ================================================
# DICTIONARY COMPREHENSIONS WITH CONDITIONAL LOGIC
# ================================================

num_list = list(range(1, 5))
answer = {num:("even" if num % 2 == 0 else "odd") for num in num_list}
print(answer)


# ================================
# EXCERSISES
# ================================

# list1 = ["CA", "NJ", "RI"]
# list2 = ["California", "New Jersey", "Rhode Island"]


# answer = {list1[i]:list2[i] for i in range(len(list1))}
# print(answer)


#EXCERSIZE 2

# person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]

# answer = {person[i][0]:person[i][1] for i in range(len(person))}
# print(answer)

# #ANOTHER WAY
# answer = {thing[0]: thing[1] for thing in person}

# #ANOTHER WAY
# answer = {k:v for k,v in person}

# #EASIEST WAY
# answer = dict(person)



# #EXCERSIZE 3

# answer = {}.fromkeys(["a", "e", "i", "o", "u"], 0) #can also use dict.fromkeys("aeiou", 0)
# print(answer) 



# #EXCERSIZE 4
# answer = dict.fromkeys(list(range(65, 91)), chr(range(65, 91))) #DOES NOT WORK chr() can not hold a range
# answer = {i:chr(i) for i in range(65, 91)}
# print(answer) 