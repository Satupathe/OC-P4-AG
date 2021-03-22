import colorama
from colorama import Fore, Back, Style
from colorama import init
from termcolor import colored, cprint 
  
text = colored('Hello, World!', 'red', attrs=['reverse', 'blink']) 
print(text) 
cprint('Hello, World!', 'green', 'on_red') 
  
print_red_on_cyan = lambda x: cprint(x, 'red', 'on_cyan') 
print_red_on_cyan('Hello, World!') 
print_red_on_cyan('Hello, Universe!') 
  
for i in range(10): 
    cprint(i, 'magenta', end=' ') 
  


print(f"{Style.BRIGHT}Voulez-vous modifier les ranks des joueurs du tournoi venant de se terminer?")
print("")
print(f"{Style.BRIGHT}{Fore.RED}yes:{Style.NORMAL}{Fore.WHITE}Permet i venant de se terminer")