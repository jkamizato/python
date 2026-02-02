import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors: "))
valid_choice = True

computer_choice = random.randint(0,2)

if choice == 0:
    print(rock)
elif choice == 1:
    print(paper)
elif choice == 2:
    print(scissors)
else:
    print("Invalid input")
    valid_choice = False

if valid_choice:
    print(f"Computer chose: {computer_choice} \n")
    if computer_choice == 0:
        print(rock)
    elif computer_choice == 1:
        print(paper)
    else:
        print(scissors)

    if choice == computer_choice:
        print ("You draw")
    else:
        if choice == 0 and computer_choice == 1:
            print("You lose")
        if choice == 1 and computer_choice == 0:
            print("You win")
        if choice == 2 and computer_choice == 0:
            print("You lose")
        if choice == 2 and computer_choice == 1:
            print("You win")
        if choice == 0 and computer_choice == 2:
            print("You win")
        if choice == 1 and computer_choice == 2:
            print("You lose")