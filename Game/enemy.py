import os
import random
import main

from colorama import Fore, Back, Style
from colorama import init

import player

init(autoreset=True)
clear = lambda: os.system('cls')

hp = 100
dmg = 30


engine = 4
generator = 2
turret = 0
radar = 6

#Store all the ship parts with their color
parts = ['TURRET', Fore.RED + Style.BRIGHT + 'TURRET',
         'GENERATOR', Fore.RED + Style.BRIGHT + 'GENERATOR',
         'ENGINE', Fore.RED + Style.BRIGHT + 'ENGINE',
         'RADAR', Fore.RED + Style.BRIGHT + 'RADAR']

current_ship = 0

#Draws the ship and prints it out
def draw_ship():
    ships = [Fore.WHITE + '                       \n          ______     _____\n  _______/' + parts[turret] + Fore.WHITE + '\___/' +parts[radar] + Fore.WHITE + '\___\n \_' + parts[generator] + Fore.WHITE + '___________' + parts[engine] + Fore.WHITE + '|\n' + Fore.LIGHTBLUE_EX + Style.BRIGHT + '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~']

    current_ship = random.randrange(0, len(ships))

    print(ships[current_ship])
    # print(ships[2])


def ship_damage(part):
    # What part did they hit? Find out and change the color of that to red
    if part == 'turret':
        global turret
        turret = turret + 1
    if part == 'generator':
        global generator
        generator = generator + 1
    if part == 'radar':
        global radar
        radar = radar + 1
    if part == 'engine':
        global engine
        engine = engine + 1

def attack():
    chance = random.randrange(0,10)

    if(chance >= 5):
        print("Enemy fired and got a direct hit!")
        dmg = random.randrange(20,30)

        #apply damage to the player's health
        player.dmg_hp(dmg)
    else:
        print("Enemy missed!")

    #player.attack()