#Author: 808-Dev
#License: GPL - GNU General Public License
#Version: V.1.0.0 (Version 1)
#-----------------------------------------
#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <https://www.gnu.org/licenses/>.
#------------------------------------------
#You didn't get a copy cuz your a loser! Ahaha
#------------------------------------------
from colorama import init, Fore, Style
init(autoreset=True)
def PrintBad(data):
    print(Style.BRIGHT + Fore.RED + data)
def PrintGood(data):
    print(Style.BRIGHT + Fore.GREEN + data)
def PrintWarn(data):
    print(Style.BRIGHT + Fore.YELLOW + data)
def PrintStatus(data):
    print(Style.BRIGHT + Fore.BLUE + data)