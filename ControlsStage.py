import pygame
from Colour import Colour


class ControlStage:

    def __init__(self, screen):
        self.screen = screen
        self.text = pygame.font.Font(r"./assets/fonts/SpaceGrotesk-Regular.ttf", 20)
        self.inStage = True

    def show(self):
        # self.screen.fill(Colour.BLACK.value)
        render_text_speed_up = self.text.render("Press W to speedup the simulation", True, Colour.WHITE.value)
        render_text_speed_down = self.text.render("Press S to slowdown the simulation", True, Colour.WHITE.value)
        x = (self.screen.get_width() / 2) - (render_text_speed_up.get_width() / 2)
        speed_up_y = (self.screen.get_height() / (1 / 4)) - (render_text_speed_up.get_height() / 2)
        slowdown_y = (self.screen.get_height() / (3 / 4)) - (render_text_speed_down.get_height() / 2)
        self.screen.blit(render_text_speed_up, (x, speed_up_y))
        self.screen.blit(render_text_speed_down, (x, slowdown_y))
        pygame.display.flip()
