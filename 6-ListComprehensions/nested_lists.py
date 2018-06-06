# ===========================
# NESTED LISTS
# ===========================

nested_list = [list(range(1,4)), list(range(4,8)), list(range(8,11))]

# print(nested_list[2][2])

# ===========================
# NESTED LOOPS
# ===========================

# for x in nested_list:
#   for val in x:
#     print(val)

# ===========================
# NESTED LISTS COMPREHENSION
# ===========================

# [[print(val) for val in li] for li in nested_list]


# board = [[num for num in range(1,4)] for val in range(1,4)]
# print(board)

# board = [["X" if num % 2 != 0 else "O" for num in range(1,4)] for val in range(1,4)]
# print(board)

# ===========================
# EXERCISES
# ===========================

# answer = [[ x for x in range(3)] for val in range(3)]


# answer = [[ x for x in range(10)] for val in range(10)]
# print(answer)