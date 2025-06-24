from screens.main_menu import print_main_menu, print_stock_dimensions
from user_input import get_confirmation, get_part_dimension

def main():
    print_main_menu(get_part_dimension)

if __name__ == "__main__":
    main()

"""
LumberCutOptimizer
Author: Alex Shelton

Description:
A CLI too to calculate the optimal cut lists for rectangular
parts from wood, such as sheet goods. Accepts parameters for stock
size and part dimensions from the user, organizes them on sheets,
and outputs a cut list.

Notes:
- First iteration assumes hardcoded kerf of 1/8 inch (0.125")
- First iteration only works with imperial units
"""