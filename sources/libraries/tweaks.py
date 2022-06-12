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
import os, configparser

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def GenerateConfig():
    try: #Create ConfigFile.ini file
        ConfigFile = configparser.ConfigParser()
        ConfigFile.add_section("KEYS")
        ConfigFile.set("KEYS", "API_PUBLIC_KEY", "")
        ConfigFile.set("KEYS", "API_PRIVATE_KEY", "")
        ConfigFile.add_section("TOKENS")
        ConfigFile.set("TOKENS", "API_PUBLIC_TOKEN", "")
        ConfigFile.set("TOKENS", "API_PRIVATE_TOKEN", "")
        with open("config.ini", 'w') as Config:
            ConfigFile.write(Config) #Write to the file
        print('Config file had been successfully generated')
    except:
        print('File already generated somehow.')
