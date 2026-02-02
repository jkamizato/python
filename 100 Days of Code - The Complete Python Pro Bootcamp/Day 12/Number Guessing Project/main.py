from art import logo
import random


attempt = 0

print(logo)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
level = input("Choose a difficulty. Type 'easy' or 'hard':")

if level == 'easy':
    attempt = 10
else:
    attempt = 5

super_number = random.randint(1, 100)

game_over = False

while attempt >= 1 and not game_over:
    print(super_number)
    print(f"You have {attempt} attempts remaining to guess the number.")
    guess = int(input("Make the guess: "))
    if guess == super_number:
        print("You win!")
        game_over = True
    elif guess > super_number:
        print("Too high!")
    else:
        print("Too low!")

    attempt -= 1

if attempt < 1:
    print("You've run out of guesses. Refresh the page to run again.")