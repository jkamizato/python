def ask_age():
    age_value = 0
    try:
        age_value = int(input("How old are you?"))
    except ValueError:
        print("That's not an integer")
        ask_age()
    return age_value

age = ask_age()

if age > 18:
    print(f"You can drive at age {age}.")
