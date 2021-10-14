import pygame

from Colour import Colour


class IntroStage:

    def __init__(self, screen):
        self.screen = screen
        self.text = pygame.font.Font(r"./assets/fonts/SpaceGrotesk-Regular.ttf", 20)
        self.inStage = True

    def show(self):
        self.screen.fill(Colour.BLACK.value)
        render_text = self.text.render("Press space to start and space to pause", True, Colour.WHITE.value)
        x = (self.screen.get_width()/2) - (render_text.get_width()/2)
        y = (self.screen.get_height()/2) - (render_text.get_height()/2)
        self.screen.blit(render_text, (x, y))
        pygame.display.flip()
