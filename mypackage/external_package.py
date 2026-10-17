# Requires colorama; install with: pip install colorama
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

# Demonstrate usage by printing colored text messages
print(Fore.GREEN + "Success! The colorama package has been installed and imported correctly.")
print(Fore.CYAN + Style.BRIGHT + "Task 3 completed: External packages are working smoothly.")