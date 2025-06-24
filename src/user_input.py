import sys
from time import sleep
from cli_elements import clear_screen, clear_lines

def get_confirmation():

    confirm = input("Y or N?\n")
    
    if confirm.lower() == "y":
        return True
    elif confirm.lower() == "n":
        return False
    else:
        print("invalid input")
        sleep(0.5)
        clear_lines(3)
        get_confirmation()

# Development Note:
# Add a positive number input validation for use in get_part_dimension
# and other numbers required. Will need to print a message (as input).

def get_part_dimension():
       length_dimension = int(input("What is the length of your part (inches)?: "))
       width_dimension = int(input("What is the width of your part (inches)?: "))
       total_needed = int(input("How many of this part do you require?: "))

       print(f"{total_needed} part{'s'[:total_needed^1]} needed of size {length_dimension}\" x {width_dimension}\", correct?\n")
       get_confirmation()
