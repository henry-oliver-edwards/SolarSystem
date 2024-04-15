import pygame

from Colour import Colour
from Utils import top_quarter, centre_text, lower_quarter, create_colour_wheel


class NewPlanetStage:

    def __init__(self, screen):
        self.screen = screen
        self.text = pygame.font.Font(r"./assets/fonts/SpaceGrotesk-Regular.ttf", 20)
        self.name_text = self.text.render("Enter a name for your new planet", True, Colour.WHITE.value)
        self.continue_text = self.text.render("Press SPACE to continue", True, Colour.WHITE.value)
        self.size_text = self.text.render("Use MOUSE-WHEEL or UP and DOWN to change the planet size",
                                          True, Colour.WHITE.value)
        # self.colour_text = self.text.render("Select the planet colour from the colour wheel", True, Colour.WHITE.value)
        self.name = ""
        self.step = 1
        self.size = 8

    def step1(self):
        self.screen.fill(Colour.BLACK.value)

        coords = top_quarter(self.screen, self.name_text)
        self.screen.blit(self.name_text, coords)

        temp_text = self.text.render(self.name, True, Colour.WHITE.value)
        centre_coords = centre_text(self.screen, temp_text)
        self.screen.blit(temp_text, centre_coords)

        enter_coords = lower_quarter(self.screen, self.continue_text)
        self.screen.blit(self.continue_text, enter_coords)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.name += " "
                elif event.key == pygame.K_RETURN:
                    self.step += 1
                elif pygame.key.name(event.key).isalnum():
                    self.name += pygame.key.name(event.key)

    def step2(self):
        self.screen.fill(Colour.BLACK.value)

        coords = top_quarter(self.screen, self.size_text)
        self.screen.blit(self.size_text, coords)

        enter_coords = lower_quarter(self.screen, self.continue_text)
        self.screen.blit(self.continue_text, enter_coords)

        centre = [self.screen.get_width() / 2, self.screen.get_height() / 2]

        pygame.draw.circle(surface=self.screen, color=Colour.WHITE.value, center=centre,
                           radius=self.size, width=0)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.step += 1
                elif event.key == pygame.K_UP:
                    self.size += 1
                elif event.key == pygame.K_DOWN:
                    self.size += 1
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    self.size += 1
                elif event.button == 5:
                    self.size -= 1

    def step3(self):
        self.screen.fill(Colour.BLACK.value)

        # coords = top_quarter(self.screen, self.colour_text)
        # self.screen.blit(self.colour_text, coords)


        # colour_wheel = create_colour_wheel(radius=100)
        # self.screen.blit(colour_wheel, [540, 360])
        #
        # pygame.display.flip()

    def run(self):
        if self.step == 1:
            self.step1()
        elif self.step == 2:
            self.step2()
        elif self.step == 3:
            self.step3()
