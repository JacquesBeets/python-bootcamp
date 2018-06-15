

#GAME LOGIC
def start_game(quotes): 
  quote = choice(quotes)
  remaining_guesses = 4
  print("Here is a quote: ")
  print(quote["text"])
  print(quote['author'])
  guess = ''

  while guess.lower() != quote["author"].lower() and remaining_guesses > 0:
    print(f"Guesses remaining: {remaining_guesses}\n")
    guess = input(f"Who said this? ")
    if guess.lower() == quote['author'].lower():
      print("Well done! You got it right!")
      break
    remaining_guesses -= 1
    if remaining_guesses == 3:
      res = requests.get(f"{BASE_URL}{quote['link']}")
      soup = BeautifulSoup(res.text, "html.parser")
      birth_date = soup.find(class_="author-born-date").text
      birth_place = soup.find(class_="author-born-location").text
      print(f"\nHere's a hint: The author was born on {birth_date} {birth_place}")
    elif remaining_guesses == 2:
      print(f"\nHere's a hint: The authors first name begins with: {quote['author'][0]}")
    elif remaining_guesses == 1:
      last_initial = quote['author'].split(" ")[1][0]
      print(f"\nHere's a hint: The authors first name begins with: {last_initial}")
    else:
      print(f"\nSorry you ran out of guesses. The answer was {quote['author']}")


  again = ''
  while again.lower() not in ('y', 'yes', 'n', 'no'):
    again = input("Would you like to play again? (y/n)? ")
  if again.lower() in ('yes', 'y'):
    return start_game(quotes)
  else:
    print('OK, Goodbye!')


quotes = scrape_quotes()

start_game(quotes)