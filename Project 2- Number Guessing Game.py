import random
print("Welcome to the Number Guessing Game!")

while True:
    number = random.randint(1,100)
    attempts = 0

    guess = int(input("Hello, I am your Guessing Bot. Please guess a number between 1 & 100: "))
    while guess != number:
        attempts += 1
        if guess > number:
            print("Sorry! Your Number was Too big! Please Try again!")
            try:
                guess = int(input("Please guess again: "))
            except ValueError:
                print("Please enter a Valid integer")
        elif guess < number:
            print("Sorry! Your Number was too small! Please try again!")
            try:
                guess = int(input("Please guess again: "))
            except ValueError:
                print("Please enter a Valid integer")
        elif guess > 100 or guess < 1:
            print(f"Please pick a number between 1 & 100! You have guessed {attempts} times so far!")
            try:
                guess = int(input("Please guess again: "))
            except ValueError:
                print("Please enter a Valid integer")
        if attempts > 10:
            print(f"Sorry! You have used up all of your attempts! the number was {number}! Better Luck Next Time!")

    if guess == number:
        print(f"Congratulations! You guessed the correct number. The number was {number}!")
        print(f"You guessed the number in {attempts} Attempts!")
    play_again = input("Would you like to play again? Type 'yes' or 'no': ")
    if play_again.lower() != 'yes' or 'Yep' or 'Yup':
        print("Thanks for playing! Goodbye!")
        break