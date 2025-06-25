from decimal import Decimal, InvalidOperation
from time import sleep
from cli_elements import clear_lines

def get_confirmation():

    confirm = input("Y or N?\n")
    
    if confirm.lower() == "y":
        return True
    elif confirm.lower() == "n":
        return False
    else:
        print("Invalid input")
        sleep(0.5)
        clear_lines(3)
        get_confirmation()

def is_decimal(value):
    try:
        Decimal(value)
        return True
    except (InvalidOperation, ValueError):
        return False
    
def get_integer_input(message = "Enter a whole number:"):
    number_input = input(f"{message}\n")
    number_input = Decimal(number_input)

    if number_input % 2 == 0 or (number_input + 1) % 2 == 0:
        return int(number_input)
    else:
        print("Invalid entry, you must enter a whole number:")
        sleep(1.5)
        clear_lines(7)
        get_integer_input()

def get_decimal_input(message = "Enter a number:", error = "Invalid number"):
    number_input = input(f"{message}\n")
     
    if is_decimal(number_input):
        number_input = Decimal(number_input)
        return number_input
    else:
        print(error)
        sleep(0.9)
        clear_lines(3)
        get_decimal_input()

def get_part_dimension():
       length_dimension = get_decimal_input("What is the length of your part (inches)?:")
       width_dimension = get_decimal_input("What is the width of your part (inches)?: ")
       total_needed = get_integer_input("How many of this part do you require?: ")
       print(f"{total_needed} part{'s'[:total_needed^1]} needed of size {length_dimension}\" x {width_dimension}\", correct?\n")
       get_confirmation()
