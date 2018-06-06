from random import randint

print("====================")
print("...rock...")
print("...paper...")
print("...scissors...")
print("====================")

player_wins = 0
computer_wins = 0
winning_score = 2

while player_wins < winning_score and computer_wins < winning_score:
  print(f"||||| PLAYER SCORE: {player_wins} ||||| COMPUTER SCCORE: {computer_wins} |||||")
  player = input("Please enter your choice: ").lower()
  if player == "quit" or player == "q":
    break
  computer = None
  rand_num = randint(0, 2)

  if rand_num == 0:
    computer = "rock"
  elif rand_num == 1:
    computer = "paper"
  elif rand_num == 2:
    computer = "scissors"

 
  print(f"Computers plays: {computer}")

  if player == computer:
    print("Its a tie!")
  elif player == "rock":
    if computer == "scissors":
      print("Player Wins!")
      player_wins += 1
    else:
      print("Computer Wins!")
      computer_wins += 1
  elif player == "paper":
    if computer == "rock":
      print("Player Wins!")
      player_wins += 1
    else: 
      print("Computer Wins!")
      computer_wins += 1
  elif player == "scissors":
    if computer == "paper":
      print("Player Wins!")
      player_wins += 1
    else: 
      print("Computer Wins!")
      computer_wins += 1
  else:
    print("Something went wrong")
print("============\nGAME OVER\n============")

if player_wins > computer_wins:
  print("CONGRATS! YOU WON!")
elif player_wins == computer_wins:
  print("ITS A TIE")
else:
  print("OH NO! COMPUTER WON!")
# print(f"=====FINAL SCORES!===== \nPLAYER: {player_wins} ||||| COMPUTER: {computer_wins} \n=====FINAL SCORES!=====")