#! /usr/bin/python3
#
#   Uninstall github-webscrapping
#
#   GitHub WebScrapping | github-webscrapping uninstall script
#   GitHub: https://github.com/TheWatcherMultiversal/github-webscrapping
#
#   License: GPLv3 (GNU/General Public License version 3.0)
#
# ------------------------------------------------------------------ (*)
#   |
#   |
#   °-- Include modules:

import subprocess
try:
    from colorama import Fore
except ImportError:
    print("Install python3-colorama to be able to run the installation script.")

# ------------------------------------------------------------------ (*)
#   |
#   |
#   °-- Remove pdfgui_tools if it's previously installed:

print(Fore.YELLOW + '\r\nThe following command requires superuser privileges:' + Fore.RESET + ' sudo rm -r\r\n')
print(Fore.GREEN + 'Removing github-webscrapping from the system...' + Fore.RESET)

subprocess.run(f'sudo rm -r /usr/bin/github-webscrapping /usr/share/github-webscrapping/ /usr/share/applications/github-webscrapping.desktop /usr/share/doc/github-webscrapping/', shell=True)

print(Fore.GREEN + '\r\ngithub-webscrapping was successfully removed' +  Fore.RESET)