age = input("How old are you: ")

# if age:
#   age = int(age)
#   if age >= 18 and age < 21:
#     print("You can enter, but need a wristband.")
#   elif age >= 21:
#     print("You can enter and drink.")
#   else:
#     print("Sorry, you cant come in.")
# else:
#   print("Please enter an age!")

if age:
  age = int(age)
  if age >= 21:
    print("You can enter and drink.")
  elif age >= 18:
    print("You can enter, but need a wristband.")
  else:
    print("Sorry, you cant come in.")
else:
  print("Please enter an age!")
