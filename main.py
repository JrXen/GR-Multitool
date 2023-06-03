import subprocess
from colorama import init, Fore, Style

init(autoreset=True)

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
    "12": ["Starting Vouch",  ["python", "modules/vouch.py"]],
    "13": ["..................",  ["python", "modules/pinger.py"]],
    "14": ["..................",  ["python", "modules/discordbotnuker.py"]],    
    "15": ["=.=",  ["python", "modules/serverclonermenu.py"]],        
    "16": ["=.=",  ["python", "modules/credits.py"]]    
}

banner = f"""
{Fore.MAGENTA}
{' ' * 40}  /$$$$$$  /$$$$$$$ 
{' ' * 40} /$$__  $$| $$__  $$
{' ' * 40}| $$  \__/| $$  \ $$
{' ' * 40}| $$ /$$$$| $$$$$$$/
{' ' * 40}| $$|_  $$| $$__  $$
{' ' * 40}| $$  \ $$| $$  \ $$
{' ' * 40}|  $$$$$$/| $$  | $$
{' ' * 40}\______/ |__/  |__/

{' ' * 42}made by GR#1111
{Style.RESET_ALL}

{' ' * 10 + Fore.MAGENTA + '╔══════════════════════════════════════════════════════════════════════════════════════════════════════╗' + Style.RESET_ALL}
{' ' * 10 + Fore.MAGENTA + '║  ' + Fore.CYAN + '[1] Token Checker        ' + Fore.MAGENTA + '  ' + Fore.CYAN + '[6] Webhook Spammer    ' + Fore.MAGENTA + '  ' + Fore.CYAN + '[11] Nitro Checker     ' + Fore.MAGENTA + '  ' + Fore.CYAN + '[16] Credits           ' + Fore.MAGENTA + '║' + Style.RESET_ALL}
{' ' * 10 + Fore.MAGENTA + '║  ' + Fore.CYAN + '[2] Leave Servers        ' + Fore.MAGENTA + '  ' + Fore.CYAN + '[7] Webhook Deleter    ' + Fore.MAGENTA + '  ' + Fore.CYAN + '[12] Vouches           ' + Fore.MAGENTA + '  ' + Fore.CYAN + '[17] Soon              ' + Fore.MAGENTA + '║' + Style.RESET_ALL}
{' ' * 10 + Fore.MAGENTA + '║  ' + Fore.CYAN + '[3] Onliner              ' + Fore.MAGENTA + '  ' + Fore.CYAN + '[8] Hypesquad          ' + Fore.MAGENTA + '  ' + Fore.CYAN + '[13] Ping Raid         ' + Fore.MAGENTA + '  ' + Fore.CYAN + '[18] Soon              ' + Fore.MAGENTA + '║' + Style.RESET_ALL}
{' ' * 10 + Fore.MAGENTA + '║  ' + Fore.CYAN + '[4] Nuker                ' + Fore.MAGENTA + '  ' + Fore.CYAN + '[9] Raid               ' + Fore.MAGENTA + '  ' + Fore.CYAN + '[14] Bot Nuker         ' + Fore.MAGENTA + '  ' + Fore.CYAN + '[15] Soon              ' + Fore.MAGENTA + '║' + Style.RESET_ALL}
{' ' * 10 + Fore.MAGENTA + '║  ' + Fore.CYAN + '[5] Token Info           ' + Fore.MAGENTA + '  ' + Fore.CYAN + '[10] Nitro Generator   ' + Fore.MAGENTA + '  ' + Fore.CYAN + '[15] Server Cloner     ' + Fore.MAGENTA + '  ' + Fore.CYAN + '[19] Soon              ' + Fore.MAGENTA + '║' + Style.RESET_ALL}
{' ' * 10 + Fore.MAGENTA + '╚══════════════════════════════════════════════════════════════════════════════════════════════════════╝' + Style.RESET_ALL}
"""
print(banner)

user_input = input("Select an option: ")

if user_input in options:
    selected_option = options[user_input]
    print(selected_option[0])
    subprocess.run(selected_option[1])
else:
    print("Invalid option selected.")
