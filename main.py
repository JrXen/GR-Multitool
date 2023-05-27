import subprocess
import colorama
from colorama import Fore, Style

colorama.init()

banner = f"""
{Fore.LIGHTMAGENTA_EX} ██████╗ ██████╗      ██████╗ ███╗   ██╗    ████████╗ ██████╗ ██████╗ 
{Fore.LIGHTMAGENTA_EX}██╔════╝ ██╔══██╗    ██╔═══██╗████╗  ██║    ╚══██╔══╝██╔═══██╗██╔══██╗
{Fore.LIGHTMAGENTA_EX}██║  ███╗██████╔╝    ██║   ██║██╔██╗ ██║       ██║   ██║   ██║██████╔╝
{Fore.LIGHTMAGENTA_EX}██║   ██║██╔══██╗    ██║   ██║██║╚██╗██║       ██║   ██║   ██║██╔═══╝ 
{Fore.LIGHTMAGENTA_EX}╚██████╔╝██║  ██║    ╚██████╔╝██║ ╚████║       ██║   ╚██████╔╝██║     
{Fore.LIGHTMAGENTA_EX} ╚═════╝ ╚═╝  ╚═╝     ╚═════╝ ╚═╝  ╚═══╝       ╚═╝    ╚═════╝ ╚═╝     

{Style.RESET_ALL}
{Fore.CYAN}╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋
{Fore.CYAN}╋{"TOKEN ":^25}╋{"WEBHOOK":^25}╋{"OTHER":^25}╋{"NITRO":^25}╋
{Fore.CYAN}╋{"-" * 27}╋{"-" * 27}╋{"-" * 27}╋{"-" * 20}╋
╋ {Fore.YELLOW}[1]{Fore.RESET} Token Checker         ╋ {Fore.YELLOW}[6]{Fore.RESET} Webhook Spammer     ╋ {Fore.YELLOW}[8]{Fore.RESET} Hypesquad          ╋ {Fore.YELLOW}[10]{Fore.RESET} Nitro Generator    ╋
╋ {Fore.YELLOW}[2]{Fore.RESET} Leave Servers         ╋ {Fore.YELLOW}[7]{Fore.RESET} Webhook Deleter     ╋ {Fore.YELLOW}[9]{Fore.RESET} COMING SOON        ╋ {Fore.YELLOW}[11]{Fore.RESET} Nitro Checker      ╋
╋ {Fore.YELLOW}[3]{Fore.RESET} Onliner               ╋                         ╋                        ╋                         ╋
╋ {Fore.YELLOW}[4]{Fore.RESET} Nuker                 ╋                         ╋                        ╋                         ╋  
╋ {Fore.YELLOW}[5]{Fore.RESET} Token Info            ╋                         ╋                        ╋                         ╋
╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋
"""

print(banner)

user_input = input("Select: ")

options = {
    "1": ["Starting Token Checker...", ["python", "modules/checker.py"]],
    "2": ["Starting Leave Servers...", ["python", "modules/leaver.py"]],
    "3": ["Starting Onliner...", ["python", "modules/onliner.py"]],
    "4": ["Starting Nuker...", ["python", "modules/nuke.py"]],
    "5": ["Starting Token Info...", ["python", "modules/tokeninfo.py"]],
    "6": ["Starting Webhook Spammer...", ["python", "modules/webhook_spammer.py"]],
    "7": ["Starting Webhook Deleter...", ["python", "modules/deleter.py"]],
    "8": ["Starting Hypesquad...", ["python", "modules/hypesquad.py"]],
    "9":  ["Coming Soon"],
    "10": ["Starting Nitro Generator...", ["python", "modules/nitro_generator.py"]],
    "11": ["Starting Nitro Checker...", ["python", "modules/nitro_checker.py"]],
}

if user_input in options:
    selected_option = options[user_input]
    print(selected_option[0])
    subprocess.call(selected_option[1])
else:
    print("Invalid input. Please enter a valid number.")
