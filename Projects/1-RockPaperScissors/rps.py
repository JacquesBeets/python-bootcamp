print("...rock...")
print("...paper...")
print("...scissors...")

player1 = input("Player 1, Make your move: ")
print("======== NO CHEATING ========\n" * 20)
player2 = input("Player 2, Make your move: ")

#=============================================
#Verbose Method
#=============================================

# if player1 == "rock" and player2 == "scissors":
#   print("Player 1 wins")
# elif player1 == "rock" and player2 == "paper":
#   print("Player 2 wins")
# elif player1 == "paper" and player2 == "rock":
#   print("Player 1 wins")
# elif player1 == "paper" and player2 == "scissors": 
#   print("Player 2 wins")
# elif player1 == "scissors" and player2 == "paper":
#   print("Player 1 wins")
# elif player1 == "scissors" and player2 == "rock":
#   print("Player 2 wins")
# elif player1 == player2:
#   print("Its a tie!")
# else:
#   print("Something went wrong")

#=============================================
#Refactored
#=============================================

if player1 == player2:
  print("Its a tie!")
elif player1 == "rock":
  if player2 == "scissors":
    print("Player 1 wins")
  elif player2 == "paper":
    print("Player 2 wins")
elif player1 == "paper":
  if player2 == "rock":
    print("Player 1 wins")
  elif player2 == "scissors":
    print("Player 2 wins")
elif player1 == "scissors":
  if player2 == "paper":
    print("Player 1 wins")
  elif player2 == "rock":
    print("Player 2 wins")
else:
  print("Something went wrong")
  

  
    