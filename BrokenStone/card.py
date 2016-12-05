import game_render
import pygame

class Card:
    # Init some variables.

    def __init__(self, x, y, width, height, damage, health, cost, _id):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.id = _id
        self.pos = 0
        self.cost = cost

        self.damage = damage
        self.health = health
        self._health = health
        self.canMove = True

    def get_worth(self):
        return self.damage + self._health

    def set_pos(self, x, y):
        self.x = x
        self.y = y

    def take_dmg(self, dmg):
        self.health -= dmg

    def get_dmg(self):
        return self.damage

    def get_health(self):
        return self._health

    def get_id(self):
        return self.id

    def get_pos_x(self):
        pos = (self.x + self.width)
        return pos

    def get_pos_y(self):
        pos = (self.y + self.height)
        return pos

    def get_cost(self):
        return self.cost

    def get_img(self):
        return self.img

    def img(self, img):
        self.img = pygame.image.load(img)

    def is_dead(self, table_card):
        if self.health <= 0:
            print("Card destroyed!")
            table_card.remove(self)

    def render(self):
        # Change size of card
        new_img = pygame.transform.scale(self.img, (self.width + 80, self.height + 90))
        game_render.gameDisplay.blit(new_img, [self.x, self.y])

        # Render out HEALTH
        game_render.message_to_screen(str(self.health), game_render.white, self.x + self.width * 1.35, self.y + self.height * 1.25)

        # Render out DAMAGE
        game_render.message_to_screen(str(self.damage), game_render.white, self.x + self.width - 98, self.y + self.height * 1.25)

    def current(self, cur):
        if (self.x + self.width + 100) > cur[0] > self.x and (self.y + self.height + 100) > cur[1] > self.y:
            return self.id


class PlayerCard(Card):

    def __init__(self, x, y, width, height, damage, health, cost, _id):
        super().__init__(x, y, width, height, damage, health, cost, _id)


    def attack(self, cur):
        #if player clicks on this card while it's on the table
        if (self.x + self.width + 100) > cur[0] > self.x and (self.y + self.height + 100) > cur[1] > self.y:
            print("YOU ARE IN THE CARD")
            #Let player select the card to attack by clicking on it.

    def move(self, cur):
        if self.canMove == True:
            if (self.x + self.width + 100) > cur[0] > self.x and (self.y + self.height + 100) > cur[1] > self.y:
                (pressed1, pressed2, pressed3) = pygame.mouse.get_pressed()

                if pressed1 == 1:
                    self.x = cur[0] - (self.width)
                    self.y = cur[1] - (self.height)

                    # rect_obj = (self.x, self.y, self.width+150, self.height+150)
                    # rects.append(rect_obj)
                    # return self.id
                else:
                    return 0

#Make an AI card class
class AICard(Card):

    def __init__(self, x, y, width, height, damage, health, cost, _id):
        super().__init__(x, y, width, height, damage, health, cost, _id)


