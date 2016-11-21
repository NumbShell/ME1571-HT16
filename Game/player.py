import random
import enemy
import os
import time

from colorama import Fore, Back, Style
from colorama import init
init(autoreset=True)

clear = lambda: os.system('cls')

hp = 100
visibility = 80

def get_visibility():
    return visibility

def get_hp():
    return hp

#change hp based on input and then prints it out
def dmg_hp(dmg):
    global hp
    hp = hp - dmg
    status()

def status():
    if hp <= 0:
        print("Your ship sank.")
        time.sleep(3)
        clear()
        print("Run program to try again!")

    elif hp <= 25:
        print(Fore.RED + Style.BRIGHT + 'HP:' + str(hp) + Fore.WHITE + '   VSB:' + str(visibility))
        print("_________________________________________")
    elif hp <= 50:
        print(Fore.YELLOW + Style.BRIGHT + 'HP:' + str(hp) + Fore.WHITE + '   VSB:' + str(visibility))
        print("_________________________________________")

    else:
        print(Fore.GREEN + Style.BRIGHT + 'HP:' + str(hp) + Fore.WHITE + '   VSB:' + str(visibility))
        print("_________________________________________")


def attack(part):
    chance = random.randrange(0, 10)
    if (part == 'turret' or part == 'engine' and chance >= 5):
        clear()
        print('You blew up the ' + part + '!')
        enemy.ship_damage(part)
        enemy.draw_ship()

    elif (part == 'generator' or part == 'radar' and chance >= 7):
        clear()
        print('You blew up the ' + part + '!')
        enemy.ship_damage(part)
        enemy.draw_ship()
    else:
        print('You missed!')
    #enemy.attack()