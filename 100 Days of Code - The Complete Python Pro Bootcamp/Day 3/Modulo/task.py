# Discover if a number is even or odd.

value = int(input("Give a number: "))

odd_even = value % 2

if odd_even == 0:
    print("It is even")
else:
    print("It is odd")