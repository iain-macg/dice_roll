import random

def validate_number(number, range_end):
    try:
        num = int(number)
    except ValueError:
        print(f"Invalid input, enter a number 1 - {range_end}")
    else:
        if 0 <  num <= range_end:
            return True 
        else:
           print(f"Invalid input, enter a number 1 - {range_end}") 

def choose_num_dice():
    num_dice_valid = False
    while not num_dice_valid:
        num = input("how many dice would you like to roll? ")
        num_dice_valid = validate_number(num, 5)
    return int(num)

def choose_num_sides():
    sides_valid = False
    while not sides_valid:
        sides = input("how many sides would you like the dice to have? ")
        sides_valid = validate_number(sides, 20)
    return int(sides)

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

def main():
    still_playing = True
    while still_playing:
        num_dice = choose_num_dice()
        num_sides = choose_num_sides()
        roll_dice(num_dice, num_sides)
        still_playing = continue_check()
    print("goodbye")

if __name__ == "__main__":
    main()
   