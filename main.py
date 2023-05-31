
import subprocess




options = {
    "1": ["Starting Token Checker...", ["python", "modules/checker.py"]],
    "2": ["Starting Leave Servers...", ["python", "modules/leaver.py"]],
    "3": ["Starting Onliner...", ["python", "modules/onliner.py"]],
    "4": ["Starting Nuker...", ["python", "modules/nuke.py"]],
    "5": ["Starting Token Info...", ["python", "modules/tokeninfo.py"]],
    "6": ["Starting Webhook Spammer...", ["python", "modules/webhook_spammer.py"]],
    "7": ["Starting Webhook Deleter...", ["python", "modules/deleter.py"]],
    "8": ["Starting Hypesquad...", ["python", "modules/hypesquad.py"]],
    "9": ["Starting Raid...", ["python", "modules/raid.py"]],
    "10": ["Starting Nitro Generator...", ["python", "modules/nitro_generator.py"]],
    "11": ["Starting Nitro Checker...", ["python", "modules/nitro_checker.py"]],
    "12": ["..................",  ["python", "modules/massdm.py"]],
    "13": ["..................",  ["python", "modules/massdm.py"]],
    "14": ["..................",  ["python", "modules/massdm.py"]],        
    "15": ["=.=",  ["python", "modules/credits.py"]]    
}

from colorama import init, Fore, Style

init(autoreset=True)

banner = f"""
{' ' * 14}{Fore.CYAN}     ╔═══════════════════════════════════════════════════════╗{Style.RESET_ALL}
{' ' * 14}{Fore.CYAN}     ║           {Fore.WHITE}https://discord.gg/vTtScREqkk{Fore.CYAN}               ║{Style.RESET_ALL}
{' ' * 10}{Fore.CYAN}╔═════════════════════════════════════════════════════════════════════════════╗{Style.RESET_ALL}
{' ' * 10}{Fore.CYAN}║  {Fore.GREEN}[1] Token Checker        {Fore.CYAN}║  {Fore.GREEN}[6] Webhook Spammer    {Fore.CYAN}║  {Fore.GREEN}[11] Nitro Checker   {Fore.CYAN}║{Style.RESET_ALL}
{' ' * 10}{Fore.CYAN}║  {Fore.GREEN}[2] Leave Servers        {Fore.CYAN}║  {Fore.GREEN}[7] Webhook Deleter    {Fore.CYAN}║  {Fore.GREEN}[12] MassDM          {Fore.CYAN}║{Style.RESET_ALL}
{' ' * 10}{Fore.CYAN}║  {Fore.GREEN}[3] Onliner              {Fore.CYAN}║  {Fore.GREEN}[8] Hypesquad          {Fore.CYAN}║  {Fore.GREEN}[13] Soon            {Fore.CYAN}║{Style.RESET_ALL}
{' ' * 10}{Fore.CYAN}║  {Fore.GREEN}[4] Nuker                {Fore.CYAN}║  {Fore.GREEN}[9] Raid               {Fore.CYAN}║  {Fore.GREEN}[14] Soon            {Fore.CYAN}║{Style.RESET_ALL}
{' ' * 10}{Fore.CYAN}║  {Fore.GREEN}[5] Token Info           {Fore.CYAN}║  {Fore.GREEN}[10] Nitro Generator   {Fore.CYAN}║  {Fore.GREEN}[15] Credits         {Fore.CYAN}║{Style.RESET_ALL}
{' ' * 10}{Fore.CYAN}╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}
"""

print(banner)


user_input = input("Select an option: ")

if user_input in options:
    selected_option = options[user_input]
    print(selected_option[0])
    subprocess.run(selected_option[1])
else:
    print("Invalid option selected.")
 