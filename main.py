import pygame

from Colour import Colour
from Planet import Planet
from Universe import Universe

resolution = (1080, 720)

# Inner Solar System
Sun = Planet(name="Sun", size=109, transform=1/7.5, position=[resolution[0] / 2, resolution[1] / 2],
             colour=Colour.SUN.value)
Mercury = Planet(name="Mercury", size=0.383, transform=10, sm_axis=0.39, eccentricity=0.21, d_angle=4.15,
                 colour=Colour.MERCURY.value)
Venus = Planet(name="Venus", size=0.910, transform=8, sm_axis=0.72, eccentricity=0.01, d_angle=1.63,
               colour=Colour.VENUS.value)
Earth = Planet(name="Earth", size=1, transform=8, sm_axis=1, eccentricity=0.02, d_angle=1, colour=Colour.EARTH.value)
Mars = Planet(name="Mars", size=0.533, transform=10, sm_axis=1.52, eccentricity=0.09, d_angle=0.531,
              colour=Colour.MARS.value)

# Outer Solar System
Jupiter = Planet(name="Jupiter", size=11.2, transform=1, sm_axis=5.20, eccentricity=0.049, d_angle=0.084,
                 colour=Colour.JUPITER.value)
Saturn = Planet(name="Saturn", size=9.45, transform=1, sm_axis=9.58, eccentricity=0.057, d_angle=0.034,
                colour=Colour.SATURN.value)
Uranus = Planet(name="Uranus", size=4, transform=1, sm_axis=19.22, eccentricity=0.046, d_angle=0.01189,
                colour=Colour.URANUS.value)
Neptune = Planet(name="Neptune", size=3.9, transform=1, sm_axis=30.07, eccentricity=0.0087, d_angle=0.0061,
                 colour=Colour.NEPTUNE.value)


def main():
    multi = 1
    pygame.init()
    screen = pygame.display.set_mode(resolution)
    universe = Universe(bodies=[Sun, Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune], screen=screen, multi=multi)
    running = True
    simulate = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    multi += 1
                    universe.multi = multi
                elif event.key == pygame.K_s:
                    multi -= 1
                    universe.multi = multi

                if event.key == pygame.K_SPACE:
                    simulate = not simulate
        if simulate:
            universe.tick()
            universe.draw()


if __name__ == '__main__':
    main()
