# Accessible anywhere
my_global_var = 1

for _ in range(10):
    # Accessible anywhere
    my_block_var = 3


def my_function():
    # Only accessible within my_function()
    my_local_var = 2
    print(my_block_var)


print(my_block_var)