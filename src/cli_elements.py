import os

def print_header():
    print("==========================")
    print("   Lumber Cut Optimizer   ")
    print("==========================")

def print_footer():
    version = "0.0.1"
    print("==========================")
    print(f"Version: {version}")
    print("==========================")

def clear_lines(x = 1):
        cursor_up = "\033[1A"
        clear = "\x1b[2K"

        while x > 0:
            print(cursor_up + clear, end="")
            x = x - 1

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')