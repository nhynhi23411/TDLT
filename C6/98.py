import random

def guess_number_game():
  while True:
    computer_number = random.randint(1, 100) 
    guess_count = 0
    win = False

    while guess_count < 7:
      guess_count += 1
      user_guess = int(input("Guess a number between 1 and 100: "))
      print(f"You guessed {guess_count} times.")

      if computer_number == user_guess:
        print("Congratulations! You guessed it. The number was:", computer_number)
        win = True
        break
      elif computer_number > user_guess:
        print("Too low. Try again.")
      else:
        print("Too high. Try again.")

    if not win:
      print("Game over! The number was:", computer_number)

    play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower() != 'y':
      break

  print("Thanks for playing!")

guess_number_game()