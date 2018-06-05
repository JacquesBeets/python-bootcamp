from random import randint
import time

print("...rock...")
print("...paper...")
print("...scissors...")

player = input("Please enter your choice: ").lower()
computer = None
rand_num = randint(0, 2)

if rand_num == 0:
  computer = "rock"
elif rand_num == 1:
  computer = "paper"
elif rand_num == 2:
  computer = "scissors"

time.sleep(1)
print(f"Computers plays: {computer}")

time.sleep(1)
if player == computer:
  print("Its a tie!")
elif player == "rock":
  if computer == "scissors":
    print("Player Wins!")
  else:
    print("Computer Wins!")
elif player == "paper":
  if computer == "rock":
    print("Player Wins!")
  else: 
    print("Computer Wins!")
elif player == "scissors":
  if computer == "paper":
    print("Player Wins!")
  else: 
    print("Computer Wins!")
else:
  print("Something went wrong")