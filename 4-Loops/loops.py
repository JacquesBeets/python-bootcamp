#=============================
# for LOOP
#=============================

# for number in range(1, 10):
#   print(number*number)
#   print(number)

# for letter in "coffee":
#   print(letter)

#=============================
# RANGES
#=============================

# r = range(10)
# print(list(r))

# nums = range(1, 10, 2) #skip every second number
# print(list(nums))

#=============================
# REPEATER EXCERSIZE
#=============================

# times = input("How many time do you have to clean your room? ")
# times = int(times)

# for time in range(times):
#     print(f"time {time+1}:Clean your room!")

#=============================
# UNLUCKY NUMBERS EXCERSIZE
#=============================

# x = None

# for x in range(1, 21):
#     x = x + 1
#     if x == 4 or x == 13:
#         print(f"{x}: UNLUCKY")
#     elif x % 2 == 0:
#         print(f"{x}: even")
#     else:
#         print(f"{x}: odd")

#=============================
# WHILE LOOPS - Continues to loop WHILE condition is met
#=============================

# msg = input("whats the secret password? ")

# while msg != "please":
#     print("Wrong!")
#     msg = input("whats the secret password? ")
# print("Correct!")

#=============================
# EMOJI ART EXCERSIZE
#=============================
# emoji = 0

# while emoji < 10:
#     emoji += 1
#     print("\U0001f600 " * emoji)

#=============================
# STOP COPYING ME EXCERSIZE
#=============================


# msg = input("Hows it going? ")

# while msg != "stop it":
#     # print(msg)
#     msg = input(f"{msg}\n")
# print("FINE!")

#=============================
# THE "break" KEYWORD
#=============================

# while True:
#     command = input("Type 'exit' to exit: ")
#     if (command == "exit"):
#         break

