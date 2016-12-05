import game_render

class Crystals():
    """This class will keep track of everything concerning the crystals"""

    def __init__(self, count):
        self.crystals = count

    def get_crystals(self):
        return self.crystals

    def set_crystals(self, cost):
        self.crystals -= cost

    def render_crystals(self):
        # Render out HEALTH
        game_render.message_to_screen(str(self.crystals), game_render.white, 1250, 1080)