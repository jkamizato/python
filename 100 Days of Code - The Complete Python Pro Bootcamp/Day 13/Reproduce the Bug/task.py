from random import randint
dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, len(dice_images) - 1)
print(dice_images[dice_num])
