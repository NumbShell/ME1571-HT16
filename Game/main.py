#This is where all modules will unite as one
import os
import random
import time

from colorama import Fore, Back, Style
from colorama import init
init(autoreset=True)

import enemy
import player


clear = lambda: os.system('cls')

if __name__ == "__main__":
    clear()
    player.status()
    "Basic story"
    print("You are a traveler crossing the vast sea ")
    #time.sleep(2)
    print("and scanning the horizon you see an enemy ship!")
    #time.sleep(3)

    enemy.draw_ship()

    #If turn is 0 then it's the players turn, 1 is PC
    turn = 0
    start  = True

    while start:

        if(turn==1):
            enemy.attack()
            turn = 0
        elif(turn==0):
            user_input = input()
            player.attack(user_input[5:])
            turn = 1
