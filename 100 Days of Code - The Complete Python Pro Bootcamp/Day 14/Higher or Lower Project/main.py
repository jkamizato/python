from art import logo, vs
from game_data import data
import random

def check_result(compare_a, compare_b, answer_value):
    if answer_value == 'a':
        return compare_a['follower_count'] > compare_b['follower_count']
    else:
        return compare_b['follower_count'] > compare_a['follower_count']

def display_data(compare, compare_type):
    print(f"Compare {compare_type}: {compare['name']}, a {compare['description']}, from {compare['country']}.")


score = 0
compareB = random.choice(data)
keep_going = True


while keep_going:
    print("\n"*10)
    print(logo)
    if score > 0:
        print(f"You're right! Current score: {score}")

    compareA = compareB
    compareB = random.choice(data)

    # Change B if is equals
    while compareA == compareB:
        compareB = random.choice(data)

    display_data(compareA, 'A')
    print(vs)
    display_data(compareB, 'B')

    answer = input("Who has more followers? Type 'A' or 'B': ").lower()

    if check_result(compareA, compareB, answer):
        score += 1
    else:
        print("\n"*10)
        print(logo)
        print(f"Sorry, that's wrong. Final score: {score}")
        keep_going = False

