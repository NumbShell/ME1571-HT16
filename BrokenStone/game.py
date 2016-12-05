import pygame
import os
import time
import random

import card as _card
import crystals as _crystals
import game_render as _render

from pygame.locals import *

flags = FULLSCREEN

pygame.init()

clear = lambda: os.system('cls')

# Defining colors
white = (255, 255, 255)
black = (0, 0, 0)
orange = (242, 114, 19)
bright_orange = (252, 149, 46)

display_width = 1920
display_height = 1200

infoObject = pygame.display.Info()

scaleX = display_width / 1920
scaleY = display_height / 1200

gameDisplay = pygame.display.set_mode((infoObject.current_w, infoObject.current_h), flags)
pygame.display.set_caption('Heroless')


# Store card objects.
PLAYER_cards_hand = []
PLAYER_cards_table = []

AI_cards = []
AI_table_slots = [(display_width/2)-300, (display_width/2)-100, (display_width/2)+100, (display_width/2)+300]
AI_card_placement = 0

# Font for text.
font = pygame.font.SysFont(None, 50)
# Get the time.
clock = pygame.time.Clock()

# Frames per second.
FPS = 30


class Battleground():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.pos_x = 325
        #self.cards_on_battlefield = []

    # Check to see if card is in battleground
    def check(self, cards):
        global card_placement

        if (self.x + self.width) > cur[0] > self.x and (self.y + self.height) > cur[1] > self.y:
            # Get position of the cards and see if they are inside the battleground
            for card in cards:
                if (self.x + self.width) > card.get_pos_x() > self.x and (self.y + self.height) > card.get_pos_y():
                    # Get mouse state
                    (pressed1, pressed2, pressed3) = pygame.mouse.get_pressed()

                    # If user drop card in the battleground box
                    if pressed1 == 0:
                        print(card.get_cost())
                        print(crystal.get_crystals())

                        if card.get_cost() > crystal.get_crystals():
                            print("Out of crystals!")
                        else:
                            # Remove crystals based on Card COST
                            crystal.set_crystals(card.get_cost())

                        # Put card at right spot and disable it so user can't move it again
                        card.canMove = False
                        # Assign card to a spot in the list and close that spot, do same for others!
                        # self.spots.append(card)

                        # Place the cards in a nice line, no matter where you drop them in the arena!
                        if not card in PLAYER_cards_table:
                            print("Placed a card in the arena!")
                            self.pos_x += 200
                            card.set_pos(self.pos_x, 550)
                            PLAYER_cards_table.append(card)

                            #Check for card ID and move the cards with a higher ID -1 in X
                            for c in PLAYER_cards_hand:
                                #Compare where they are in the list instead
                                if PLAYER_cards_hand.index(card) < PLAYER_cards_hand.index(c):
                                    print("True!")
                                #if card.id < c.id:
                                    #card_placement -=1
                                    #c.set_pos(c.x * (0.15 * card_placement), (display_height / 2) + 250)

                        # Remove the card from the players hand  "BUG: Also removes them from TABLE (FIXED)"
                            PLAYER_cards_hand.remove(card)


                        #Loop through the cards in the players deck and fix their X pos
                            """if(card not in self.cards_on_battlefield):
                                self.pos_x += 50
                                card.set_pos(self.pos_x, 400)
                                self.cards_on_battlefield.append(card)"""
                            # card.health = 2


class Button:
    # Init some vars
    def __init__(self, text, color, x, y, width, height):
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self, cur):

        if (self.x + self.width) > cur[0] > self.x and (self.y + self.height) > cur[1] > self.y:
            pygame.draw.rect(gameDisplay, bright_orange, (self.x, self.y, self.width, self.height))
        else:
            pygame.draw.rect(gameDisplay, orange, (self.x, self.y, self.width, self.height))
            # message_display('BATTLE')

    def click(self):
        (pressed1, pressed2, pressed3) = pygame.mouse.get_pressed()
        if pressed1 == 1 and (self.x + self.width) > cur[0] > self.x and (self.y + self.height) > cur[1] > self.y:
            global player_turn
            global AI_turn

            # No need to loop through, only player will press it, AI_turn is called within the AI class(I think)
            if player_turn == True and AI_turn == False:
                player_turn = False
                AI_turn = True
                #print("AI's turn")
                """AI_turn = True
            else:
                player_turn = True
                AI_turn = False"""

            #Works but you must assign a unique ID for each card
            #You can also check so there are no more than 6 cards in the players hand
            global x
            global card_placement

            card_placement+=1

            if len(PLAYER_cards_hand) < 6:
                x+=1
                card = _card.PlayerCard((display_width / 2) * (0.15 * card_placement), (display_height / 2) + 250, 120, 190, 2, 4, 1,x)
                card.img = _render.cards[random.randrange(0,len(_render.cards))]
                PLAYER_cards_hand.append(card)
            else:
                print("Hand is full, card destroyed")

class AI:

    def __init__(self, cards, health):
        self.cards = cards
        self.health = health
        self.crystals = _crystals.Crystals(3)
        self.id = 0

    def play(self):

        #If It's the AI's turn, do something...
        global AI_turn
        global player_turn

        if(AI_turn):
            """Here lies all the behaviors that the AI will play by."""

            _max = PLAYER_cards_hand[0]
            _min = PLAYER_cards_hand[0]
            #First I need to gather information from the player to make a decision.

            #I also need to add a weight to each card that helps the AI to make better moves

            #Place a random card on the table, you have 12 cards total

            #print("AI is thinking... (Not really)")
            #time.sleep(2)
            global AI_card_placement

            if len(AI_cards) == 0:
                card = _card.AICard(AI_table_slots[AI_card_placement], ((display_height / 2) - 350), 120, 190, 2, 4,1, self.id)
                card.img = _render.cards[random.randrange(0, len(_render.cards))]
                AI_cards.append(card)
                AI_table_slots.append(card)
                self.id += 1
            elif len(PLAYER_cards_table) > 0:

                #Find the card with the most worth
                for c in PLAYER_cards_table:
                    #Get the card with max worth.
                    if c.get_worth() > _max.get_worth():
                        _max = c
                        #target = c

                    #Get the card with min worth.
                    if c.get_worth() < _min.get_worth():
                        _min = c

                    """for x in AI_cards:
                        #Compare health of all AI Cards to _min and _max
                        if x.get_health > _min.get_dmg() and x.get_dmg() > _min.get_health():
                            AI_selected_card = x"""


                #Which one can the PC destroy without destroying it's own card?

                target = PLAYER_cards_table[0]
                #Select the card with most worth
                #target = PLAYER_cards_table[random.randrange(0, len(PLAYER_cards_table))]
                AI_selected_card = AI_cards[random.randrange(0, len(AI_cards))]

                #Attack the card
                #print("AI struck " + str(target) + " with " + str(AI_selected_card))
                target.take_dmg(AI_selected_card.damage)
                AI_selected_card.take_dmg(target.damage)
            else:
                #If player has not yet put any card on the table, play another card
                AI_card_placement += 1

                card = _card.AICard(AI_table_slots[AI_card_placement], ((display_height / 2) - 350), 120, 190, 2, 4,1, self.id)
                card.img = _render.cards[random.randrange(0, len(_render.cards))]
                AI_cards.append(card)
                AI_table_slots.append(card)
                self.id += 1



            print("AI has made it's move!")
            time.sleep(1)

            AI_turn = False

            #Reset Player
            crystal.set_crystals(-1)
            player_turn = True

#Make a method that handle the creation of cards?
"""def create_card(type, num, list, pos):

        for i in range(num):
            card = type((display_width / 2) * (0.15 * card_placement), (display_height / 2) + 250, 120, 190, 2,
                                4, 1, x)
            card.img = cards[random.randrange(0, len(cards))]
            list.append(card)"""


def message_to_screen(msg, color, x, y):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [x, y])


# Scale backgrounds to the current display size e.g 1280x720
for obj in range(len(_render.bgs)):
    _render.bgs[obj] = pygame.transform.scale(_render.bgs[obj], (display_width, display_height))

# Scale cards to the current display size e.g 1280x720
"""for obj in range(len(cards)):
    cards[obj] = pygame.transform.scale(cards[obj], (int(200*scaleX), int(276*scaleY)))
    print(cards[obj].get_rect().size)"""

#Player crystals
crystal = _crystals.Crystals(1)

#This will be used to place the cards in the players hand correctly
card_placement = 0

# Create cards and add them to card_list  NOTE: Create all the 30 cards and add to list, then select 4 at random to start with! <------ READ THIS PLEASE
#Create the starting cards
for x in range(4):
    card = _card.PlayerCard((display_width / 2) * (0.15 * x), (display_height / 2) + 250, 120, 190, random.randrange(1, 5), random.randrange(1, 5), 1, x)
    card.img = _render.cards[x]
    PLAYER_cards_hand.append(card)


# Some vars
canChange = True
current_card = 0
current_selected = 0

player_turn = True
AI_turn = False

gameExit = False
menuExit = True

gameDisplay.blit(_render.bgs[2], [0, 0])
pygame.display.update()

# Create Battleground
battleground = Battleground(350, 300, 1100, 350)

# text, color, x, y, width, height
play = Button('Play', orange, display_width / 2, display_height / 2, 200, 70)
end_turn = Button('END TURN', orange, display_width - 450, (display_height / 2) - 80, 150, 70)


PC = AI(15, 30)

# --------------MAIN GAME LOOP---------------

while not gameExit:
    #print(player_turn)

    # get current mouse pos and button clicking
    cur = pygame.mouse.get_pos()
    (pressed1, pressed2, pressed3) = pygame.mouse.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True

    while not menuExit:
        cur = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.blit(_render.bgs[2], (0, 0))

        # self, text, color, x, y, width, height
        #play.draw(cur)

    # message_to_screen('TwistStone', white)

    # Draws the background image to the screen
    gameDisplay.blit(_render.bgs[2], [0, 0])
    crystal.render_crystals()

    # Render PC Cards
    #gameDisplay.blit(PC_cards[1], [display_width / 2, display_height / 2 - 330])

    # End turn button.
    end_turn.draw(cur)
    end_turn.click()

    """for x in range(12):
        x = gameDisplay.blit(backs[0], [1650+(x*3),650])

        back_list.append(x)

    for x in range(12):
        x = gameDisplay.blit(backs[1], [1650+(x*3),100])
        back_list.append(x)
    #gameDisplay.fill(white)"""

    """Create a list containing all the cards and
    then iterate through them and change their pos and background!"""

    # x.render()
    # y.render()

    # x.move(cur)
    # y.move()

    #Render PC cards
    for card in AI_cards:
        card.render()
        card.is_dead(AI_cards)

    #Render player cards on the table
    for c in PLAYER_cards_table:
        c.render()
        c.is_dead(PLAYER_cards_table)

    #Render player cards in the hand
    for card in PLAYER_cards_hand:
        card.render()


        # gameDisplay.blit(bgs[3], x.rect)
        """If the card the user press is equal to the card he is hovering over
        move that card, the other card wont be affected because it's applied only on press DOWN
        not on HOLD"""

        # -------------------------------
        # CODE BELOW MAKE SO YOU CAN MOVE EACH CARD ON THEIR OWN WITHOUT INTERFERING WITH EACH OTHER
        # -------------------------------


        if player_turn:
            #crystal.set_crystals(1)

            #Check if any crystals are left
            for c in PLAYER_cards_hand:
                if crystal.crystals <= 0:
                    c.canMove = False
                else:
                    c.canMove = True

            # 1. Look at what ID the cursor is hovering over and apply it to current_hover
            #(pressed1, pressed2, pressed3) = pygame.mouse.get_pressed()
            if pressed1 == 1:
                current_selected = card.current(cur)

            # print(current_hover)

            # 2. If that card is pressed, assign that ID to current_card
            if current_selected != None and pressed1 == 1 and canChange == True:
                current_card = card.current(cur)
                canChange = False

            # 3. As long as the button is held down, move THIS card with THIS id
            if current_selected == current_card:
                card.move(cur)

            # 4. If mouse is not held down, reset current_card
            if pressed1 == 0:
                current_card = 0
                current_selected = 0
                canChange = True

            """When user let go of mouse, assign current_card to an "old_card" var to be used"""

    # Check if player is selecting a card on the table, if he is call the ATTACK method from Card
    if pressed1 == 1:
        for c in PLAYER_cards_table:
            current = c.current(cur)
            if c.get_id() == current:
                print("That's it!")


    battleground.check(PLAYER_cards_hand)
    # print(battleground.spots)

    PC.play()

    # Update the display
    pygame.display.update()

    # Keeps it at the specified fps
    clock.tick(FPS)
    # clear()
    # print(clock.get_fps())

pygame.quit()
quit()