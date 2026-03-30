import random

def choose_num_dice():
    num_dice_valid = False
    while not num_dice_valid:
        try:
            num = int(input("how many dice would you like to roll? "))
        except ValueError:
            print("Invalid input, enter a number 1 - 5")
        else:
            if 0 <  num < 6:
                num_dice_valid = True
            else:
                print("Invalid input, enter a number 1 - 5")
    return num

def choose_num_sides():
    sides_valid = False
    while not sides_valid:
        try:
            sides = int(input("how many sides would you like the dice to have? "))
        except ValueError:
            print("Invalid input, enter a number 1 - 21")
        else:
            if 0 < sides < 22:
                sides_valid = True
            else:
                print("Invalid input, enter a number 1 - 21")
    return sides

def roll_dice(num, sides):
    dice_list = [random.randint(1, sides) for dice in range(num)]
    for i, dice in enumerate(dice_list):
        print(f"dice no. {i+1}: rolled {dice}")
    
def continue_check():
    while True:
        cont = str(input("Would you like to roll again? ")).lower()
        if cont == "yes":
            return True
        elif cont == "no":
            return False
        else:
            print("please enter only yes or no")

still_playing = True
while still_playing:
    num_dice = choose_num_dice()
    num_sides = choose_num_sides()
    roll_dice(num_dice, num_sides)
    still_playing = continue_check()
print("goodbye")
   