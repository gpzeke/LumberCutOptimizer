from cli_elements import print_header, print_footer, clear_screen
from user_input import get_confirmation

def print_main_menu(test):
        clear_screen()
        print_header()
        test()


def print_stock_dimensions():
        print("\nDo you want to use 48\" x 96\" sheet goods (49\" x 97\" nominal?)\n\n\n")
        get_confirmation()