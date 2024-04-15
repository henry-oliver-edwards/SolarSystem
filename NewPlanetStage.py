import pygame

from Colour import Colour
from Utils import top_quarter, centre_text, lower_quarter, random_colour
from Planet import Planet


# TODO Implement planet simulation and when things like sm_axis, eccentricity and d_angle entered add the planet to the screen with those values like a small scale simulation
class NewPlanetStage:

    def __init__(self, screen, universe):
        self.screen = screen
        self.text = pygame.font.Font(r"./assets/fonts/SpaceGrotesk-Regular.ttf", 20)
        self.name_text = self.text.render("Enter a name for your new planet", True, Colour.WHITE.value)
        self.continue_text = self.text.render("Press ENTER to continue", True, Colour.WHITE.value)
        # self.continue_text2 = self.text.render("Press SPACE to continue", True, Colour.WHITE.value)
        self.size_text = self.text.render("Use MOUSE-WHEEL or UP and DOWN to change the planet size",
                                          True, Colour.WHITE.value)
        self.colour_text = self.text.render("Use R to create a random coloured planet", True, Colour.WHITE.value)
        self.sm_axis_text = self.text.render("Enter an sm axis (semi-major axis) for the planet", True,
                                             Colour.WHITE.value)
        self.eccentricity_text = self.text.render("Enter an eccentricity for the planet", True,
                                                  Colour.WHITE.value)
        self.d_angle_text = self.text.render("Enter an d angle for the planet", True,
                                                  Colour.WHITE.value)
        self.name = ""
        self.step = 1
        self.size = 8
        self.universe = universe
        self.colour = [255, 255, 255]
        self.sm_axis = 1
        self.sm_axis_number = []
        self.eccentricity = 0.02
        self.eccentricity_number = []
        self.d_angle = 1
        self.d_angle_number = []


    def create_name(self):
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

    def create_size(self):
        self.screen.fill(Colour.BLACK.value)

        coords = top_quarter(self.screen, self.size_text)
        self.screen.blit(self.size_text, coords)

        enter_coords = lower_quarter(self.screen, self.continue_text)
        self.screen.blit(self.continue_text, enter_coords)

        centre = [self.screen.get_width() / 2, self.screen.get_height() / 2]

        pygame.draw.circle(surface=self.screen, color=self.colour, center=centre,
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

    def create_planet_colour(self):
        self.screen.fill(Colour.BLACK.value)

        coords = top_quarter(self.screen, self.colour_text)
        self.screen.blit(self.colour_text, coords)

        enter_coords = lower_quarter(self.screen, self.continue_text)
        self.screen.blit(self.continue_text, enter_coords)

        centre = [self.screen.get_width() / 2, self.screen.get_height() / 2]

        pygame.draw.circle(surface=self.screen, color=self.colour, center=centre,
                           radius=self.size, width=0)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.step += 1
                elif event.key == pygame.K_r:
                    self.colour = random_colour()

    def create_sm_axis(self):
        self.screen.fill(Colour.BLACK.value)
        coords = top_quarter(self.screen, self.sm_axis_text)
        self.screen.blit(self.sm_axis_text, coords)

        temp_text = self.text.render(str(self.sm_axis), True, Colour.WHITE.value)
        centre_coords = centre_text(self.screen, temp_text)
        self.screen.blit(temp_text, centre_coords)

        enter_coords = lower_quarter(self.screen, self.continue_text)
        self.screen.blit(self.continue_text, enter_coords)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.step += 1
                else:
                    self.sm_axis_number += pygame.key.name(event.key)
                    self.sm_axis = "".join(self.sm_axis_number)

    def create_eccentricity(self):
        self.screen.fill(Colour.BLACK.value)
        coords = top_quarter(self.screen, self.eccentricity_text)
        self.screen.blit(self.eccentricity_text, coords)

        temp_text = self.text.render(str(self.eccentricity), True, Colour.WHITE.value)
        centre_coords = centre_text(self.screen, temp_text)
        self.screen.blit(temp_text, centre_coords)

        enter_coords = lower_quarter(self.screen, self.continue_text)
        self.screen.blit(self.continue_text, enter_coords)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.step += 1
                else:
                    self.eccentricity_number += pygame.key.name(event.key)
                    self.eccentricity = "".join(self.eccentricity_number)

    def create_d_angle(self):
        self.screen.fill(Colour.BLACK.value)
        coords = top_quarter(self.screen, self.d_angle_text)
        self.screen.blit(self.d_angle_text, coords)

        temp_text = self.text.render(str(self.d_angle), True, Colour.WHITE.value)
        centre_coords = centre_text(self.screen, temp_text)
        self.screen.blit(temp_text, centre_coords)

        enter_coords = lower_quarter(self.screen, self.continue_text)
        self.screen.blit(self.continue_text, enter_coords)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.step += 1
                else:
                    self.d_angle_number += pygame.key.name(event.key)
                    self.d_angle = "".join(self.d_angle_number)

    def add_to_universe(self, universe):
        _tmp_planet = Planet(name=self.name, size=self.size, transform=1, sm_axis=float(self.sm_axis),
                             eccentricity=float(self.eccentricity), d_angle=float(self.d_angle), colour=self.colour)
        universe.add_planet(_tmp_planet)

    # def step3(self):
    #     self.screen.fill(Colour.BLACK.value)

    # coords = top_quarter(self.screen, self.colour_text)
    # self.screen.blit(self.colour_text, coords)

    # colour_wheel = create_colour_wheel(radius=100)
    # self.screen.blit(colour_wheel, [540, 360])
    #
    # pygame.display.flip()

    def run(self):
        if self.step == 1:
            self.create_name()
        elif self.step == 2:
            self.create_size()
        elif self.step == 3:
            self.create_planet_colour()
        elif self.step == 4:
            self.create_sm_axis()
        elif self.step == 5:
            self.create_eccentricity()
        elif self.step == 6:
            self.create_d_angle()
        elif self.step == 7:
            self.add_to_universe(self.universe)
            return {"is_done": "done"}
