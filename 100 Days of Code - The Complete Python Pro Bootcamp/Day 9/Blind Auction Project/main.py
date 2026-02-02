from art import logo

print(logo)
bid = {}

keep_bid = 'yes'
while keep_bid == 'yes':
    # TODO-1: Ask the user for input
    name = input("Name:")
    price = int(input("Price:"))
    # TODO-2: Save data into dictionary {name: price}
    bid[name] = price
    # TODO-3: Whether if new bids need to be added
    keep_bid = input("Is there other user who want to bid? 'yes' or 'no'")
    print("\n" * 20)

# TODO-4: Compare bids in dictionary
max_value = 0
max_key = ''

for key in bid:
    if bid[key] > max_value:
        max_value = bid[key]
        max_key = key


print(f"The winner {max_key} is {max_value}.")