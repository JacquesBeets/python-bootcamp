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

calling_in_sick = None

if sick_days > 0 and actually_sick:
  calling_in_sick = True
elif sick_days > 0 and kinda_sick and hate_your_job: