WINNER_POSITIONS = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]

player1 = [0] * 9 # 0 - 8 (9 positions)
player2 = [0] * 9 # 0 - 8 (9 positions)

def is_player_won(player):
    indexes_mark = [index for index, value in enumerate(player) if value == 1]
    for position in WINNER_POSITIONS:
        if set(position).issubset(set(indexes_mark)):
            return True
    return False

def is_position_valid(position, player1, player2):
    if position < 0 or position > 8:
        return False

    if player1[position] == 1:
        return False

    if player2[position] == 1:
        return False

    return True

def print_board(player1, player2):

    for row in range(3):
        print_row = ""
        for column in range(3):
            index = (row * 3) + column

            if player1[index] == 1:
                print_row = f"{print_row} X "
            elif player2[index] == 1:
                print_row = f"{print_row} 0 "
            else:
                print_row = f"{print_row} _ "

        print_row = f"{print_row} \n"

        print(print_row)


# matriz 3x3

keep_going = True

while keep_going:

    # Player 1
    choice_player1 = int(input("Please enter X your choice: "))
    choice_is_valid = is_position_valid(choice_player1, player1, player2)
    while not choice_is_valid:
        choice_player1 = int(input("Please enter X your choice: "))
        choice_is_valid = is_position_valid(choice_player1, player1, player2)
    player1[choice_player1] = 1
    print_board(player1, player2)
    if is_player_won(player1):
        print("Player 1 You won!")
        keep_going = False
        break


    # Player 2
    choice_player2 = int(input("Please enter O your choice: "))
    choice_is_valid = is_position_valid(choice_player2, player1, player2)
    while not choice_is_valid:
        choice_player2 = int(input("Please enter O your choice: "))
        choice_is_valid = is_position_valid(choice_player2, player1, player2)
    player2[choice_player2] = 1
    print_board(player1, player2)
    if is_player_won(player2):
        print("Player 2 You won!")
        keep_going = False
        break
