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
        return get_confirmation()

def is_decimal(value):
    try:
        Decimal(value)
        return True
    except (InvalidOperation, ValueError):
        return False
    
def get_integer_input( message = "Enter a whole number:"):
    while True:
        try:
            number_input = input(f"{message}\n")
            number_input = Decimal(number_input)

            if number_input % 2 == 0 or (number_input + 1) % 2 == 0:
                return int(number_input)
        except (InvalidOperation, ValueError):
            sleep(1.5)
            clear_lines(7)
            return get_integer_input()

def get_decimal_input(message = "Enter a number:", error = "Invalid number"):
    while True:
        try:
            number_input = input(f"{message}\n")
            number_input = Decimal(number_input)

            if is_decimal(number_input):
                return number_input
        except (InvalidOperation, ValueError):
            print(error)
            sleep(0.9)
            clear_lines(3)
            return get_decimal_input()

def get_part_dimension():
       length_dimension = get_decimal_input("What is the length of your part (inches)?:")
       width_dimension = get_decimal_input("What is the width of your part (inches)?: ")
       total_needed = get_integer_input("How many of this part do you require?: ")
       #print(f"{total_needed} part{'s'[:total_needed^1]} needed of size {length_dimension}\" x {width_dimension}\", correct?\n")
       print(f"{total_needed} part{'s' if total_needed >= 1 else ''} needed of size {length_dimension}\" x {width_dimension}\", correct?\n")
       get_confirmation()
       return length_dimension, width_dimension, total_needed