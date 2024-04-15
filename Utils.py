import pygame
from pygame import Surface
from math import sin, cos, radians, floor


def to_delay(multi):
    return int((1 / multi) * 1000)


def centre_text(screen, text):
    x = (screen.get_width() / 2) - (text.get_width() / 2)
    y = (screen.get_height() / 2) - (text.get_height() / 2)
    return [x, y]


def top_quarter(screen, text):
    x = (screen.get_width() / 2) - (text.get_width() / 2)
    y = (screen.get_height() / 4) - (text.get_height() / 2)
    return [x, y]


def lower_quarter(screen, text):
    x = (screen.get_width() / 2) - (text.get_width() / 2)
    y = ((screen.get_height() / 4) * 3) - (text.get_height() / 2)
    return [x, y]


def create_colour_wheel(radius, saturation=1):
    surface = Surface((radius, radius))
    iters = 360 * radius

    for i in range(iters):
        if i <= 360:
            x = radius * cos(radians(i))
            y = radius * sin(radians(i))
            surface.set_at([x, y], pygame.Color(hsl_to_rbg(h=i, s=saturation, l=1)))
        else:
            rotation = floor(i / 360)
            deg = i - (rotation * 360)
            x = (radius - rotation) * cos(radians(deg))
            y = (radius - rotation) * sin(radians(deg))
            surface.set_at([x, y], pygame.Color(hsl_to_rbg(h=deg, s=saturation, l=1)))

    return surface


def hsl_to_rbg(h, s, l):
    if s == 0:
        r = g = b = l
    else:
        if l < 0.5:
            q = l * (1 + s)
        else:
            q = l + s - l * s

        p = 2 * l - q

        r = int(hue_to_rgb(p, q, h + 1 / 3))
        g = int(hue_to_rgb(p, q, h))
        b = int(hue_to_rgb(p, q, h - 1 / 3))

        print(r, g, b)

    return [r, g, b]


def hue_to_rgb(p, q, t):
    if t < 0:
        t += 1
    elif t > 0:
        t -= 1
    elif t < 1 / 6:
        return p + (q - p) * 6 * t
    elif t < 1 / 2:
        return q
    elif t < 2 / 3:
        return p + (q - p) * (2 / 3 - t) * 6
