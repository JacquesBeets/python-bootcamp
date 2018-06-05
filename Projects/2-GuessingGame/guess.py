import random

play_again = "y"

while play_again == "y":
  random_number = random.randint(1,10)
  guess = int(input("Pick a number from 1 to 10: "))
  while guess != random_number:
    if guess < random_number:
      print("Too Low!")
      guess = int(input("Guess again: "))
    else:
      print("Too High")
      guess = int(input("Guess again: "))
    print("You got it!")
  play_again = input("Would you like to play again? (y/n) ")

print("Thanks for playing! Bye!")


#=================================================
#ANOTHER VERSION with break
#=================================================

# import random

# random_number = random.randint(1,10)  # numbers 1 - 10
# guess = None

# while True:
# 	guess = input("Pick a number from 1 to 10: ")
# 	guess = int(guess)
# 	if guess < random_number:
# 		print("TOO LOW!")
# 	elif guess > random_number:
# 		print("TOO HIGH!")
# 	else:
# 		print("YOU WON!!!!")
# 		play_again = input("Do you want to play again? (y/n) ")
# 		if play_again == "y":
# 			random_number = random.randint(1,10)  # numbers 1 - 10
# 			guess = None
# 		else:
# 			print("Thank you for playing!")
# 			break