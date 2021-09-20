class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print(f"{bcolors.WARNING}Warning: No active frommets remain. Continue?{bcolors.ENDC}")
print(f"{bcolors.FAIL}Warning: No active frommets remain. Continue?{bcolors.ENDC}")
print(f"{bcolors.BOLD}Warning: No active frommets remain. Continue?{bcolors.ENDC}")
print(f"{bcolors.OKGREEN}Warning: No active frommets remain. Continue?{bcolors.ENDC}")

from termcolor import colored
print(colored('hello', 'red'), colored('world', 'green'))

#https://stackoverflow.com/questions/287871/how-to-print-colored-text-to-the-terminal



import sys
from time import sleep
from colorama import init, Fore
init()


def tprint(words):
    for char in words:
        sleep(0.15)
        sys.stdout.write(char)
        sys.stdout.flush()

red_string = Fore.RED + "This is a red string\n" + Fore.RESET

tprint(red_string)    # prints red_string in red font with typewriter effect