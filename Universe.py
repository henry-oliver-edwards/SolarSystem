import copy
from math import sin, cos, radians, sqrt, floor
import pygame.draw

from Colour import Colour
from Utils import to_delay


def kepler_solver(planet):
    temp1 = planet.a * (1 - planet.e ** 2)
    temp2 = 1 + planet.e * cos(radians(planet.theta))
    planet.r = temp1 / temp2
    return planet


def correction_func(x):
    return sqrt(x) * 2


def correction_size_func(x):
    return sqrt(x) + 2

# Conversion is the factor to change AU into a px value
# conversion variable turns AU into px, a scaling factor
def coordinate_solver(planet, r, conversion, screen_width, screen_height):
    x = ((r * cos(radians(planet.theta))) * conversion) + (screen_width/2)
    y = ((r * sin(radians(planet.theta))) * conversion) + (screen_height/2)
    planet.position = [x, y]
    return planet


# Simulate the planet at 0 degree's
def norm_simulate0(planet, screen_width, screen_height):
    planet.theta = 0
    temp1 = kepler_solver(planet)
    temp2 = coordinate_solver(temp1, temp1.r, 100, screen_width, screen_height)
    return temp2


# Simulate the planet at 90 degree's,
# the change in degree's should give the
# max x and y of the planets orbit
def norm_simulate90(planet, screen_width, screen_height):
    planet.theta = 90
    temp1 = kepler_solver(planet)
    temp2 = coordinate_solver(temp1, temp1.r, 100, screen_width, screen_height)
    return temp2


class Universe:

    def __init__(self, bodies, screen, multi):
        self.bodies = bodies
        self.screen = screen
        self.multi = multi
        self.simulation_speed = to_delay(multi)
        self.time = 0
        self.day = 0
        self.text = pygame.font.Font(r"./assets/fonts/SpaceGrotesk-Regular.ttf", 20)
        self.correction = correction_func
        self.correction_size = correction_size_func

    def tick(self):
        for body in self.bodies:
            body.theta += body.rotation
            self.update_position()
        if self.day == 0:
            self.normalise()
            self.norm_size()
        self.norm_coordinates()
        self.update_day()
        self.update_simulation_speed()

    def update_position(self):
        _bodies = []
        for body in self.bodies:
            if body.name != "Sun":
                temp1 = kepler_solver(body)
                temp1.r = self.correction(temp1.r)
                temp2 = coordinate_solver(temp1, temp1.r, 100, self.screen.get_width(), self.screen.get_height())
                _bodies.append(temp2)
            elif body.name == "Sun":
                _bodies.append(body)
        self.bodies = _bodies

    def update_day(self):
        self.day += 1

    def update_simulation_speed(self):
        self.simulation_speed = to_delay(self.multi)

    def normalise(self):
        maxA = 0
        maxBody = None
        for body in self.bodies:
            if body.name != "Sun":
                if body.a > maxA:
                    maxA = body.a
                    maxBody = body

        planet0 = copy.deepcopy(maxBody)
        planet90 = copy.deepcopy(maxBody)
        temp0 = norm_simulate0(planet0, self.screen.get_width(), self.screen.get_height())
        temp90 = norm_simulate90(planet90, self.screen.get_width(), self.screen.get_height())
        if temp0.position[0] < temp90.position[0]:
            maxX = temp90.position[0]
        elif temp0.position[0] > temp90.position[0]:
            maxX = temp0.position[0]

        if temp0.position[1] < temp90.position[1]:
            maxY = temp90.position[1]
        elif temp0.position[1] > temp90.position[1]:
            maxY = temp0.position[1]

        scaleX = self.screen.get_width()/maxX
        scaleY = self.screen.get_height()/maxY
        self.scale_factor = [(floor(scaleX*100))/100, (floor(scaleY*100))/100]

    # Normalise the coordinates to the scale factors
    def norm_coordinates(self):
        temp1 = self.screen.get_width()*self.scale_factor[0]
        const_x = self.screen.get_width() - temp1
        temp2 = self.screen.get_height()*self.scale_factor[1]
        const_y = self.screen.get_height() - temp2
        for body in self.bodies:
            if body.name != "Sun":
                body.position[0] *= self.scale_factor[0]
                body.position[0] += (const_x/2)
                body.position[1] *= self.scale_factor[1]
                body.position[1] += (const_y/2)

    # Normalise the size of the planet the scale factors
    def norm_size(self):
        for body in self.bodies:
            if body.name != "Sun":
                body.size = self.correction_size(body.size)

    def draw(self):
        self.screen.fill(Colour.BLACK.value)
        for body in self.bodies:
            pygame.draw.circle(surface=self.screen, color=body.colour, center=body.position,
                               radius=body.size, width=0)

        day_text = self.text.render(f"Current day: {self.day}", True, Colour.WHITE.value)
        speed_text = self.text.render(f"Speed: {self.multi}x", True, Colour.WHITE.value)
        self.screen.blit(day_text, (5, 5))
        self.screen.blit(speed_text, (5, 30))
        pygame.display.flip()
        pygame.time.delay(self.simulation_speed)

    def add_planet(self, planet):
        self.bodies.append(planet)
