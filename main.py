import sys 
import os
import pyfiglet

sys.path.extend([
    r"C:\Users\gowrishankar\Desktop\projects\harish\open port checher",
    r"C:\Users\gowrishankar\Desktop\projects\harish\sql injection",
    r"C:\Users\gowrishankar\Desktop\projects\harish\Sub domain Extractor"
])

from port import port_check
from sqlifinder import inject
from domainExtractor import domain

def clear():
    if 'linux' in sys.platform or 'darwin' in sys.platform:
        os.system('clear')
    else:
        os.system('cls')
clear()
banner = pyfiglet.figlet_format("pentesting      tools")

print("-"*80)
print(banner)
print("-"*80)
 
print(" 1. check open the port \n 2. sql injection on website \n 3. extract the domains of a website ")
option = input(">>>")

while True:
    if option == "1":

        port_check()
        break

    elif option == "2":

        inject()
        break

    elif option == "3":
        domain()
        break

    else:
        print("Invalid option. Please choose again.")
        option = input(">>>")


